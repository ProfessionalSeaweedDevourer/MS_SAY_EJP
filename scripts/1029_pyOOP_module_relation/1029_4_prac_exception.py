class Calculate:
    def __init__(self, x, y):
        # __init__에서는 받은 값(이미 float으로 검증된 값)을 저장합니다.
        self.x = x
        self.y = y

    def run(self):
        # 사칙연산을 수행하고 결과를 튜플로 반환합니다.
        try:
            addition = self.x + self.y
            subtraction = self.x - self.y
            multiplication = self.x * self.y
            # 여기까지는 오류의 여지가 없음
            
            # y가 0이면 ZeroDivisionError 발생 가능
            division = self.x / self.y 
            
            return (addition, subtraction, multiplication, division)
        
        # Java에서는 catch를 대신 쓴다.

        except ZeroDivisionError:
            # 나눗셈이 불가능할 경우, 해당 위치에 메시지를 반환합니다.
            print("오류: 0으로 나눌 수 없습니다.")
            # 다른 연산 결과는 정상적으로 반환하고, 나눗셈 결과만 오류 메시지로 대체합니다.
            return (self.x + self.y, self.x - self.y, self.x * self.y, "-")

# try - except로 각종 예외를 미리 기술하고, 이도 저도 아닌 경우는 else, 최종적으로는 finally 부분이 (항상) 실행된다.

def inputValidator(x_str, y_str):
    """
    입력된 문자열 x, y가 유효한 숫자인지 검증하고 float으로 변환하여 반환합니다.
    유효하지 않으면 예외 처리 후 None을 반환합니다.
    """
    try:
        # 입력값을 float으로 변환 시도 (숫자가 아니면 ValueError 발생)
        x = float(x_str)
        y = float(y_str)
        return x, y
        
    except ValueError:
        print("오류: 입력된 x 또는 y 값이 유효한 숫자가 아닙니다.")
        return None, None # 유효하지 않으면 None 반환

if __name__ == "__main__":
    # 사용자로부터 문자열 입력 받음
    x_input = input("x: ")
    y_input = input("y: ")

    # 입력값 검증 및 변환
    x, y = inputValidator(x_input, y_input)

    # x, y가 모두 None이 아니어야 정상적으로 Calculate 인스턴스 생성 및 run 실행
    if x is not None and y is not None:
        calcxy = Calculate(x, y)
        result = calcxy.run()
        print(f"연산 결과 (합, 차, 곱, 나눗셈): {result}")
    else:
        print("유효하지 않은 입력으로 인해 계산을 수행할 수 없습니다.")