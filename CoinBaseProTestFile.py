import cbpro
from datetime import datetime

c = cbpro.PublicClient()

coins = ['ETH-USD', 'ALGO-USD', 'ATOM-USD', 'GRT-USD',
         'BTC-USD', 'XTZ-USD', 'ACH-USD', 'POLY-USD']

# for i in coins:
# data = c.get_product_24hr_stats(i)
# coin = i
# vol = data.get("volume")
# high = data.get("high")
# low = data.get("low")
# print(f'Coin: {coin}\nVolume: {vol}\nHigh: {high}\nLow: {low}\n')


print("\n\n\n")
data8 = c.get_time()
print(data8.get("iso"), "\n\n")
now = datetime.now()
print(now)

# print("----------------")
# data1 = c.get_product_24hr_stats("ETH-USD")
# print(data1)
# print("---------------")
# data2 = c.get_product_ticker("ETH-USD")
# print(data2)
# print("---------------")
# data3 = c.get_product_order_book("ETH-USD")
# print(data3)
# print("---------------")
