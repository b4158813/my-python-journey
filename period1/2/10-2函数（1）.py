# -*- coding: utf-8 -*-


student={"name":"laowang"}
a="laogao"
'''
在函数中修改全局变量：
1、如果是可变类型可以直接修改变量的值
2、如果全局变量是不可变类型，如果想要在函数中修改
不可变类型，其实本质上是在函数中修改不可变类型的全
局变量的引用，加上global就可以修改不可变变量的引用。

'''
b=100
def test1():
    print("原始的全局变量为：%s"%names)
    names[2]="laoxiao"
    student["age"]=23
    #a="goldbin" #定义了一个局部变量
    global a
    a="goldbin"#修改全局变量的引用
    global b
    b+=1
names=["laowang","lisi","zhangsan"]#全局变量定义在调用函数之前
test1()
print("最后的全局变量为：%s"%names)
print("最后的全局变量为student:%s"%student)
print("最后的全局变量a为%s"%a)
print("最后的全局变量b为%s"%b)


