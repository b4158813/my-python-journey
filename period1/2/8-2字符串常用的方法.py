# -*- coding: utf-8 -*-

#切片 字符串截取
#【起始：结束：步长（下标变化的规律）】
name="abcefghijk"
print(name[0:2])#包含头不包含尾，这打印出来是 ab
print(name[:-1])#起始位省略  默认以0起始
print(name[2:])#结束位不写 默认到最后一个字符
print(name[0::2])#从第一个开始 往后每次 +2 选取
#不写步长 默认为+1

#字符串的反转
#用程序表示如下
i=len(name)
while i>0:
    i-=1
    print(name[i],end="")
print('')
#用字符串方法
print(name[-1::-1])#这里注意步长应该是-1


''''''''''''''''''''''''
my_str="hello world bjsxt laoxiao is bjsxt.com"
#find函数：
print(my_str.find('laoxiao'))#找到所确定字符串的第一个字符的下标
#空格算一个字符
print(my_str.find('laowang'))#找不到 只会返回-1
print(my_str.find('bjsxt'))#find函数默认从左边开始找 且只找第一个符合的字符串
print(my_str.rfind('bjsxt'))#rfind函数则从右开始找
#index函数：
print(my_str.index('bjsxt'))#index函数与find类似 具有索引功能
print(my_str.index('laoxiao'))#找不到 则会报错
#rindex 与rfind同理

'''
查找字符串：
find，找不到返回-1
index，找不到报错
都是从左边找，右边找加r
'''

#count函数（统计出现次数）
print(my_str.count('bjsxt'))

#replace函数（替换字符串）
print(my_str.replace('laoxiao','laowang'))
print(my_str.replace('bjsxt','laowang',1))
#查找并替换 默认替换全部符合条件字符串 替换第几个需要在后面加序号



#split函数（分隔 切割 字符串）   常见！
print(my_str.split(' '))#引号内为隔开符 这里是空格
print(my_str.split('laoxiao'))#隔开符为laoxiao 
#  split结构中不存在隔开符
print(my_str.split(' ',2))#2表示分隔两次 隔成三个片段
#partition函数 
print(my_str.partition('laoxiao'))
#partition结构中存在隔开符



#capitalize函数（大写第一个字符）
#title函数（大写每个单词首字母）
print(my_str.capitalize())
print(my_str.title())



#startwith（判断字符串是否以 开头，是则返回True，否则返回False）
#endwith（判断字符串是否以 结尾，是则返回True，否则返回False）

file_name="xxxx.txt"
if file_name.endswith(".txt"):
    print('文本文件')
    
    
    
#lower（把字符串所有字母变成小写）
#upper（把字符串所有字母变成大写）
#验证码应用
str="ABC"
user_str="AbC"
user_str.upper()



#下面三个函数作用为 字符串对齐
#ljust（左对齐）
#rjust（右对齐）
#center（居中对齐）
print(name.ljust(50))#宽度为50像素
print(name.rjust(50))
print(name.center(50))



###删除空白字符：
#lstrip（删除左边空白字符）
#rstrip（删除右边空白字符）
#strip（删除左右两端空白字符）
test_str="    abc     "
print(test_str.strip())
print(test_str.lstrip())
print(test_str.rstrip())



#splitlines（按照换行符隔开） 不需记！
line="asd\ngsdgs\ndgaseg\nsddsf\nsdrwqe"
print(line.splitlines())
print(line.split("\n"))



#isalpha（字符串都是字母则True）
#isdigit（字符串都是数字则True）
#isalnum（字符串都是字母或数字则True）
#isspace（字符串都是空格则True）
print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.isspace())




#join （将列表转化成新字符串）
names=['100','200','300']
print(''.join(names))#将空字符串放到每个元素后面练成一个新字符串
print('-'.join(names))#同上




