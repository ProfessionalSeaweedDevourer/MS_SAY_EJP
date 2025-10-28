from random import randint

# 상수 정의 (가독성 향상)
rsp = {1: "가위", 2: "바위", 3: "보"}

# 승패 결과 매핑 (0: 무승부, 1: 승리, 2: 패배)
RESULT_MAP = {
    0: "무승부",
    1: "승리",
    2: "패배"
}

def validate_input(prompt): # 사용자 입력의 유효성 검사
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in rsp:
                return user_input
            else:
                print("1, 2, 3 중 하나를 입력해 주세요.")
        except ValueError:
            print("잘못된 입력입니다. 1, 2, 3 중 하나를 입력해 주세요.")

def rspGame_Mod(player, computer): # 모듈러 연산을 활용한 승패 판정
    # 1. 입력값을 0, 1, 2로 변환 (1, 2, 3이 순환적 규칙에 맞도록)
    p = player - 1
    c = computer - 1
    
    # 2. 승패 판정 공식: (플레이어 - 컴퓨터 + 3) % 3
    # 결과: 0=무승부, 1=플레이어 승리, 2=플레이어 패배
    result = (p - c + 3) % 3
    
    return result

# --- 메인 게임 루프 ---

print("\n--- 가위바위보 게임: 모듈러 판본 ---")
print("내고 싶은 것을 결정하세요.")
print("1로 가위, 2로 바위, 3으로 보를 입력하세요.")

win_streak = 0

while True:
    cpu_input = randint(1, 3)
    
    # 입력값 검사
    user_input = validate_input("입력: ")
    
    print(f"컴퓨터: {rsp[cpu_input]}, 플레이어: {rsp[user_input]}")

    # 승패 판정
    result = rspGame_Mod(user_input, cpu_input)
    result_str = RESULT_MAP[result]
    
    if result == 0:
        print(f"{result_str}!")
        print("-" * 15)
    elif result == 1:
        win_streak += 1
        print(f"{result_str}! 현재 {win_streak}연승 중!")
        print("-" * 15)
    else: # result == 2 (패배)
        print(f"{result_str}! 최종 {win_streak}연승 기록.")
        
        # --- 재도전 로직 ---
        retry_choice = input("재도전하시겠습니까? (Y/N): ").strip().lower()
        
        if retry_choice == 'y':
            print("--- 재도전합니다! 연승 기록이 초기화됩니다. ---")
            win_streak = 0
            continue # 메인 루프 처음으로 돌아감
        else:
            print("게임을 종료합니다.")
            break # 메인 루프 종료