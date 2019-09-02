'''
迭代器（Iterator）和可迭代对象（Iterable）
迭代是访问集合元素的一种方式

迭代器是一个可以记住遍历的位置的对象
迭代器只能往前不会后退

可迭代对象（Iterable）：
    1.集合数据类型：如 list、tuple、dict、set、str等
    2.生成器和带yield的generation function
'''

from collections import Iterable,Iterator
# 判断一个对象是不是可迭代对象
isinstance([],Iterable)# 判断列表是不是可迭代对象
isinstance((x for x in range(5)),Iterator)# 判断生成器是不是迭代器
# 将可迭代对象转换成迭代器
a = [1,2,3]
it = iter(a)# 将列表a转换成迭代器
