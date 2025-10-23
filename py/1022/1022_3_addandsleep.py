from time import sleep

# 실습 3: 수 2개를 입력받아 그 합을 구하고, 그만큼 쉬었다가 결과를 반환하는 함수

def AddandSleep(a,b):
    sleep(a+b)
    return(a+b) # return 값: 함수의 '결과'를 반환하면서, 함수가 끝남. return 이후에 뭔가를 써 놔도 실행되는 일은 없음.

a=int(input("임의의 수를 입력하세요. "))
b=int(input("임의의 수를 하나 더 입력하세요. "))
print(AddandSleep(a,b))