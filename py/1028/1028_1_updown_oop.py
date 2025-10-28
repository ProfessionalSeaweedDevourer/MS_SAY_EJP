from random import randint

# 1. 게임 범위 입력과 검증 로직 (클래스 외부 함수)
def get_game_range():
    print("--- 게임 범위 설정 ---")
    while True:
        try:
            start = int(input("시작 범위 (예: 1): "))
            end = int(input("끝 범위 (예: 10000): "))
            
            if start >= end:
                print("오류: 끝 범위가 시작 범위보다 커야 합니다. 다시 입력해 주십시오.")
                continue
            
            # 입력값의 유효성 검사를 통과하면 범위 반환
            return start, end
        except ValueError:
            print("오류: 유효한 정수를 입력해 주십시오.")

# 2. 클래스화된 게임 메인 로직
class GuessingGame:
    def __init__(self, start, end):
        self.range_start = start
        self.range_end = end
        
        # 전달받은 범위 내에서 무작위 정수 선출
        self.answer = randint(self.range_start, self.range_end)
        self.guess_count = 0
        
        # 디버그용 출력 제거
        # print(f"디버그용 정답: {self.answer}")

    def get_guess(self):
        while True:
            try:
                prompt = f"{self.range_start} - {self.range_end} 사이 정수 입력: "
                guess = int(input(prompt))
                
                # 입력값이 범위 내에 있는지 추가 검사
                if self.range_start <= guess <= self.range_end:
                    return guess
                else:
                    print(f"오류: 입력은 {self.range_start}와 {self.range_end} 사이여야 합니다.")
            except ValueError:
                print("유효한 정수를 입력해 주십시오.")

    def check_guess(self, guess):
        self.guess_count += 1
        
        if guess == self.answer:
            return True  # 정답
        else:
            hint = "UP" if guess < self.answer else "DOWN"
            print(hint)
            print("--------")
            return False # 오답

    def start(self):
        """게임의 전체 흐름을 제어합니다."""
        print(f"\n--- 숫자 맞히기 게임 시작 ({self.range_start} ~ {self.range_end}) ---")
        
        is_correct = False
        while not is_correct:
            user_guess = self.get_guess()
            is_correct = self.check_guess(user_guess)
        
        # 루프 탈출 후 정답 처리 및 종료
        print(f"\n!!! 정답 !!!")
        print(f"축하합니다! {self.guess_count}회 만에 정답을 맞췄습니다.")

# 3. 메인 실행 블록
if __name__ == "__main__":
    
    # 게임 시작 전, 사용자가 범위를 결정
    start_range, end_range = get_game_range() 
    
    # 결정된 범위로 GuessingGame 객체 생성
    game = GuessingGame(start_range, end_range) 
    
    # 게임 시작
    game.start()