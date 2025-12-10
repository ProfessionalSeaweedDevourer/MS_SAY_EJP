const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

// --- 환경 설정 ---
const PORT = 7777;
const CANVAS_SIZE = 666;
const BAR_WIDTH = 100;
const BAR_HEIGHT = 15;

const app = express();
const server = http.createServer(app);
const io = socketIo(server); 

// 정적 파일 제공 설정
app.use(express.static(path.join(__dirname))); 

// 기본 라우팅 (Host)
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'host.html'));
});

// Guest 라우팅
app.get('/guest', (req, res) => {
    res.sendFile(path.join(__dirname, 'guest.html'));
});

// --- 게임 상태 변수 (서버에서 관리) ---
let gameData = {
    ballX: CANVAS_SIZE / 2,
    ballY: CANVAS_SIZE / 2,
    dx: 4,
    dy: 4,
    hostBarX: (CANVAS_SIZE / 2) - (BAR_WIDTH / 2),
    guestBarX: (CANVAS_SIZE / 2) - (BAR_WIDTH / 2),
    isBallAlive: false, 
    // 실제 볼 크기는 클라이언트에서 받은 후 초기화 로직에 반영하는 것이 정확하지만,
    // 여기서는 간단하게 상수로 가정합니다. (probe.png 크기에 맞게 임의 설정)
    BALL_RADIUS: 25 
};

let playerCount = 0;
let hostSocketId = null;
let guestSocketId = null;
let gameInterval = null;

// --- 서버 측 게임 루프 ---
function gameLoop() {
    if (!gameData.isBallAlive) return;

    const BALL_RADIUS = gameData.BALL_RADIUS;
    const BAR_Y_HOST = CANVAS_SIZE - BAR_HEIGHT; // 호스트 바 위치 (하단)
    const BAR_Y_GUEST = 0; // 게스트 바 위치 (상단)

    // 1. 공 이동
    gameData.ballX += gameData.dx;
    gameData.ballY += gameData.dy;

    // 2. 벽 충돌 판정 (좌/우)
    if (gameData.ballX + BALL_RADIUS >= CANVAS_SIZE || gameData.ballX - BALL_RADIUS <= 0) {
        gameData.dx *= -1;
    }

    // 3. 바/골 충돌 판정

    // 3-1. Host 바 (하단) 충돌 판정
    if (gameData.dy > 0 && 
        gameData.ballY + BALL_RADIUS >= BAR_Y_HOST && 
        gameData.ballY + BALL_RADIUS <= BAR_Y_HOST + BAR_HEIGHT &&
        gameData.ballX + BALL_RADIUS > gameData.hostBarX && 
        gameData.ballX - BALL_RADIUS < gameData.hostBarX + BAR_WIDTH) {
        
        const hitPoint = gameData.ballX - (gameData.hostBarX + BAR_WIDTH / 2);
        gameData.dx = hitPoint * 0.3; // 반사각 적용
        gameData.dy *= -1;
    } 
    // 3-2. Guest 바 (상단) 충돌 판정
    else if (gameData.dy < 0 && 
             gameData.ballY - BALL_RADIUS <= BAR_Y_GUEST + BAR_HEIGHT &&
             gameData.ballY - BALL_RADIUS >= BAR_Y_GUEST &&
             gameData.ballX + BALL_RADIUS > gameData.guestBarX && 
             gameData.ballX - BALL_RADIUS < gameData.guestBarX + BAR_WIDTH) {
        
        const hitPoint = gameData.ballX - (gameData.guestBarX + BAR_WIDTH / 2);
        gameData.dx = hitPoint * 0.3; // 반사각 적용
        gameData.dy *= -1;
    }
    
    // 3-3. Host 골 (아래쪽 통과) - 게임 종료 및 게스트 승리
    else if (gameData.ballY + BALL_RADIUS >= CANVAS_SIZE) {
        gameData.isBallAlive = false; 
        clearInterval(gameInterval);
        gameInterval = null;
        io.emit('game_over', { winner: 'guest' });
    } 
    // 3-4. Guest 골 (위쪽 통과) - 게임 종료 및 호스트 승리
    else if (gameData.ballY - BALL_RADIUS <= 0) {
        gameData.isBallAlive = false; 
        clearInterval(gameInterval);
        gameInterval = null;
        io.emit('game_over', { winner: 'host' });
    }

    // 4. 모든 클라이언트에게 최신 게임 상태 브로드캐스트
    io.emit('game_state', gameData);
}


// --- Socket.IO 이벤트 처리 ---
io.on('connection', (socket) => {
    if (playerCount < 2) {
        playerCount++;

        if (playerCount === 1) {
            hostSocketId = socket.id;
            socket.emit('role', 'host');
        } else if (playerCount === 2) {
            guestSocketId = socket.id;
            socket.emit('role', 'guest');
            // 두 플레이어 모두 연결되면 호스트에게 알림
            io.to(hostSocketId).emit('player_status', 'guest_joined');
        }
        
        // 초기 게임 상태 전달
        socket.emit('game_state', gameData);

    } else {
        socket.emit('message', '게임이 이미 진행 중입니다. 다음에 시도해 주세요.');
        socket.disconnect();
        return;
    }
    
    // 1. 호스트의 게임 시작 요청
    socket.on('start_game', () => {
        if (socket.id === hostSocketId && playerCount === 2 && !gameData.isBallAlive) {
            gameData.isBallAlive = true;
            gameData.ballX = CANVAS_SIZE / 2;
            gameData.ballY = CANVAS_SIZE / 2;
            gameData.dx = 4;
            gameData.dy = 4;
            
            io.emit('game_started'); 
            
            if (!gameInterval) {
                gameInterval = setInterval(gameLoop, 15);
            }
        }
    });

    // 2. 플레이어의 바 이동 (Host/Guest 모두 사용)
    socket.on('move_bar', (newBarX) => {
        if (socket.id === hostSocketId) {
            gameData.hostBarX = newBarX;
        } else if (socket.id === guestSocketId) {
            gameData.guestBarX = newBarX;
        }
    });

    // --- 연결 종료 ---
    socket.on('disconnect', () => {
        playerCount--;
        
        if (playerCount < 2 && gameInterval) {
             clearInterval(gameInterval);
             gameInterval = null;
             gameData.isBallAlive = false;
             io.emit('game_over', { winner: 'disconnect' });
        }

        // 역할 재설정 (여기서는 단순화하고, 재연결 시 재부여되도록 처리)
        if (socket.id === hostSocketId) {
            hostSocketId = null;
        } else if (socket.id === guestSocketId) {
            guestSocketId = null;
        }
    });
});


server.listen(PORT, () => {
    console.log(`서버가 http://localhost:${PORT} 에서 실행 중입니다.`);
});