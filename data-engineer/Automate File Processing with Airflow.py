# Automate File Processing with Airflow
# This script demonstrates a simple Airflow DAG to automate an ETL pipeline.

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

# Define ETL functions
def extract():
    df = pd.read_csv('source_data.csv')
    return df

def transform(df):
    df['new_column'] = df['old_column'] * 2
    return df

def load(df):
    df.to_csv('transformed_data.csv', index=False)

# Define DAG
dag = DAG('etl_pipeline', description='Simple ETL Pipeline', schedule_interval='@daily', start_date=datetime(2023, 10, 1))

# Define tasks
extract_task = PythonOperator(task_id='extract', python_callable=extract, dag=dag)
transform_task = PythonOperator(task_id='transform', python_callable=transform, op_args=[extract_task.output], dag=dag)
load_task = PythonOperator(task_id='load', python_callable=load, op_args=[transform_task.output], dag=dag)

# Set task dependencies
extract_task >> transform_task >> load_task