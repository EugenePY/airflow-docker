# -*- coding: utf-8 -*-
#
#     Copyright 2019 Hunter Senft-Grupp
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from datetime import datetime, timedelta
import json
from airflow import DAG

from airflow_docker.operator import Operator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 10, 10),
    'retries': 2,
    'retry_delay': timedelta(seconds=30),
}

dag = DAG(
    'use-context',
    default_args=default_args,
    catchup=False,
    schedule_interval=None,
    concurrency=2,
)

with dag:
    use_context = Operator(
        task_id='use-context',
        image='airflowdocker/example-tasks:latest',
        provide_context=True,
        command=json.dumps([
            'use-context.py',
        ]),
    )
