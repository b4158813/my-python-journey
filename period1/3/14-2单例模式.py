# -*- coding: utf-8 -*-
#两种单例模式
'''
class User(object):
    __instance=None
    def __init__(self,name):
        self.name=name
    
    @classmethod
    def get_instance(cls,name):
        if not cls.__instance:#如果__instance为none
            cls.__instance=User(name)
        return cls.__instance
    
    
#u1=User("zs")
#u2=User("ls")
u1=User.get_instance("zs")
u2=User.get_instance("ls")
####这两个对象name属性值都是"zs"
print(u1==u2)#判断表达式，如果返回True这两个对象是一个对象，并且内存地址相同
print("u1对象的内存地址：%s\nu2对象的内存地址：%s"%(id(u1),id(u2)))
'''


class User(object):
    __instance=None
    def __init__(self,name):
        self.name=name

    def __new__(cls,name):
        if not cls.__instance:#保证 object.__new__()方法只会调用一次
            cls.__instance=object.__new__(cls)
        return cls.__instance

u1=User("zs")
u2=User("ls")
print(u1.name)
print(u2.name)####这两个对象name属性值都是"ls"
print(u1==u2)#判断表达式，如果返回True这两个对象是一个对象，并且内存地址相同
print("u1对象的内存地址：%s\nu2对象的内存地址：%s"%(id(u1),id(u2)))












