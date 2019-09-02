'''
DataFrame数据框
'''
import numpy as np
import pandas as pd
from pandas import DataFrame,Series

df01 = DataFrame([['Tom','Merry','John'],[76,98,100]])
print(df01,'\n')
df02 = DataFrame([['Tom',76],['Merry',98],['John',100]])
print(df02)

'''
属性 索引和切片
'''
print(20*'-')
df = DataFrame([[1,2,3],[4,5,6]], index=['a', 'b'], columns=['c', 'd', 'e'])
print(df)
print(df['c']['a'])# 取出第'c'列，第'a'行的数据
print(df[1:])# 如果使用切片，那么从行开始取值
print(df.index)# 注意：这里index和columns为对象，可以更改属性值
print(df.columns)
print(df.values)

print(20*'-')
'''
通过字典定义DataFrame
    （一列一列输入数据）
'''
a = DataFrame({'wlx':[100,98,99],'wxy':[97,98,96],'yl':[99,95,90]})
print(a)