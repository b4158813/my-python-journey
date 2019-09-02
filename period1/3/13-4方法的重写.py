# -*- coding: utf-8 -*-

#重写：子类中有一个和父类相同名字的方法（只要方法名一样就是重写）

class Animal:
    
    def __init__(self):
        print("动物的初始化")
        self.color="黄色"
    def eat(self):
        print('-----吃饭-----')
    def sleep(self):
        print('-----睡觉-----')
        
class Dog(Animal):#继承Animal类里所有方法
    #init 和父类init名字一样，所以叫方法的重写
    def __init__(self,name):
        super().__init__()#主动调用父类的init方法
        self.name=name
    def eat(self):
        super().eat()#主动调用父类的eat方法
        print("狗自己的eat方法")
    def shout(self):
        print("-----汪汪叫-----")
        
class Cat(Animal):
    #重写父类的init方法
    def __init__(self):
        print("猫初始化了")
    def catch(self):
        print("-----抓老鼠-----")
    def mew(self):
        print("-----喵喵叫-----")
class ZangAo(Dog):#本身-父类-父类的父类
    def fight(self):
        print("-----战斗-----")
    
    
dog=Dog("小白")#如果子类中对某个方法重写了，优先调用子类自己本身的方法
print(dog.name)
print(dog.color) 
#虽然init方法重写了，可还是想自动调用父类的init方法
dog.eat()























