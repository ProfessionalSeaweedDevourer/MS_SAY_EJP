async function BMIvalidate(event) {
    
    event.preventDefault();
    
    const nameInput = document.getElementById('nameInput');
    const heightInput = document.getElementById('heightInput');
    const weightInput = document.getElementById('weightInput');
    const photoInput = document.getElementById('photoInput');

    // 1. Generalvalidate.js 활용한 유효성 검증 (이름, 키, 몸무게)
    if (isEmpty(nameInput) || isEmpty(heightInput) || isEmpty(weightInput)) {
        alert("이름, 키, 몸무게를 모두 입력해 주십시오.");
        return false;
    }
    
    // 2. 숫자 및 양수 검증 (isNotNum 확장 활용)
    if (isNotNum(heightInput) || isNotNum(weightInput)) {
        alert("키와 몸무게는 올바른 양수 값이어야 합니다.");
        return false;
    }
    
    // 3. 사진 파일 필수 확인 로직 (Generalvalidate.js에서 처리 불가)
    if (!photoInput.files || photoInput.files.length === 0) {
        alert("사진 파일을 반드시 업로드해 주십시오.");
        return false;
    }

    // 4. 값 추출 및 계산
    const name = nameInput.value.trim();
    const height = parseFloat(heightInput.value);
    const weight = parseFloat(weightInput.value);

    const calculationResult = calculateBMI(height, weight);
    
    // 5. FormData 객체 생성 및 데이터 추가
    const formData = new FormData();
    formData.append('name', name);
    formData.append('height', height);
    formData.append('weight', weight);
    
    formData.append('stdWeight', calculationResult.stdWeight);
    formData.append('bmi', calculationResult.bmi);
    formData.append('judgment', calculationResult.judgment); 

    const photoFile = photoInput.files[0];
    if (photoFile) {
        formData.append('photo', photoFile);
    }
    
    // 6. FastAPI 서버로 비동기 POST 요청
    try {
        const response = await fetch('http://127.0.0.1:8000/calculate-and-upload', {
            method: 'POST',
            body: formData 
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json(); 
        
        const params = new URLSearchParams();
        params.append('name', result.name);
        params.append('weight', result.weight);
        params.append('stdWeight', result.stdWeight);
        params.append('bmi', result.bmi);
        params.append('judgment', result.judgment);
        params.append('photo_path', result.photo_path);
        
        window.location.href = `Output.html?${params.toString()}`;

    } catch (error) {
        console.error('데이터 전송 및 처리에 오류가 발생했습니다:', error);
        alert('데이터 전송 중 서버 연결 오류가 발생했습니다. (FastAPI 서버 실행 및 CORS 설정 확인)');
    }
    
    return false;
}