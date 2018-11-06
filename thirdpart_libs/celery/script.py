# -*- coding: utf-8 -*-
from celery import Celery

app = Celery("script",
             broker="redis://127.0.0.1:6379/1",
             backend="redis://127.0.0.1:6379/2")

app.conf.update(task_serializer="json",
                accept_content=["json"],
                result_serializer="json",
                timezone="Asia/Shanghai",
                enable_utc=True)


@app.task
def add(x, y):
    return x + y


@app.task
def sub(x, y):
    return x - y




