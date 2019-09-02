'''
Series索引取值
    切片索引都是 视图
'''
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

series = Series([1,2,3,4],index=['wlx','yl','wxy','xzy'])
print(series)
print(series['wlx'], '\n')
print(series['wlx':'wxy'])# 包头包尾

