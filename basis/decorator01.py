# -*- coding: utf-8 -*-
import functools
import time

"""
*************** 装饰器 ************
在代码运行期间动态增加功能的方式, 称之为“装饰器”（Decorator）
主要用于加强函数功能,本质上装饰器是一个返回函数的高阶函数(参见 function03.py 了解高阶函数内容)
使用过程中引入 functools.wraps 用于解决 __name__ 指向问题

"""


def log_one(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("this is pre operation of {}".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


def log_two(cmd):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("this is pre operation of {}".format(func.__name__))
            print(cmd)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_one
def print_time01():
    print("the time is : ", time.strftime("%Y-%m-%d", time.localtime(time.time())))


@log_two("this is a test ...")
def print_time02():
    print("the time is : ", time.strftime("%y-%M-%D", time.localtime(time.time())))


if __name__ == "__main__":
    print_time01()
    print_time02()

