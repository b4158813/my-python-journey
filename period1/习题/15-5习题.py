# -*- coding: utf-8 -*-

'''
#set:集合类型
列表（list）     a=[]      先后顺序，有下标位[index],可以重复，可变类型
元组（tuple）    a=()      先后顺序，有下标位，元素可以重复，不可变（只能查）
字典（dict）     a={key:value}  没有先后顺序，没有下标，key不可重复，value可以，可变
集合（set）      a={}      没有先后顺序，没有下标，不可重复，可变类型
'''
#空集合：set{}  
#空字典：{}
a={1,2,3,4}
a.add(5)
print(a)
a.add(5)
print(a)
b={1,2,1,2,1,2,1,2}#两个元素
print(b)
i=b.pop()#去除一个元素
print(i)
print(b)
l=list(a)
print(l)
s=set(l)
print(s)
t=tuple(s)
print(t)
li=[1,2,3,4,1,2,3,4]#八个元素
print(len(li))
li=set(li)#去重复
print(len(li))
li=list(li)#变回列表
print(li)

print("="*20)
#############################################
#写一段python代码，实现列表去重（不用set）
a=[1,2,3,4,5,6,1,2,3,4]
def change_list(li):
    temp=[]
    for i in li:
        if i not in temp:
            temp.append(i)
    return temp

if __name__=="__main__":
    print(change_list(a))

#############################################
print("="*20)
#写出一段python代码实现分组一个list里面的元素 如[1,2,3,...100]变成[[1,2,3],[4,5,6],...]
b=[i for i in range(1,101)]
def part_list(li):
    temp=[]
    for i in b:
        if i%3==0:
            temp.append([b[i-3],b[i-2],b[i-1]])
    return temp

if __name__=="__main__":
    print(part_list(b))
    
#############################################
print("="*20)
#写出一个函数，给定参数n,生成含有n个元素值为1-n的列表，元素顺序随机，但值不重复
import random
def create_list(n):
    temp=[]
    while True:
        if len(temp)==n:
            break
        i=random.randint(1,n)
        if i not in temp:
            temp.append(i)
    return temp
if __name__=="__main__":    
    print(create_list(5))
##########################################
print("="*20)
#仔细斟酌下面这段代码
def extendList(val,list=[]):
    list.append(val)
    return list
list1=extendList(10)
list2=extendList(123,['a','b','c'])
list3=extendList("a")
print("list1=%s"%list1)
print("list2=%s"%list2)
print("list3=%s"%list3)
#第一次调用extendList方法和第三地调用的时候，两次调用list形参指向的内存地址一样


















