# -*- coding: utf-8 -*-

#密码长度不够的异常
class PasswordException(Exception):
    
    def __init__(self,pw,min_length):
        self.password=pw
        self.min_length=min_length
    def __str__(self):
        return "%s的密码错误，密码的最小长度为%s"%(self.password,self.min_length)


def reg(username,password):
    if len(password)<6:
        raise PasswordException(password,6)#抛出你指定的异常
    else:
        print("用户名为:%s,密码为:%s"%(username,password))
        

try:
    reg("zs","123")
except Exception as ex:#捕获异常，并打印异常信息
    print("第一个except")
    print(ex)
except PasswordException as ex:#两个exc2ept会按照顺序先执行第一个，如果第一个满足异常类型条件，进入第一个except,不会进入后面的
    print("第二个except")
    print(ex)





