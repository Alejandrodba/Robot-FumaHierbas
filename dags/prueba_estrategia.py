import pandas as pd

market = 'BANDUSDT'
memory = 5
interval = "1m"

columns = ['Open_Time', 'Open', 'High', 'Low', 'Close', 'Volume',
                'Close_Time', 'Quote_asset_vol', 'Number_trades', 'Taker_buy_base',
                'Taker_buy_quote','Ignore','Open_Timestamp','Close_Timestamp']

filename = market + '_' + interval + '.csv'
df = pd.read_csv(filename, sep=',', names=columns)

# Valores posibles de order: 1=compra, 0=mantener, -1=venta
print( df['Open'][4])
print( df['Open'][3])
print( df['Open'][2])


if df['Open'][4] >df['Open'][3] and df['Open'][4] >df['Open'][2]:
    order = 1
elif df['Open'][4] <df['Open'][3] and df['Open'][4] <df['Open'][2]:
    order = -1
else:
    order = 0
print(order)