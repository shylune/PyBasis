# -*- coding: utf-8 -*-
import sys

"""
********************** 函数递归 *****************
在函数内部，可以调用其他函数；如果一个函数在内部调用自身，那么这个函数就是递归函数
递归的优点： 定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰
递归的缺点： 递归算法解题的运行效率较低。在递归调用的过程当中系统为每一层的返回点、局部量等开辟了栈来存储。递归次数过多容易造成栈溢出等

注意点：
    1、 防止栈溢出：
        在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
        每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
        在python中，默认是的递归深度是999，当超过这个深度就会抛出 RecursionError 错误， 这个错误可以
        通过 sys.setrecursionlimit(n) 来设置解决(貌似治标不治本)
    2、 尾递归问题
        尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
        这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

"""


# 1、求阶乘
def fact(n):
    if not isinstance(n, int) or n <= 0:
        raise Exception("value error, parameter need positive number")
    if n == 1:
        return 1
    return n * fact(n-1)

# sys.setrecursionlimit(2000)
# print(fact(998))


# 2、 尾递归方式实现阶乘
def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# 大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
# 实际上，这种方式在Python中递归的次数反而不如正常递归的简单有效了
# print(fact1(998))
