'''
=================================================
Milestone 3

Nama  : Muhammad Rofi Senoaji
Batch : FTDS-HCK-008

Program ini dibuat untuk melakukan otomasi dari load data dari postgres, data cleaning dan post ke elastic search
Dataset yang digunakan merupakan data insiden birdstrikes di Amerika Serikat dari tahun 1999 hingga 2009
=================================================
'''

# Import Library
import datetime as dt
from datetime import datetime, timedelta
from airflow import DAG
from elasticsearch import Elasticsearch
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator 
import pandas as pd
import psycopg2 as db

# Fungsi untuk mengambil data dari postgress

'''
Fungsi ini bertujuan untuk mengambil data dari PostgreSQL dan menyimpannya dalam file CSV.

Parameters:
  Tidak ada parameter yang diterima oleh fungsi ini.

Return:
  Tidak ada nilai yang dikembalikan oleh fungsi ini.

Contoh penggunaan:
  get_data_from_db()
'''

def get_data_from_db():
    conn_string = "dbname='postgres' host='localhost' user='airflow' password='airflow'"
    conn = db.connect(conn_string)
    df = pd.read_sql("select * from table_m3", conn)
    df.to_csv('/opt/airflow/dags/P2M3_muhammad_rofi_data_raw.csv', index=False)

def data_pipeline():
    
'''
Fungsi ini digunakan untuk memuat data dari file CSV yang dihasilkan oleh fungsi `get_data_from_db()`, melakukan pembersihan data dengan menghapus beberapa kolom dan baris yang memiliki nilai kosong, dan kemudian menyimpan data bersih ke file CSV.

Parameters:
  Tidak ada parameter yang diterima oleh fungsi ini.

Return:
  Tidak ada nilai yang dikembalikan oleh fungsi ini.

Contoh penggunaan:
  data_pipeline()
'''

    # Loading CSV ke dataframe
    df_data = pd.read_csv('/opt/airflow/dags/P2M3_muhammad_rofi_data_raw.csv')

    # Data Cleaning
    df_data = df_data.drop(['remarks', 'conditions_precipitation', 'effect_impact_to_flight'], axis=1, inplace=True)
    df_data = df_data.dropna()
    df_data.to_csv('/opt/airflow/dags/P2M3_muhammad_rofi_data_clean.csv', index=False)

# Fungsi untuk ngepost ke kibana

'''
Fungsi ini bertujuan untuk memposting data yang telah dibersihkan ke Kibana, menggunakan Elasticsearch.

Parameters:
  Tidak ada parameter yang diterima oleh fungsi ini.

Return:
  Tidak ada nilai yang dikembalikan oleh fungsi ini.

Contoh penggunaan:
  post_to_kibana()
'''

def post_to_kibana():
    es = Elasticsearch("http://elasticsearch:9200")
    df = pd.read_csv('/opt/airflow/dags/P2M3_muhammad_rofi_data_clean.csv')

    for i, r in df.iterrows():
        doc = r.to_json()
        res = es.index(index="table_m3", id=i + 1, body=doc)

# Setup DAG
default_args = {
    'owner': 'aji',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=60),
}

with DAG('Milestone3',
         description='milestone_test',
         default_args=default_args,
         schedule_interval='@daily', 
         start_date=dt.datetime(2023, 10, 30, 13, 30, 0) - timedelta(hours=7),
         catchup=False) as dag:

    # Jalankan fungsi untuk mengambil data dari SQL
    fetch_task = PythonOperator(
        task_id='get_data_from_db',
        python_callable=get_data_from_db
    )

    # Jalankan fungsi cleaning data dengan PhytonOperator
    clean_task = PythonOperator(
        task_id='cleaning_data',
        python_callable=data_pipeline
    )

    # Jalankan fungsi untuk ngepost ke kibana
    post_to_kibana_task = PythonOperator(
        task_id='post_to_kibana',
        python_callable=post_to_kibana
    )

    # Tentukan alur
    fetch_task >> clean_task >> post_to_kibana_task