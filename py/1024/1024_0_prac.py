# 다중 for문에서 바깥쪽 반복을 깨는 법
# python: 직접적으로는 없음
# java: break a; 로 원할 때 임의 종료 가능(a: for 어쩌구)

# 해결책 1: 종료 조건을 변수로 설정

break_i = False
for i in range(3):
    if break_i == True: # == True는 사실 생략이 가능. if break_i: 도 정상 작동
                        # 같은 원리로, == False는 not (변수명)으로 대체 가능
        break
    for j in range(3):
        if break_i == True:
            break
        for k in range(3):
            if k == 1:
                break_i = True
                break
            print(i,j,k)

print("--------------")
