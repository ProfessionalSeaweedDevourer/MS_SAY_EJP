from random import randint
 
 
class Referee:
    def __init__(self):
        self.ruleBook = [None, "가위", "바위", "보"]
 
    def blueFire(self, blue):
        return blue.fire()
 
    def callBlueCorner(self):
        return Friend()
 
    def callRedCorner(self):
        return Player()
 
    def judge(self, bluePaper, redPaper):
        t = redPaper - bluePaper
        if t == 0:
            print("무")
            return 0
        elif t == -1 or t == 2:
            print("패")
            return -999
        else:
            print("승")
            return 1
 
    def redFire(self, red):
        redTemp = red.fire()
        if 0 < redTemp < 4:
            return redTemp
        return self.redFire(red)
 
    def tellHand(self, bluePaper, redPaper):
        print("컴 : %s" % self.ruleBook[bluePaper])
        print("나 : %s" % self.ruleBook[redPaper])
 
    def tellResult(self, win):
        print("%d연승" % win)
 
    def tellRule(self):
        for i, v in enumerate(self.ruleBook):
            if i != 0:
                print("%d) %s" % (i, v))
        print("-----")
 
    def start(self):
        blue = self.callBlueCorner()
        red = self.callRedCorner()
        self.tellRule()
        win = 0
        while True:
            bluePaper = self.blueFire(blue)
            redPaper = self.redFire(red)
            self.tellHand(bluePaper, redPaper)
            t = self.judge(bluePaper, redPaper)
            if t == -999:
                break
            win += t
            print("-----")
        self.tellResult(win)
 
 
class Friend:
    def fire(self):
        return randint(1, 3)
 
 
class Player:
    def fire(self):
        return int(input("뭐 : "))
 
 
#################
r = Referee()
r.start()