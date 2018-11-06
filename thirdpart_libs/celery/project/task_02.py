# -*- coding: utf-8 -*-
from __future__ import absolute_import
from time import sleep

from celery.exceptions import SoftTimeLimitExceeded

from .celery import app


@app.task
def t(x, y):
    try:
        sleep(x)
        return y * 3
    except SoftTimeLimitExceeded:
        return y * 2
