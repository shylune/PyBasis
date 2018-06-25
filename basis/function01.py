# -*- coding: utf-8 -*-

"""
************** 函数 ******************
定义： 使用def语句定义函数，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回

"""


# 1、函数的定义
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


# 2、空函数
def nop():
    pass


# 3、位置参数
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 4、默认参数 *****:定义默认参数要牢记一点：默认参数必须指向不变对象！
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 5、可变参数 (函数内部将接收到的多个参数组合成一个tuple)
def calc(*numbers):
    s = 0
    for n in numbers:   # type(numbers) is tuple
        s = s + n * n
    return s


# 可变参数函数调用
# nums1 = (1, 2, 3, 4)
# nums2 = [1, 2, 3, 4]
# print(calc(*nums1))
# print(calc(*nums2))
# print(calc(1, 2, 3, 4, 5))

# 6、关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kwargs):
    print('name:', name, 'age:', age, 'other:', kwargs)


# person('xiaoming', 21, male='F')
# person('xiaowang', 21, male='M', job='engineer')


# 7、命名关键字参数 (可以限制关键字参数)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def people(name, age, *, city, job):
    print(name, age, city, job)


# people('xiaowang', 21, male='M', job='engineer')


# 8、参数组合
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
