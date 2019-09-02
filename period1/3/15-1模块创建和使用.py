# -*- coding: utf-8 -*-
#import random as rm
#print(random.randint(0,5))
#from random import rndint
#print(randint(1,9))


#使用自己制作的模块
#import module1
from my_package import module1
from my_package import module2
#from module1 import *#不建议使用
#from module2 import *#如果两个模块中方法名字相同，则后面覆盖前面
a="22"
print(module1.isnull(a))
module2.test1()
















