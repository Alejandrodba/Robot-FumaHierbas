def ingesta(market,memory,interval):
    print('EXECUTING TRADING INGEST')
    print("MARKET: "+market)
    import requests
    import pandas as pd

    re = requests.get("https://api.binance.com/api/v3/exchangeInfo")
    print("REQUEST https: "+ str(re))
    data = re.json()
    symbols = data['symbols']

    symbol_list = []
    status_list = []

    for item in symbols:
        symbol_list.append(item['symbol'])
        status_list.append(item['status'])

    btc_symbol = filter(lambda x : market in x,symbol_list)
    btc_symbol_list = list(btc_symbol)



    for symbol_str in btc_symbol_list:
        
        print(f'---------------')
        print(f'Downloading {symbol_str} data')
        url = 'https://api.binance.com/api/v3/klines'
        headers = {'accept': 'application/json'}
        
        doc_columns = ['Open_Time', 'Open', 'High', 'Low', 'Close', 'Volume',
                    'Close_Time', 'Quote_asset_vol', 'Number_trades', 'Taker_buy_base',
                    'Taker_buy_quote','Ignore']     
        
        response = requests.get(url, headers=headers, params={"symbol": symbol_str, "interval":interval, "limit":"1"})
        data = response.json()
        print('Data requested')
        
        df = pd.DataFrame(data, columns = doc_columns)
        df['Open_Timestamp'] = pd.to_datetime(df['Open_Time'], unit='ms')
        df['Close_Timestamp'] = pd.to_datetime(df['Close_Time'], unit='ms')
        
                

    print("PRINT REQUEST")
    print(df)

    filename = market + '_' + interval + '.csv'

    
    from csv import writer
    try:
        with open(filename, 'r', newline='') as f_object:
            lines = f_object.readlines()
            f_object.close()
            
        if len(lines) > memory-1:
            del lines[0]
    except:
        lines = []



    with open(filename, 'w', newline='') as f_object:  
        for line in lines:
            f_object.write(line)
        
        writer_object = writer(f_object)
        if lines == []:
            writer_object.writerow(df.iloc[0].tolist())
            writer_object.writerow(df.iloc[0].tolist())
            writer_object.writerow(df.iloc[0].tolist())
            writer_object.writerow(df.iloc[0].tolist())
        
        writer_object.writerow(df.iloc[0].tolist())
        f_object.close()