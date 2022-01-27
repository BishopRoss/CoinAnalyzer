import cbpro

c = cbpro.PublicClient()

coins = ['ETH-USD', 'ALGO-USD', 'ATOM-USD', 'GRT-USD',
         'BTC-USD', 'XTZ-USD', 'ACH-USD', 'POLY-USD']

for i in coins:
    data = c.get_product_24hr_stats(i)
    coin = i
    vol = data.get("volume")
    high = data.get("high")
    low = data.get("low")
    print(f'Coin: {coin}\nVolume: {vol}\nHigh: {high}\nLow: {low}\n')


