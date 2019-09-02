# -*- coding: utf-8 -*-

def test(a,b,func):
    result=func(a,b)
    return result
func_new=input("请输入你的操作：")#python3里input默认输入为字符串
func_new=eval(func_new)#把字符串转换成可以执行的表达式
print(test(22,33,func_new))


#复习：
'''
#交换a,b的值：
借用元组：   a,b=b,a
使用中间值：
t=0
t=a
a=b
b=t
'''

'''
可变类型与不可变类型辨析：
def test(num):
    #num+=num(如果是a=10则相当于num=num+num，因为此时a是不可变类型)
    #num=num+num（赋值符号，引用一定会变，无论是不可变还是可变类型）
    print(num)
a=10与a=[10] 最后打印的结果不同（前者打印两个不同的值，后者打印两个相同的值）
test(a)
print(a)
'''

'''
list和dict不可以作为dict的key：
dict用了哈希算法，同一个字典所有的key不允许有相同的哈希值（key不能重复）
而list和dict尽管值变了，哈希值没变
*可变类型不能作为字典的key*
'''
























