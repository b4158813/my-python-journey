# -*- coding: utf-8 -*-

import sys
print(sys.argv)


#列表推导公式
a=[i for i in range(1,10)]#生成1-9的列表
print(a)

b=[i**2 for i in range(1,10)]
print(b)

c=[x for x in range(1,3) for y in range(0,2)]#循环嵌套
print(c)



d=[i for i in range(1,101) if i%2==1]#打印奇数
print(d)


e=[1,2,3]
f=[[e[0]+i,e[1]+i,e[2]+i] for i in range(0,98) if i%3==0]
print(f)



