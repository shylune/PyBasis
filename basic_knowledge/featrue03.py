# -*- coding: utf-8 -*-
from collections import Iterator

"""
******************* 高级特性 之 可迭代对象 迭代器 和 生成器 ******************

在python中, 可以直接作用于for循环的迭代遍历对象统称为可迭代对象：Iterable,
主要包括：一类是集合数据类型, 如: list, tuple, dict, set, str等；另一类是generator, 包括生成器和带yield的生成器函数。

可迭代对象（Iterable）: 实现了 __iter__() 方法
                      __iter__返回迭代器自身,
迭代器（Iterator）   : 实现了 __iter__() 和 __next__() 方法
                     __next__返回容器中的下一个值, 如果容器中没有更多元素了, 则抛出StopIteration异常

生成器（Generator）  : 是一种特殊的迭代器, 不过显得更优雅, 不需要显示实现上述两个函数；
                     一边循环一边计算, 节省空间, 有生成器推导式（）和 带 yield 的生成器函数两种定义方式.

三者关系： 生成器是一种特殊的迭代器， 迭代器是一种特殊的可迭代对象
"""


class MyIterable(object):
    def __init__(self, *args):
        self.args = args
        self.index = 0

    def __iter__(self):
        return self    # 返回一个迭代器对象

    def __next__(self):
        if self.index > len(self.args) - 1:
            raise StopIteration
        else:
            self.index += 1
            return self.args[self.index-1]


class MyIterator(Iterator):
    def __init__(self, *args):
        self.args = args
        self.index = 0

    def __next__(self):
        if self.index > len(self.args) - 1:
            raise StopIteration
        else:
            self.index += 1
            return self.args[self.index-1]


gen1 = (g*g for g in range(10))


def gen2(x):
    for i in range(x):
        yield i * i


if __name__ == "__main__":
    args = [1, 3, 5, 7, 9, 11]
    my_iterable = MyIterable(*args)
    print(isinstance(my_iterable, Iterator))
    for i in my_iterable:
        print(i)

    my_iterator = MyIterator(1, 2, 3,  'a', 'b', 'c')
    print(isinstance(my_iterator, Iterator))
    for i in my_iterator:
        print(i)

    print(isinstance(gen1, Iterator))
    for i in gen2(10):
        print(i)
