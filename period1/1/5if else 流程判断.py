# -*- coding: utf-8 -*-

import getpass
#这是将密码改为密文（但密文在此不适用） 
_username = 'gary'
_password = 'gary'

username = input('username:')
password = getpass.getpass('password:')

if _username == username and _password == password:
    print('welcome user {name} login...'.format(name=_username))
else:
    print('invalid username or password!')
#强制缩进 省去了结束符
#所有的代码如果是顶级的 都必须顶格写
    
    