# -*- coding: utf-8 -*-


"""
**************** 面向对象 之 类与实例 *****************
1、类（class）是创建实例的模板，而实例(instance)则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
2、方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据(实例方法通过 self )；
3、通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
4、和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同（可以动态绑定）

"""


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == "__main__":
    lily = Student('lily', 21, 97)
    lucy = Student('lucy', 21, 78)
    print(lily.get_grade())
    lucy.address = "test address"
    print(lucy.name, lucy.age, lucy.get_grade(), lucy.address)
    # 能够在“运行时”创建实例属性，是 Python 类的优秀特性之一（正好验证笔记中的第4点）
    # print(lily.name, lily.age, lily.get_grade(), lily.address)