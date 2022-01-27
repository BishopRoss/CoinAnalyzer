import mysql.connector


class DatabaseLogin:

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "BishopRoss"
        self.database = "test"

    def setHost(self, host):
        self.host = host

    def __setUsername(self, user):
        self.user = user

    def __setPassword(self, password):
        self.password = password

    def setDatabase(self, database):
        self.database = database


class MyCursor:
    def __init__(self):
        DatabaseLogin.__init__(self)
        self.mydb = mysql.connector.connect(
            host= MyCursor.host,
            user=MyCursor.user,
            password=MyCursor.password,
            database=MyCursor.database
        )

    def createCursor(self):
        pass
# login = DatabaseLogin()
login = MyCursor().mydb


mydb = mysql.connector.connect(
    host=login.host,
    user=login.user,
    password=login.password,
    database=login.database
)

mycursor = mydb.cursor()

# mycursor = mycursor.execute("CREATE DATABASE test") mycursor.execute("CREATE TABLE ETHEREUM (COIN_ID VARCHAR (30),
# TOTAL_VOLUME DOUBLE PRECISION, PRICE DOUBLE PRECISION, BUY_VOLUME DOUBLE PRECISION, SELL_VOLUME DOUBLE PRECISION,
# MARKET_CAP DOUBLE PRECISION)")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
