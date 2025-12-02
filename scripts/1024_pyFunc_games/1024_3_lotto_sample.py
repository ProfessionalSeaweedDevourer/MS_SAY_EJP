from random import randint

def pick(i, lotto):
    l = randint(1, 45)
    for j in range(i):
        if l == lotto[j]:
            return pick(i, lotto)
    return l

lotto = []
for i in range(6):
    l = pick(i, lotto)
    lotto.append(l)

print(lotto)