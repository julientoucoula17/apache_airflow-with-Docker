import logging
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

from tempfile import NamedTemporaryFile
from typing import TYPE_CHECKING, Dict, List, Optional, Sequence, Union

from airflow.exceptions import AirflowException
from airflow.models import BaseOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


# Change these to your identifiers, if needed.
AWS_S3_CONN_ID = "s3_conn"



def s3_extract():
   source_s3 = S3Hook(AWS_S3_CONN_ID)
   paths = source_s3.list_keys(bucket_name='lead-m3-d2')
   print(paths)

   	 
with DAG(
	dag_id="s3_extract",
	start_date=datetime(2022, 2, 12),
	schedule_interval=timedelta(days=1),
	catchup=False,
) as dag:

  t1 = PythonOperator(
    	task_id="s3_extract_task",
    	python_callable=s3_extract)
   	 
  t1


  #COPY dev.public.part FROM 's3://tutorial-loading-data-upload-files/part-csv.tbl-000' IAM_ROLE 'arn:aws:iam::962771681951:role/RedshiftFromQuickSights' FORMAT AS CSV DELIMITER ',' QUOTE '"' REGION AS 'us-east-1'