# # 실습 1: 임의의 '위치'의 피보나치 수열 값 구하기 (1,1,2,3,5,8,13...)
# def getfib(n):
#     if n <= 1:
#         return n
#     else:
#         return getfib(n-1) + getfib(n-2)
    
# # 그러나, 재귀 호출은 매우 비효율적인 '설계'임. 이해하기는 간단하지만, 알고리즘 복잡도가 높음.
# # 호출될 때마다, 새로 실행되는 함수를 위한 할당 공간 생성, 분기, 복귀가 수백억 회 발생.

# # 입력값 검증 및 결과 출력
# try:
#     n = int(input("1 이상의 자연수 하나를 입력하십시오.\n"))
    
#     if n <= 0:
#         print("오류: 1 이상의 자연수를 입력해야 합니다.")
#     else:
#         print(getfib(n))

# except ValueError:
#     print("오류: 유효한 정수를 입력하십시오.")
# except Exception as e:
#     print(f"알 수 없는 오류 발생: {e}")


# 모범 답안
def getfib_iterative(n):
    if n <= 1:
        return n
    
    # 0, 1, 2번째 피보나치 수열 값 초기화
    a, b = 0, 1 
    
    # n-1번 반복하여 n번째 값까지 계산
    for _ in range(2, n + 1):
        # 다음 피보나치 수는 a와 b의 합이고,
        # 새로운 a는 기존의 b가 되고, 새로운 b는 다음 피보나치 수가 됨
        a, b = b, a + b 
        
    return b

n = int(input("1 이상의 자연수 하나를 입력하십시오.\n"))
print(getfib_iterative(n))