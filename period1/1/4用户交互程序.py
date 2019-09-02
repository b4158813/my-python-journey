# -*- coding: utf-8 -*-
'''
username = input('username:')
password = input('password:')
print(username,password)
'''


Name = input('Name:')
#raw_input 2.x      input 3.x
#input 2.x 没用 多余
Age = int(input('Age:'))#integer
print(type(Age),type(str(Age)))
#所有输入的字符都默认为字符串类型，需要强制转换成整型
Job = input('Job:')
Salary = input('Salary:')
info = '''
-------- info of %s -------
Name:%s
Age:%s
Job:%s
Salary:%s
''' %(Name,Name,Age,Job,Salary)

print(info)

#下面是另一种定义格式


info2 = '''
-------- info of {_Name} -------
Name:{_Name}
Age:{_Age}
Job:{_Job}
Salary:{_Salary}
''' .format(_Name=Name,
_Age=Age,
_Job=Job,
_Salary=Salary)

print(info2)

#下面是另一种方式

info3 = '''
-------- info of {0} -------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
''' .format(Name,Age,Job,Salary)

print(info3)