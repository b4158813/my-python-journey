'''
引入约定
'''
import numpy as np
import pandas as pd
from pandas import DataFrame,Series# 数据框、一维数组

'''
Series
    包含：索引 和 值
'''
arr = np.arange(5)# 建立一个数组
series = Series(arr)# 建立一个Series
print(series.index)# 查看索引列
print(series.values)# 查看数据列
print(series.dtype)# 查看数据类型

print('-'*20)
'''
Series.index 属性
'''
series1 = Series([70,89,67],index=['张三','李四','王五'])# 实现数据索引的绑定
series1 = Series({'张三':70,'李四':89,'王五':67})# 也可通过字典定义
print(series1)

print(20*'-')

'''
Series缺失值检测
    isnull 和 notnull
'''
series2 = Series([1,2,3,4,np.nan,6,7,8])
print(series2.isnull())# 为空返回True
print(series2.notnull())# 不为空返回True

print('-'*20)
'''
Series及index的name属性
'''
print(series2)
series.name = 'ProductNums'
series.index.name = 'ProductType'
print(series2)