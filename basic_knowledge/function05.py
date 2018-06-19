# -*- coding: utf-8 -*-

"""
******************** 匿名函数 *****************
关键字lambda表示匿名函数, 冒号 ":" 前面的变量表示函数参数

优点： 不需要显式地定义函数, 直接传入, 方便; 不用担心命名冲突
缺点:  限制只能有一个表达式, 但是不用写return, 返回值就是该表达式的结果

匿名函数也是对象, 可以赋值, 也可以作为返回值
"""

# 赋值
f = lambda x: x * x


# 作为返回值
def get_lambda(x, y):
    return lambda: x * x + y * y


if __name__ == "__main__":
    print(f(5))
    ff = get_lambda(3, 4)
    print(ff())

