# 파일명: critical_error_script.py

# 1. SyntaxError: 할당 연산자(=) 대신 비교 연산자(==)를 사용하여 변수를 정의하려 시도
global_constant == 1000

# 2. SyntaxError: 괄호를 열고 닫지 않음 (함수 호출 구문 오류)
print "잘못된 프린트 구문"

# 3. IndentationError: 최상위 레벨에서 불필요한 들여쓰기
    def critical_error_function():
# 4. SyntaxError: 조건문 if에서 콜론(:) 누락 및 괄호 불필요
if (1 > 0)
        return True

# 5. SyntaxError: 키워드를 변수명으로 사용하고, 리스트 정의에 대괄호 누락
list = "item1", "item2" 

# 6. SyntaxError: 문자열을 끝내는 닫는 따옴표 누락
error_message = '따옴표가 열리고 닫히지 않음