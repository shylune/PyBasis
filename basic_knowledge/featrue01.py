# -*- coding: utf-8 -*-
from collections import Iterable

"""
******************* 高级特性 之 切片 和 迭代 ******************
1、 切片
    常见用途：截取 list 或者 tuple 对象的一部分.
    表示方式： obj[x: y : z], 其中 x 是起始索引, y 是结束索引, z 是跨度大小
    索引： 可以从正向开始（默认x=0, z=1）, 也可以逆向开始(即倒序截取, 逆向第一个元素索引为： -1 )

2、 迭代
    常见用途： 遍历对象内部元素.
    操作方式： for ... in ...
    迭代过程中不用关注对象是否是 list或tuple , 只要是可迭代对象即可（这点于java是有别的）
    判断对象是否可迭代可使用 isinstance(obj, Iterable)
"""

# eg. list 逆序
aa = [1, 2, 3, 4, 5]
bb = aa[::-1]               # 这种方式简洁，比起使用for遍历生成list不要太方便
print(bb)

cc = list(reversed(aa))     # reversed() 内置函数会返回一个逆序迭代器
print(cc)

aa.reverse()                # reverse() 对象实例函数是改变对象本身，不是另外生成, 所以函数本身不返回（None）
print(aa)


# eg. for 遍历
if isinstance(aa, Iterable):
    for a in aa:
        print(a)

    for i, a in enumerate(aa, 1):
        print(i, " : ", a)

# 对于字典对象，默认情况下，迭代是key, dict默认是无序的
dd = {"a": "python", "b": "java", "c": "golang", "d": "shell"}
for key in dd:
    print(key)

for key, value in dd.items():
    print(key, ":", value)



