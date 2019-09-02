# -*- coding: utf-8 -*-

#第一个匿名函数：
def test(a,b):
    return a+b
print(test(22,33))
func=lambda x,y:x+y#这里把函数本身赋值给func，冒号后面只能接表达式
print(func(22,33))

#匿名函数应用1：
def test(a,b,func):
    result=func(a,b)
    return result
print(test(22,33,lambda x,y:x*y))

#匿名函数应用2：
stus=[{"name":"zs","age":22},{"name":"lw","age":33},{"name":"ainiyiwannian","age":18}]
a=[22,2,5,5,66,5,4,4,5]
#a.sort(reverse=True)#降序排序
#a.reverse()#反转
#print(a)
stus.sort(key=lambda x:x["age"],reverse=True)
#默认情况下key是列表中每一个元素本身，而这里匿名函数返回了每个元素（字典）的“name”对应的值，这里sort就会根据指定的值进行比较
print(stus)





