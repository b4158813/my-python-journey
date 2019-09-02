# -*- coding: utf-8 -*-

#九九乘法表

x = 1
while x <=9:
    y=1
    while y <=x:
        print('%d*%d=%d\t'%(y,x,x*y),end="")
        y+=1
    print('')
    x+=1
#/t 为制表符1
    
#作业：打印倒等边三角形 用户输入边长
'''
此题值得反复琢磨
'''
i = int(input("请输入边长："))
a=0
while a < i:
    b=0
    while b < a:
        print(end=" ")
        b+=1
    c = i
    while c > a:
        print("*",end=" ")
        c-=1
    print('')
    a+=1


