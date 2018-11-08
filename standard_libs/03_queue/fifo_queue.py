# -*- coding: utf-8 -*- 

"""
code: by shylune
time: 2018-11-08
note: 先进先出队列
"""
from queue import Queue


def test():
    queue = Queue()
    for x in range(5):
        queue.put(x)

    while not queue.empty():
        print(queue.get())


if __name__ == "__main__":
    test()
