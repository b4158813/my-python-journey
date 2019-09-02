# -*- coding: utf-8 -*-
#打印序号+姓名：（第一种迭代方法 for或者while循环）
names=['zs','ls','ww','sl']
names2=['zs','ls','ww','sl']
j=0
print("序号\t姓名")
for i in names:#改成while也是一样
    j+=1
    print('%d\t%s'%(j,i))

print('='*20)
#第二种方式：
for i,item in enumerate(names):#枚举
    print('%d\t%s'%(i+1,item))
    
    
    
#字典常见函数： stu.kyes()/stu.values()/stu.items()
stu={'name':'laoxiao','age':'33'}
for k in stu.keys():
    print(k)
for v in stu.values():
    print(v)
print('='*20)
#迭代字典的常用方式：
for item in stu.items():#items函数获得是字典内元素，一个键+一个值
    print('key为:%s,value为:%s'%item)#item=(a,b)本身就是元组
    
#判断某个key是否在字典中：
print("="*20)
key='name'
if key in stu:
    print("%s在字典中"%key)
'''
if stu.has_key(key):
    print("%s在字典中"%key)
    该方法不常用，且仅在python2中有该函数
'''

    