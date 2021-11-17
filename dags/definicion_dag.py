"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

#Archivos python
from f_ingesta import ingesta
from f_posicion import posicion
from f_estrategia import estrategia

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 11, 15),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    #"retry_delay": timedelta(minutes=5),
    
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

with DAG('Estrategia-BANDUSDT', default_args = default_args, schedule_interval='*/1 * * * *', catchup=False, max_active_runs=1) as dag:
    market = 'BANDUSDT'
    memory = 10
    interval = "1m"
    cpt = 1
    t1 = PythonOperator(task_id = 'ejecuta-ingesta', python_callable = ingesta, op_args = [market, memory, interval])
    t2 = PythonOperator(task_id = 'ejecuta-estrategia', python_callable = estrategia, op_args = [market, memory, interval])
    t3 = PythonOperator(task_id = 'ejecuta-ordenes-posicion', python_callable = posicion, op_args = [market, memory, interval, cpt])
    
    t1 >> t2 >> t3