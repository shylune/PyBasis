# -*- coding: utf-8 -*- 

"""
code: by shylune
time: 2018-11-08
note: 后进先出队列
"""
from queue import LifoQueue


def test():
    queue = LifoQueue()
    for x in range(5):
        queue.put(x)

    while not queue.empty():
        print(queue.get())


if __name__ == "__main__":
    test()
