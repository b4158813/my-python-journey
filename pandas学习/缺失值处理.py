'''
缺失值处理
'''

import numpy as np
import pandas as pd
from pandas import DataFrame,Series

'''
reindex方法
    可以对指定轴上的索引进行修改（增加/删除）
'''
a = DataFrame(np.random.randint(1,100,(6,6)))
b = a.reindex(index=[i for i in range(3)],columns=list(a.columns))
print(a,'\n')
print(b,'\n')


print(20*'-')
'''
dropna方法去除包含缺失值的行
fillna方法更改缺失值的值
    并没有更改原来数据
'''
b.iloc[0]=np.nan
print(b,'\n')
print(b.dropna(axis=0, how='any'))# how='any','all' ,axis=0删除行，axis=1删除列
print(b.fillna(value=0))


print(20*'-')
'''
对数据进行布尔填充，用于空值判断
'''
print(pd.isnull(b))



