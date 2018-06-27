# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import Celery

app = Celery("project",
             broker="redis://127.0.0.1:6379/1",
             backend="redis://127.0.0.1:6379/2",
             include=["project.task_01", "project.task_02"])

app.config_from_object("project.config")


if __name__ == "__main__":
    app.start()
