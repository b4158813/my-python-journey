'''
描述性统计
'''
import numpy as np
import pandas as pd
from pandas import DataFrame,Series

a = DataFrame(np.random.randint(1,100,(5,5)),columns=['a','b','c','d','e'])
print(a,'\n')
print(a.mean(0),'\n')# 0轴进行统计
print(a.mean(1),'\n')# 1轴进行统计

print(20*'-')
'''
apply方法：对数据应用函数方法
'''
print(a,'\n')
print(a.apply(np.cumsum),'\n')# cumsum求和方法
print(a.apply(lambda x: x.max()-x.min()))# 自定义方法

