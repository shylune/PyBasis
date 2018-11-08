# -*- coding: utf-8 -*- 

"""
code: by shylune
time: 2018-11-08
note: 优先级队列
"""
from queue import PriorityQueue


def test():
    queue = PriorityQueue()
    tasks = [
        (-1, "am"),
        (-2, "be"),
        (-4, "is"),
        (-3, "are")
    ]
    for task in tasks:
        queue.put(task)

    while not queue.empty():
        print(queue.get())
    print(queue.get())


if __name__ == "__main__":
    test()
