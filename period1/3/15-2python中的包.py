# -*- coding: utf-8 -*-

#导入模块时，首先在当前目录下找，其次去python系统（home）目录下找。

#在python2中：有一个目录，并且目录下有一个__init__.py的文件，才叫包。
#有__init__.py文件在python3中不会有错，以后都在包的目录下新建一个__init__.py文件

import my_package
#from my_package import module1

my_package.module1.test1()
#module.test1()














