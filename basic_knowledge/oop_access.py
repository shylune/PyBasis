# -*- coding: utf-8 -*-


"""
****************** 面向对象 之 访问权限和属性 ******************
1. 访问权限
    __ : private, 私有权限(相对的, 其实在外部 python 解释器将其翻译成了 _ClassName__PropertyName)
    _  : protected, 受保护权限(意为 '虽然我可以被访问, 但是请把我视为私有变量,不要随意访问')
       : public, 公开权限 (变量前面没有 "_"的)

    __xx__ : 类似这种形式的变量是有特殊用途的(一般为系统内置变量), 特殊变量是可以直接访问的

    注意： Python本身没有任何“真正的”机制阻止你干坏事，一切全靠自觉

2. 属性（property）


"""


class Teacher(object):
    note = "I'm a teacher"                      # 类变量

    def __init__(self, name, age, gender):
        self.__name = name                      # 实例变量
        self._age = age
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


if __name__ == '__main__':
    t = Teacher('LiLei', 34, 'male')
    t.name = 'XiaoMing'
    t.__name = "ZhangSan"     # 这是为 t 动态增加了另外一个__name属性, 这个与Teacher内部的__name不是同一个(内部的解释器可能已经将其改成了_Teacher__name 或者其他)
    print(t.name, t.__name, t._age, t.gender)   # 访问时 _age 下面会有波浪线提示这是一个受保护的成员变量


