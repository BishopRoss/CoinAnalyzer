import mysql
import CoinObj


class DatabaseInserter(CoinObj):

    def __init__(self, databaseName, host):
        CoinObj.__init__(self)
        self.databaseName = databaseName
        self.host = host
        self.databaseUser = "null"
        self.databasePassword = "null"


    def login(self):
        return 0

    def insertPrice(self):
        return 0

    def insertTotalVolume(self):
        return 0

    def insertBuyVolume(self):
        return 0

    def coinName(self):
        return 0

    def changeDataBase(self, databaseName):
        self.databaseName = databaseName

    def setPassword(self, passwrd):
        self.databasePassword = passwrd

    def setUser(self, user):
        self.databaseUser = user


coin1 = CoinObj("ETH-USD")

