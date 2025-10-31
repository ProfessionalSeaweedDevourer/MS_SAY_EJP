f = open("c:/snack.csv", "a", encoding = "utf-8")

class Snack:

    def __init__(self, line):
        line = line.replace("\n", "")
        line = line.split(",")
        self.name = line[0]
        self.price = int(line[1])
        self.weight = float(line[2])

for line in f.readlines():
    s = Snack(line)        

# 가격에 따른 정렬과 출력

snacks.sor(key=lambda s: s.price, reverse=True)
snacks[0].printInfo()

# g당 가격 계산 및 정렬 후 출력

snacks.sort(key=lambda s: s.price / s.weight)
snacks[0].printInfo()

f.close()