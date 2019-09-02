# -*- coding: utf-8 -*-
#方法名如果是__xxx__()那么就有特殊功能，叫做魔法方法
class Person:
    #初始化对象的方法，不是构建对象的方法
    def __init__(self):#创建对象后自动执行该方法
        self.name="zs"
        self.age="18"
        print("对象初始化")
    def work(self):
       pass

p1=Person()#构建对象
print(p1.name)



class Person2():
    
    def __init__(self,name,age,height):#可在后面加形参
        self.name=name
        self.age=age
        self.height=height
        
    def __str__(self):#str方法：打印对象时，自动把对象转换成字符串
        return "姓名：%s,年龄：%s，身高：%scm"%(self.name,self.age,self.height)
    def introduce(self):
        print("姓名：%s,年龄：%s，身高：%s"%(self.name,self.age,self.height))
p2=Person2("zs","18","170")#构建对象
p2.introduce()
print(p2)




'''
对象形成的过程：
创建对象
__new__()构造对象方法，得到一个对象
__init__(self)初始化对象方法
'''