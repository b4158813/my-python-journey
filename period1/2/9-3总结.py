# -*- coding: utf-8 -*-

#可变类型与不可变类型
'''
不可变类型： 如 str 
可变类型： 如 list
'''

#不可变类型str 值不能变，操作完之后生成一个新的值
stu={'name':'ss'}
a='abc'
print(a.replace('a','A'))#replace函数返回值是一个新字符串，在一个新的内存空间内，但没有变量指向它
print(a)
b=a.replace('a','A')#赋值给b了以后，b就指向了新字符串
print(b)



#可变类型 list 
a=[1,2]
b=a#b也指向a的内存地址
print(id(a),"\n",id(b))#两者指向同一个内存地址
b+=[3,4]###b指向的内存地址加了一个新列表，这个列表改变了
print(b)
print(a)

c=[1,2]
d=c
d=d+[3,4]#等号右边有表达式，则先执行表达式，形成一个全新的列表，b再指向全新列表的内存地址
print(d)
print(c)
#a+=b <> a=a+b 仅对于可变类型成立


#运算符：  +   *   in   not in
#内置函数： cmp(只在python2中有)  len  max  min  del 


#作业

str=input("请输入一个字符串:")
res={}#key 不可能重复
for i in str:
    if i in res:
        res[i]=res[i]+1
    else:#表示第一次出现
        res[i]=1
print(res)





































