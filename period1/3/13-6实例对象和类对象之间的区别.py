# -*- coding: utf-8 -*-

class User(object):
    name="zs"#公共的类属性
    __password="123456"#私有（隐藏）的类属性(对外隐藏)
    
    def __init__(self,sex,username):
        self.sex=sex
        self.name=username

class QQ_User(User):
    pass

u=User("男","goldbin")
print(QQ_User.name)#name从父类继承过来的，name属于类属性，可直接通过类来访问，也可以通过类的对象来访问
print(u.name)#对象属性和类属性名字一样，如果通过对象来访问会选择对象属性
print(User.name)#通过类属性访问
#类属性修改,只能通过类来修改
u.name="ww"#本质上没有修改类属性，仅仅给该对象定义了一个对象属性name，并且赋值为"ww"
print(u.name)
print(User.name)
User.name="ww"#真正的类属性修改
print(User.name)
#print(User.__password) 私有类属性不能在类外部被引用
del u.name#删除了对象的name属性，并没有删除类属性
print(User.name)
del User.name#真正的类属性删除

print("="*20)
###############################
#类方法####
#########
class A(object):
    name="zs"
    
    def test1(self):
        print("-----A 的test1方法")
    @classmethod#类方法一定要在方法的上面加上一个修饰器（java注解），类方法的参数一定是cls,代表当前的类
    def test2(cls):
        cls.name="ww"
        print("-----A 的test2方法")

a=A()
a.test2()
A.test2()
print(A.name)
































