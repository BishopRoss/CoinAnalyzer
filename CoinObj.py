import cbpro
import mysql.connector
from datetime import datetime

c = cbpro.PublicClient()


class Coin:

    def __init__(self, coinName):
        self.coinName = coinName
        self.data = c.get_product_24hr_stats(coinName)
        self.price = self.data.get("last")
        self.volume = self.data.get("volume")
        self.monthlyVolume = self.data.get("volume_30day")
        self.openPrice = self.data.get("open")
        self.highPrice = self.data.get("high")
        self.lowPrice = self.data.get("low")

    def getOpeningPrice(self):
        return self.openPrice

    def get24HourHigh(self):
        return self.highPrice

    def get24HourLow(self):
        return self.lowPrice

    def getPrice(self):
        return self.price

    def getVolume(self):
        return self.volume

    def getMonthlyVolume(self):
        return self.monthlyVolume

    def getCoinName(self):
        return self.coinName


class DatabaseInserter(Coin):

    def __init__(self, coinName, databaseName, host, tableName):
        Coin.__init__(self, coinName)
        self.databaseName = databaseName
        self.host = host
        self.databaseUser = "root"
        self.databasePassword = "BishopRoss"
        self.tableName = tableName

    def insertInformation(self):
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.databaseUser,
            password=self.databasePassword,
            database=self.databaseName
        )
        cursor = mydb.cursor()
        price = float(self.price)
        volume = float(self.volume)
        monthlyVolume = float(self.monthlyVolume)
        openPrice = float(self.openPrice)
        highPrice = float(self.highPrice)
        lowPrice = float(self.lowPrice)
        tableName = self.tableName
        # sql = "INSERT INTO ethereum2 (PRICE,TOTAL_VOLUME,30_DAY_VOLUME) VALUES (%s,%s,%s)"
        time = datetime.now()
        sql = f"INSERT INTO {tableName} (PRICE,TOTAL_VOLUME,30_DAY_VOLUME, OPENING_PRICE, 24_HOUR_HIGH, 24_HOUR_LOW, " \
              "TIME) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s) "
        val = (price, volume, monthlyVolume, openPrice, highPrice, lowPrice, time)

        cursor.execute(sql, val)
        mydb.commit()

    def coinName(self):
        return self.coinName

    def changeDataBase(self, databaseName):
        self.databaseName = databaseName

    def setPassword(self, passwrd):
        self.databasePassword = passwrd

    def setUser(self, user):
        self.databaseUser = user


# test1 = DatabaseInserter("ETH-USD", "test", "localhost", "ethereum3")

# print("Coin Name: " + test1.getCoinName())
# print("24 Hour Volume: " + test1.getVolume())
# print("30 Day Volume: " + test1.getMonthlyVolume())
# print("Last Trading Price: " + test1.getPrice())
# print("Opening Price: " + test1.getOpeningPrice())
# print("24 Hour High Price: " + test1.get24HourHigh())
# print("24 Hour Low Price: " + test1.get24HourLow())
# test1.insertInformation()
