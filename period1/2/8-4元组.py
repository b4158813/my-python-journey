# -*- coding: utf-8 -*-
'''
tuple
元祖于列表相似 但元素不可修改
'''

my_strs=('aaa','bbb','ccc')
print(my_strs[0])
print(my_strs[-1])
print(len(my_strs))#元组长度固定
names=[100,200,300,400]
my_tuple=(100,200,names)
my_tuple[2][0]=666#可以修改元组内部的列表的元素（并没有改变元组元素）
print(my_tuple)

#元组函数只有count和index




#打印一个直立的钝角三角形
a=1
while a<=5:
    b=1
    while a>=b:
        print("*",end=" ")
        b+=1
    print("")
    a+=1
d=4
while d>=1:
    c=4
    e=d
    while c>=e and e>=1:
        print("*",end=' ')
        e-=1
    print("")
    d-=1
    



#for循环可循环一个列表
for i in names:
    print(i)

for i in range(1,10):#range一定是（小，大）
    print(i)

c=range(1,10)#range在python3里是懒加载函数 在2里不是懒加载函数
print(c)

#while也可循环列表
i=0
while i<len(names):
    print(names[i])
    i+=1



###可变类型：list
###不可变类型：数值 字符串 元组




















