# -*- coding: utf-8 -*-


"""
*************************** 面向对象 之 继承和多态 ***************************************
继承： 顾名思义就是子类继承父类之后，子类对象自然而然拥有了父类对象拥有的属性和方法，
      但是子类对象同时还可以定义拥有自己的属性方法

多态： 1. 子类对象重写父类方法  2.父类对象指向子类引用

鸭子类型： 动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
"""


class Animal(object):
    def __init__(self, color, height):
        self.color = color
        self.__height = height

    @property
    def height(self):
        return self.__height

    def eat(self):
        print("animal's color is " + self.color + " and is eating .")


class Dog(Animal):
    def __init__(self, color, height):
        super(Dog, self).__init__(color, height)

    def eat(self):
        print("dog's color is " + self.color + " and is eating .")


class Other(object):
    def __init__(self):
        self.name = "duck"

    def eat(self):
        print("other object instance is eating . duck, duck, duck ...")


def polymorpuic01(animal):
    if not isinstance(animal, Animal):
        raise TypeError("parameter is not instance of Animal")
    animal.eat()


def polymorpuic02(eatable):
    if hasattr(eatable, 'eat'):
        eat = getattr(eatable, 'eat')
        eat()


if __name__ == "__main__":
    d = Dog('Red', 25)
    o = Other()
    polymorpuic01(d)
    # polymorpuic01(o)  # 报错

    polymorpuic02(o)
    polymorpuic02(d)    # 鸭子类型包括多态


