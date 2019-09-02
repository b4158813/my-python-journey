# -*- coding: utf-8 -*-
# __del__（）方法
class User:
    
    def __init__(self):
        print('====对象初始化====')
    
    def __del__(self):
        print("对象即将要被销毁（内存回收）")
        

u1=User()
u2=u1
del u1#对象引用计数为1
print("-"*20)
del u2#对象引用计数为0，执行__del__()方法
print('='*20)
#整个程序执行完成后，也会调用__del__方法（内存肯定会被回收）


print("\n"*3)
##################################
#继承
class Animal:
    
    def __init__(self):
        print("动物的初始化")
        self.name="动物"
    def eat(self):
        print('-----吃饭-----')
    def sleep(self):
        print('-----睡觉-----')
        
class Dog(Animal):#继承Animal类里所有方法
    #init 和父类init名字一样，所以叫方法的重写
    def __init__(self,name):
        self.name=name
    def shout(self):
        print("-----汪汪叫-----")
        
class Cat(Animal):
    
    def __init__(self):
        print("猫初始化了")
    def catch(self):
        print("-----抓老鼠-----")
    def mew(self):
        print("-----喵喵叫-----")
class ZangAo(Dog):#本身-父类-父类的父类
    def fight(self):
        print("-----战斗-----")
    
    
dog=Dog("小白")
dog.eat()
cat=Cat()
#print(cat.name)#优先调用自身类的__init__方法，此时没有name属性，故无法打印
za=ZangAo("藏獒")
za.eat()

























    














