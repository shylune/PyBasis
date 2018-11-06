# -*- coding: utf-8 -*-

"""
********************** 闭包 ******************
Python中一切皆对象，函数可以作为参数传递，也可以作为返回值返回。
这种函数中又定义了函数，并且内部函数可以引用外部函数的参数和局部变量，
当调用外部函数返回内部函数时，相关参数和变量都保存在返回的函数中，这种程序结构称之为闭包（Closure）。

"""


def outer(x):
    y = 5

    def inner():
        return 2 * x + y
    return inner


if __name__ == '__main__':
    func = outer(8)
    print(func())
