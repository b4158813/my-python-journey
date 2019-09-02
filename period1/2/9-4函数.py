# -*- coding: utf-8 -*-

#复习
'''
if 条件表达式:
    pass
    pass
elif 条件表达式:
    pass

while 条件表达式：
    pass
    break
else:
    pass
    
for 变量（该变量不需要在前面申明） in 字符串或者集合:
    pass
else:
    
    
list
names=[任何类型的数据]   name[0]=值

tuple
names=(任何类型的数据)

dict
name={key:value}  names[key]=值

'''

#函数： 定义格式：
#def 函数名():
#       代码
#定义函数：
def print_hello():
    print("Hello World!")
#调用函数： 
print_hello()

#带参数的函数：
def test1(r):
    s=3.14*(r**2)
    print("圆的面积为：%s"%s)

#假设我发现一个圆，半径为9.8
r=9.8
test1(r)
#另外一个圆
test1(11.8)


































