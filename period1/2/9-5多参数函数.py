# -*- coding: utf-8 -*-

#def 函数名():
#       pass

#def 函数名(参数1，参数2...):#参数1可以随便写一个名字，在之前不需要定义

a=1
def test2(a,b):#a和b是形参，不用在前面定义，也不会和之前定义的变量冲突
    sum=a+b
    print("%s加上%s的和为：%s"%(a,b,sum))

test2(a,20)#在调用函数的时候传给函数参数的数据叫实参，20和a都是实参


def sum_2num_noreturn(a,b):
    sum=a+b

def sum_2num(a,b):
    if not isinstance(a,(int,float)):#判断a是整数或者浮点型，是则返回True
        print("传入的a是%s，不是一个数字类型"%a)
        return
    elif not isinstance(b,(int,float)):#判断a是整数或者浮点型，是则返回True
        print("传入的a是%s，不是一个数字类型"%b)
        return#如果b也不是一个数字，函数后面的代码没有必要执行
    sum=a+b
    return sum#return 被执行之后，不管return后面还有什么代码，都不会执行
    print("sum_2num求和%d"%sum)#这行代码不会执行
num1=2
num2=9
s=sum_2num(num1,num2)
print(s)    
s2=sum_2num_noreturn(num1,num2)


############
s=sum_2num("abc",2)





































