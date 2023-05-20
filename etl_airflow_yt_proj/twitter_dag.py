from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime

from twitter_etl import run_twitter_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['vivek221b@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_DAG',
    default_args=default_args,
    description="ETL project using Airflow"
)

run_etl = PythonOperator(
    task_id = 'Complete_twitter_ETL',
    python_callable=run_twitter_etl,
    dag = dag
)

run_etl