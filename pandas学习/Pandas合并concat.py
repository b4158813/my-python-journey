'''
concatenating 合并
'''

import numpy as np
import pandas as pd
from pandas import DataFrame,Series

df1 = DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3,'\n')

res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
# 按照0轴合并,忽略掉index并重新排序
print(res)


print(20*'-')
'''
join,['inner','outer']
'''
df_1 = DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df_2 = DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print(df_1)
print(df_2)

res1 = pd.concat([df_1,df_2],join='outer')
# 默认outer处理模式：把不存在的部分置为nan
print(res1)
res2 = pd.concat([df_1,df_2],join='inner',ignore_index=True)
#inner处理模式：只选出共同存在的部分合并，不共同的元素忽略
print(res2)


print(20*'-')
'''
join_axes处理：
    以指定dataframe的index进行处理
'''
res3 = pd.concat([df_1,df_2],axis=1,join_axes=[df_1.index])
print(res3)


print('-'*20)
'''
append方法
'''
res4 = df_1.append(df_2,ignore_index=True)
print(res4)
s1 = Series([1,2,3,4],index=['a','b','c','d'])
res5 = df_1.append(s1,ignore_index=True)# 添加一个Series
print(res5)


