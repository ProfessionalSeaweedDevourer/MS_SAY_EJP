from random import randint

# 유틸리티 클래스 (생략)
class InputValidator:
    @staticmethod
    def get_input(prompt, valid_options):
        while True:
            try:
                user_input = int(input(prompt))
                if user_input in valid_options:
                    return user_input
                else:
                    print("유효한 입력값(1, 2, 3)을 입력해 주세요.")
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해 주세요.")

# CPU 플레이어의 행동을 책임지는 클래스 (생략)
class CPUPlayer:
    @staticmethod
    def choose_hand(options):
        return randint(min(options), max(options))

# 승패 판정(심판)을 책임지는 클래스 (생략)
class RspJudge:
    RESULT_MAP = {
        0: "무승부",
        1: "승리",
        2: "패배"
    }

    @staticmethod
    def judge(player_hand, cpu_hand):
        p = player_hand - 1
        c = cpu_hand - 1
        return (p - c + 3) % 3

# 게임의 흐름과 상태 관리를 책임지는 클래스
class RspGame:
    RSP_OPTIONS = {1: "가위", 2: "바위", 3: "보"}

    def __init__(self, cpu_player, judge):
        self.cpu_player = cpu_player
        self.judge = judge
        self.reset_game()

    def __str__(self):
        return f"가위바위보 게임 상태: 현재 {self.win_streak}연승 중입니다."

    def reset_game(self):
        self.win_streak = 0

    @classmethod 
    def display_rules(cls):
        print("\n" + "=" * 50)
        print("--- 가위바위보 게임을 시작합니다 ---")
        print("내고 싶은 것을 결정하세요.")
        print(f"1로 {cls.RSP_OPTIONS[1]}, 2로 {cls.RSP_OPTIONS[2]}, 3으로 {cls.RSP_OPTIONS[3]}를 입력하세요.")
        print("=" * 50)

    # fight 메서드의 반환값을 승패 코드(0, 1, 2)로 변경!
    def fight(self, user_input):
        cpu_input = self.cpu_player.choose_hand(self.RSP_OPTIONS)
        
        print(f"컴퓨터: {self.RSP_OPTIONS[cpu_input]}, 플레이어: {self.RSP_OPTIONS[user_input]}")

        # 심판에게 판정 위임
        result_code = self.judge.judge(user_input, cpu_input)
        result_str = self.judge.get_result_string(result_code)

        if result_code == 0:
            print(f"{result_str}!")
            print("-" * 15)
        elif result_code == 1:
            self.win_streak += 1
            print(f"{result_str}! 현재 {self.win_streak}연승 중!")
            print("-" * 15)
        else: # result_code == 2 (패배)
            print(f"{result_str}! 최종 {self.win_streak}연승 기록.")
            
        return result_code # 승패 코드(0, 1, 2)를 반환

    def should_continue(self):
        retry_choice = input("재도전하시겠습니까? (Y/N): ").strip().lower()
        
        if retry_choice == 'y':
            print("--- 재도전합니다! ---")
            return True
        else:
            print("게임을 종료합니다.")
            return False

if __name__ == "__main__":
    
    RspGame.display_rules()
    
    cpu = CPUPlayer()
    judge = RspJudge()
    game = RspGame(cpu_player=cpu, judge=judge)
    
    while True:
        user_choice = InputValidator.get_input("입력: ", RspGame.RSP_OPTIONS) 
        
        # 라운드 실행 후, 결과를 result_code로 받음 (직관적 개선!)
        result_code = game.fight(user_choice)
        
        # 패배 코드(2)를 명시적으로 비교하여 처리
        if result_code == 2:
            if game.should_continue():
                game.reset_game() 
                RspGame.display_rules()
            else:
                break