from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

def fetch_crypto():
    os.system("python /scripts/fetch_crypto.py")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 2, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("crypto_pipeline", 
          default_args=default_args,
          schedule_interval="*/5 * * * *",
          catchup=False
          )

fetch_task = PythonOperator(
    task_id="fetch_crypto_task",
    python_callable=fetch_crypto,
    dag=dag,
)

fetch_task
