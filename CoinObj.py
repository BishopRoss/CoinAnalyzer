import cbpro

c = cbpro.PublicClient()


class Coin:

    def __init__(self, coinName):
        self.coinName = coinName
        self.data = c.get_product_24hr_stats(coinName)
        self.price = self.data.get("last")
        self.volume = self.data.get("volume")
        self.monthlyVolume = self.data.get("volume_30day")

    def getPrice(self):
        return self.price

    def getVolume(self):
        return self.volume

    def getMonthlyVolume(self):
        return self.monthlyVolume

    def getCoinName(self):
        return self.coinName


coin1 = Coin("ETH-USD")
print(coin1.getCoinName())
print(coin1.getVolume())
print(coin1.getMonthlyVolume())
print(coin1.getPrice())
