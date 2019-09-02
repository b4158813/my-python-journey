# -*- coding: utf-8 -*-
'''
class User:
    
    def __str__(self):
        return "用户名为：%s，密码为：%s"%(self.username,self.password)
    def set_password(self,pw):
        if len(pw)>=6:
            self.password=pw
        else:
            print("密码%s,长度不符合规定"%pw)
        
u1=User()
u1.username='goldbin'
u1.set_password='123'
u1.password='123'
print(u1)
并没有达到隐藏属性的效果
'''
#私有（隐藏）属性和方法
class User:
    
    def __init__(self,pw):
        if len(pw)>=6:
            self.__password=pw#隐藏属性，不能在外面调用
        else:
            print("密码%s,密码不符合规定"%pw)
    def __str__(self):
        self.__say_hello()#隐藏方法可以再里面调用
        return "密码%s"%self.__password
    def __say_hello(self):#隐藏方法，开头带有__的方法不允许在外面访问调用，但可以在里面调用
        print(self.__password)
    def get_password(self):
        return self.__password#需要在类里面改变隐藏属性，不允许外面代码调用


u1=User("123456")
#u1.__password="1234567"不能调用
#print(u1.__password)不能打印
#print(u1.get_password()) 正确
#u1.__say_hello 不能调用
print(u1)


#和C++内 puplic 和 private 同理
















