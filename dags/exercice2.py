from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(dag_id="exercice2",
         start_date=datetime(2021, 1, 1),
         schedule_interval='* * * * *',
         catchup=False) as dag:

    start = DummyOperator(task_id="start", dag=dag, trigger_rule='all_done')
    workflow = start

    task1 = BashOperator(
        task_id='loop_1',
        bash_command='echo 1',
    )

    task2 = BashOperator(
        task_id='loop_2',
        bash_command='echo 2',
    )

    task3 = BashOperator(
        task_id='loop_3',
        bash_command='echo {{task_instance_key_str}}',
    )

    for i in range(4, 10):
        task = BashOperator(
            task_id=f"loop{i}",
            bash_command='echo {{task_instance_key_str}}',
        )
        workflow >>= task

    end = DummyOperator(task_id="end", dag=dag, trigger_rule='all_done')
    workflow >>= end

    workflow
    