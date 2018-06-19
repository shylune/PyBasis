# -*- coding: utf-8 -*-


"""
******************* 返回值函数 *********************
1、 高阶函数可以将函数作为参数, 如: map()等; 同理, 高阶函数也可以将函数作为返回值返回
2、 调用返回函数, 需要特别注意闭包问题, 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
"""


def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs       # count函数返回结束是，i=3


def count2():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


if __name__ == "__main__":
    f1, f2, f3 = count1()
    print(f1(), f2(), f3())

    f11, f22, f33 = count2()
    print(f11(), f22(), f33())
