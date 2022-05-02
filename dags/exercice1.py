from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(dag_id="exercice1",
    start_date=datetime(2021, 1, 1),
    schedule_interval='* * * * *',
    catchup=False) as dag:

    task1 = BashOperator(
    task_id='loop1',
    bash_command='echo 1')
    
    task2 = BashOperator(
    task_id='loop2',
    bash_command='echo 2')

    task3 = BashOperator(
    task_id='loop_3',
    bash_command='echo {{task_instance_key_str}}')

task1 >> task2 >> task3