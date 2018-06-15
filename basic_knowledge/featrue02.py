# -*- coding: utf-8 -*-

"""
******************* 高级特性 之 生成式（也称 推导式） ******************
1、列表 生成式
    使用 [] 来生成
2、字典 生成式
    使用 {} 来生成
3、生成器 生成式
    使用 () 来生成
4、集合 生生成式
    使用 {} 来生成
"""


# List Comprehensions
l1 = [x * x for x in range(1, 11) if x % 2 == 0]
l2 = [m + n for m in 'ABC' for n in 'XYZ']

# Dict Comprehensions
test = {'a': 1, 'b': 3, 'c': 5}
d = {value: key for key, value in test.items()}

# Generator Comprehensions
g = (i*i for i in range(10))

# Set Comprehensions
s = {i for i in [1, 3, 5, 7, 5, 3, 2, 1]}

print(l1, l2, d, g, s)
