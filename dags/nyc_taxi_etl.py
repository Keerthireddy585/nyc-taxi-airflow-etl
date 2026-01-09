from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import shutil
import pandas as pd
import sqlite3

BASE_DIR = "/opt/airflow"
DATA_DIR = f"{BASE_DIR}/data"

RAW_DIR = f"{DATA_DIR}/raw"
PROCESSED_DIR = f"{DATA_DIR}/processed"
DB_PATH = f"{DATA_DIR}/nyc_taxi.db"
DATA_URL = "/opt/airflow/dags/yellow_tripdata_2016-01.csv"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

RAW_FILE = f"{RAW_DIR}/nyc_taxi_raw.csv"
PROCESSED_FILE = f"{PROCESSED_DIR}/nyc_taxi_clean.csv"


def extract():
    shutil.copy(DATA_URL, RAW_FILE)
    print("Local file copied successfully to raw directory")


def transform():
    input_path = "/opt/airflow/dags/yellow_tripdata_2016-01.csv"
    output_path = "/opt/airflow/dags/cleaned_yellow_tripdata_2016-01.csv"

    if os.path.exists(output_path):
        os.remove(output_path)

    chunk_size = 50_000
    first_chunk = True

    for chunk in pd.read_csv(input_path, chunksize=chunk_size):
        chunk = chunk.dropna()

        chunk.to_csv(
            output_path,
            mode="a",
            header=first_chunk,
            index=False
        )

        first_chunk = False


def load():
    input_path = "/opt/airflow/dags/cleaned_yellow_tripdata_2016-01.csv"

    df = pd.read_csv(input_path, nrows=100_000)  
    print("Loaded rows:", len(df))


with DAG(
    dag_id="nyc_taxi_etl",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["ETL", "NYC_TAXI", "DATA_ENGINEERING"]
):

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load
    )

    extract_task >> transform_task >> load_task
