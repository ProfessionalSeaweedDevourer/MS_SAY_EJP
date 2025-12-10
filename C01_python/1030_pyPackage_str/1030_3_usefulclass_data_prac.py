# 입력받고 쪼개기
l = input("숫자(x,y,z,...): ")
split_l = l.split(",")
sum_l = 0
cnt = len(split_l)


# 입력값 검증 - for / if로 하느냐 try catch로 하느냐
for i in split_l:
    try:
        sum_l += int(i)
    except:
        cnt -= 1

avg_l = (sum_l) / cnt

print(sum_l, avg_l)

# Deprecated: 지원 종료 / 하여튼 이제는 안 쓰고, 쓰지 않는 것이 권장되는 기능.