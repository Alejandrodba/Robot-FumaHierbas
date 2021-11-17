def posicion(market, memory, interval, cpt):
    import pandas as pd
    with open('order.txt', 'r', newline='') as f_object:  
        lines = f_object.readlines()
        order = int(lines[0])
        f_object.close()
    print(order)

    try:
        with open(f'wallet_{market}_{interval}_{memory}', 'r', newline='') as f_object:  
            lines = f_object.readlines()
            wallet = lines[0].split(',')
            cash = int(wallet[0])
            crypto_cash = int(wallet[1])
            f_object.close()
    except:
        with open(f'wallet_{market}_{interval}_{memory}', 'w', newline='') as f_object:  
            f_object.write('100,0,1') #Initial cash, Initial crypto_cash, Cash per trade
            f_object.close()
        cash = 100
        crypto_cash = 0
    
    columns = ['Open_Time', 'Open', 'High', 'Low', 'Close', 'Volume',
                    'Close_Time', 'Quote_asset_vol', 'Number_trades', 'Taker_buy_base',
                    'Taker_buy_quote','Ignore','Open_Timestamp','Close_Timestamp']
    filename = market + '_' + interval + '.csv'
    df = pd.read_csv(filename, sep=',', names=columns)
    trade_price = df['Close'][4]
            
    if order == 1:
        if cash > 0:
            cash -= cpt
            crypto_cash += cpt/trade_price
            acc_balance = cash + crypto_cash*trade_price
    
    elif order == -1:
        if crypto_cash > 0:
            cash += cpt
            crypto_cash -= cpt/trade_price
            acc_balance = cash + crypto_cash*trade_price
    
    elif order == 0:
        
        acc_balance = cash + crypto_cash*trade_price
    print(f'trade_price: {trade_price}')
    print(f'cash: {cash}')
    print(f'crypto_cash: {crypto_cash}')   
    print(f'acc_balance: {acc_balance}')
    print(df['Close_Timestamp'][4])
    
    from csv import writer
    try:
        with open('historial.csv', 'r', newline='') as f_object:  
            f_object.close()
        
        with open('historial.csv', 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            writer_object.writerow([cash, crypto_cash, acc_balance, df['Close_Timestamp'][4]])
            f_object.close()
            
    except:
        with open(f'historial_{market}_{interval}_{memory}.csv', 'w', newline='') as f_object:  
            f_object.close()