# -*- coding: utf-8 -*-

#python属弱类型语言，多态并不明显，在Java、C#这种强类型语言中比较明显


##############
#类属性####
##########
'''
#类属性：所属类，这个类下所有对象都可以共享这个类属性。相当于Java中静态属性。
比如：
    Class Person {
        public static String name="abc"
    }
'''
class User(object):
    name="zs"#公共的类属性
    __password="123456"#私有（隐藏）的类属性(对外隐藏)
    
    def __init__(self,sex,username):
        self.sex=sex
        self.username=username



u=User("男","goldbin")
print(u.name)
#print(u.__password) 私有的类属性，不可在外部访问
u2=User("女","adsf")
print(u2.name)#所有属于该类的对象公用类属性
















