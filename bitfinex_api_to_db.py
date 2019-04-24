import mongoengine
import requests

apiurl = 'https://api.bitfinex.com/v2'
pair = 'BTCUSD'
timeframe = '1h'

# API URL example: 'https://api.bitfinex.com/v2/candles/trade:1h:tBTCUSD/hist"
candle_data = apiurl + '/candles/trade:' + timeframe + ':t' + pair + '/hist'

r = requests.get(candle_data)

data = r.json()
print(data)

for record in data:
    c_mts = record[0]
    c_open = record[1]
    c_close = record[2]
    c_high = record[3]
    c_low = record[4]
    c_volume = record[5]

    print(c_mts, c_open, c_close, c_high, c_low, c_volume)

    db = mongoengine.connect('bitfinex.candles_1h', host='localhost', port=27017)
    db.bitfinex.candles_1h.insert_one(
        dict(mts=c_mts, open=c_open, close=c_close, high=c_high, low=c_low, volume=c_volume))
