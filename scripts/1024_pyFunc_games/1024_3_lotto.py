# 1 - 45 사이 무작위 자연수 6개로 나열된 로또 번호를 생성
# 단, 각 원소는 중복이 있으면 안 됨
#   > 하나 생성하고, 전 번호랑 같은지 검증해서 아니면 다시 돌리고
#   > 또는 이 번호들이 있는 것을 set으로 하면, 중복 원소는 애초에 안 들어가나?

from random import randint

minNum = 1
maxNum = 45

def genLotto():
    lottoSet = set() 
    while len(lottoSet) < 6:
        new_number = randint(minNum, maxNum)
        lottoSet.add(new_number)

        # 디버그 출력
        print(f"생성된 숫자: {new_number}, 현재 집합: {lottoSet}") 

    return lottoSet

# 실행
result = genLotto()
print(f"{result}")

