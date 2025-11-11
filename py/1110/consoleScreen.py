from company import Company

class ConsoleScreen:
    def getInfo():
        name = input("회사명: ")
        addr = input("주소: ")
        ceo = input("사장: ")
        emp = input("직원 수: ")
        return Company(name, addr, ceo, emp)
    
    def printResult(result):
        print(result)