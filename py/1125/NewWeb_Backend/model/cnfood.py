from lib.ejpDBManager import ejpDBManager

class CNFood:

    def get(self):
        try:
            con, cur = ejpDBManager.makeConCur()
            sql = "SELECT * FROM nov25_cnFood"

    def reg(self, name, price):
        pass
