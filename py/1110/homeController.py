from companyDAO import CompanyDAO
from consoleScreen import ConsoleScreen

if __name__ == "__main__":
    c = ConsoleScreen.getInfo()
    result = CompanyDAO.reg(c)
    ConsoleScreen.printResult(result)