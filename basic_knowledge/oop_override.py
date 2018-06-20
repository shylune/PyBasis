# -*- coding: utf-8 -*-


"""
******************** 面向对象 之 方法重写（覆盖） *****************
1. 方法重载（overload）
    重载的定义： 函数名相同, 但是函数签名（参数个数, 类型, 返回值类型等）不同
    与Java等编译型的面型对象语言有所不同的是， Python 不存在（或者说不需要）方法重载， 这完全得益于Python是一种解释型语言。
    但是, 这并不是说 python 就不允许在class内部定义两个同名函数, python 允许这样做, 只是后面的函数定义将会覆盖前面的函数定义,
    也就是说在class 内部声明定义多个同名函数时, 真正起作用的只是最后一个。

2. 方法重写（override）
    重写的定义： 函数声明一样，只是具体的实现不同
    由于python的方法重载与其他语言有所不同, 那么重写也有所不同。
    个人的理解是, python的重写倒是与其他语言中的重载有点类似了, 因为子类对象重写父类方法时, python允许其函数签名不一样
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("name: " + self.name, "age: " + str(self.age) )


class Man(Person):
    def __init__(self, name, age):
        super(Man, self).__init__(name, age)
        self.gender = 'male'

    def print_info(self):
        print(self.name)

    def print_info(self):
        print("name: " + self.name, "age: " + str(self.age), "gender: " + self.gender)


class Woman(Person):
    def __init__(self, name, age):
        super(Woman, self).__init__(name, age)
        self.gender = 'male'

    def print_info(self, husband):
        print("name: " + self.name, "age: " + str(self.age), "gender: " + self.gender, "husband: " + husband)


if __name__ == "__main__":
    m = Man("小明", 23)
    m.print_info()

    wm = Woman("小丽", 25)
    wm.print_info(m.name)
