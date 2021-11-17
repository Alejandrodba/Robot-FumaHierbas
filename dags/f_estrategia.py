from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def estrategia( market, memory, interval):
    import pandas as pd
        
    columns = ['Open_Time', 'Open', 'High', 'Low', 'Close', 'Volume',
                    'Close_Time', 'Quote_asset_vol', 'Number_trades', 'Taker_buy_base',
                    'Taker_buy_quote','Ignore','Open_Timestamp','Close_Timestamp']

    filename = market + '_' + interval + '.csv'
    print('00000000000')
    df = pd.read_csv(filename, sep=',', names=columns)
    print('00000000000')
    # Valores posibles de order: 1=compra, 0=mantener, -1=venta

    if df['Open'][4] >df['Open'][3] and df['Open'][4] >df['Open'][2]:
        order = 1
    elif df['Open'][4] <df['Open'][3] and df['Open'][4] <df['Open'][2]:
        order = -1
    else:
        order = 0
    print("ORDER = "+str(order))
    with open('order.txt', 'w', newline='') as f_object:  
        f_object.write(str(order))
        f_object.close()
    #ti.xcom_push(key='order', value=order)
    
    
