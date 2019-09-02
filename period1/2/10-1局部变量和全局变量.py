# -*- coding: utf-8 -*-
'''
def 函数名（[参数...]）:
    pass
    pass
    if 条件：
        return 当函数执行到return时候后面所有代码都不会执行
    pass
    pass
'''
a=400#全局变量，可以再后面的代码中使用
def test1():
    a=200#局部变量只能在该函数中使用（它的作用范围在该函数里面）
    a+=1
    print("a的值为%s"%a)
    return a

def test2(a):
    #a=300#如果函数中的局部变量和全局变量的名字一样，优先使用局部变量
    print("test2中a的值为：%s"%a)
b=test1()
test2(b)
print(a)
    
    