# -*- coding: utf-8 -*-

'''
可变类型：值可以修改（内存地址不变，但是所保存的值变化了），引用可以修改（变量的内存地址变化了）
不可变类型：值不可以修改，可以修改变量的引用（=赋值号）
'''

a=[1,2]
print(id(a))
a.insert(2,5)#改变值，地址不变
print(a)
print(id(a))
a=[4,5]#改变引用，地址变
print(id(a))
print("="*20)
b="abcd"
print(id(b))
b="efgh"#改引用
print(id(b))

'''
在函数里面修改全局变量：
1、如果全局变量是可变类型，可以在函数里面任意修改（值，引用）
2、如果全局变量是不可变类型，在函数里面不能修改值，也不能修改引用，初非加上global才能修改引用
'''
print("="*20)
#函数返回多个结果：

def test1():
    a=1
    b=2
    return [a,b]
x=test1()
print(x)

#缺省参数：
def test1(x,y,z=10,w=10):#z,w为z,w缺省时的默认值
#def test1(x,z=10,y)#语法错误，默认参数必须放后面
    print(x,y,z,w)
    return x+y+z
print("三个数的和：%s"%test1(5,8,20))

print("abc",end="")#print函数参数个数位置不确定，所以后面需要指明参数等于多少
#help(print)

print("="*20)
#不定长参数：

def test2(x,y,*args,z=10):#*args不定长参数
    print(x,y)
    print(args)
    sum=x+y
    for i in args:
        sum+=i
    print("和为：%s"%sum)
test2(2,3,4,5,6,7,z=20)#此时传值给z必须写明是z
print("="*20)
def test3(x,*args,**kwargs):#**kwargs有名字参数
    print(x)
    print(args)
    print(kwargs)
    sum=x
    for i in args:
        sum+=i
    for i in kwargs.values():
        sum+=i
    print("和为：%s"%sum)
test3(2,3,4,num1=5,num2=6)

print("="*20)

#集合的拆包：
nums=[3,4]
nums2={"num1":5,"sdfs":6}
test3(2,*nums,**nums2)#需要加*（列表*，字典**）拆包才能传值

#传参数注意：
def test(x,y):
    x=x.replace("c","C")#把一个新的字符串赋值给x，此时x地址改变，但a不变
    y.append(10)
    print("x变量指向的内存地址为：%s"%id(x))
    print("y变量指向的内存地址为：%s"%id(y))

a="abcefg"
b=[1,2,3]
print("a变量指向的内存地址为：%s"%id(a))
print("b变量指向的内存地址为：%s"%id(b))

test(a,b)#x,y接受a,b  x,y就分别指向a,b所指向的内存地址
























