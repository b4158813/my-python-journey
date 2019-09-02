# -*- coding: utf-8 -*-

#dictionary 字典dict
#用key-value 存储
#如 d={'wlx':95,'yl':75,'wxy'=90}
#d['wlx']

stus={'name':'zs','age':33,'gender':'男'}
stus['name']='ww'
print(stus['age'])#dict没有顺序 不能用下标访问 通过key访问
#print(stus['address'])#key不存在就会报错
print(stus.get('age'))
print(stus.get('address'))#用get访问不存在的key返回none

#dict的 添 删 改    查
stus['address']='beijing'
print(stus)#若字典内存在则为修改  若不存在则为在后面添加

'name' in stus#查找须输入key而不是value

del stus['gender']#也可用clear 但不好（不能回收内存）
print(stus)

































