# -*- coding: utf-8 -*-
from collections import Iterator
from functools import reduce

"""
*************** 内置常用高阶函数 *************
1、 map()
    map函数接收两个参数, 第一个是函数, 第二是Iterable; map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
    由于结果是一个Iterator，Iterator是惰性序列，因此可以通过list()函数让它把整个序列都计算出来并返回一个list
    注意： Python27 和 Python3x map返回的结果类型有所不同, 此处以Python3为准
    
2、 reduce()
    reduce把一个函数f作用在一个序列[x1, x2, x3, ...]上, 这个函数f必须接收两个参数, reduce把结果继续和序列的下一个元素做累积计算
    其效果相当于： reduce(f, [x1, x2, x3, x4]) == f(f(f(x1, x2), x3), x4)
    注意： Python27中reduce是内置函数, 无需引入模块; Python3中需要从 functools 模块中引入
    
3、 filter()
    filter()接收一个函数和一个序列, 传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
    
4、 sorted()
    sorted()也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序, 返回一个新List
"""


# *************** eg. map() ****************
def double(x):
    return 2*x


m = map(double, [1, 2, 3, 4, 'a'])
print("the type of result m is ", type(m))
print("the return value of map is instance of Iterator? ", isinstance(m, Iterator))
print("the result of converting object m is ", list(m))


# *************** eg. reduce() ****************
def rfunc(x, y):
    return 10 * x + y


r = reduce(rfunc, [1, 2, 3, 4, 5])
print("result of reduce function is ", r)


# *************** eg. filter() *****************
def is_odd(x):
    return x % 2 == 1


f = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("the type of result f is ", type(f))
print("the return value of filter is instance of Iterator? ", isinstance(f, Iterator))
print("the result of converting object f is ", list(f))


# ***************** eg. sorted() ******************
test = [1, 4, 33, 22, -73, 45, 76, 2, 9, 10, -88, 109]
s = sorted(test, key=abs, reverse=True)
print("the type of result s is ", type(s))
print("the return value of sorted is instance of Iterator? ", isinstance(f, Iterator))
print(s)



