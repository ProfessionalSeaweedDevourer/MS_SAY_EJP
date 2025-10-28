# 리스트의 정렬

l1 = [213, 765, 21, 1786, 2, 1]

# l = sorted(l)
# print(l)

# 실습: 버블 정렬

def bubble(l):
    temp = 0
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j]>l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

bubble(l1)
print(l1)

l2 = [3, 123, 984, 1, 24, 750, 1230, 500]

# 실습: 선택 정렬

def sel(l):
    for i in range(len(l)-1):
        min = i
        for j in range(i+1, len(l)): # 시작 위치의 다음 위치 내에서... > 예를 들어, i = 2일 때 (3, 7)
            if l[j] < l[min]: # 각 원소가 (시작 위치부터) 다른 원소보다 상대적으로 작으면 > l[0] < l[i]
                l[j], l[min] = l[min], l[j] # 그 원소를 맨 앞으로 보냄
    return l

sel(l2)
print(l2)