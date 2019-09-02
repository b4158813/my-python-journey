import pandas as pd
from pandas import DataFrame,Series
import numpy as np
'''
merging two df by key/kyes.(may be used in database)

simple example
'''
left = DataFrame({'key':['K0','K1','K2','K3'],
                  'A':['A0','A1','A2','A3'],
                  'B':['B0','B1','B2','B3']})
right = DataFrame({'key':['K0','K1','K2','K3'],
                  'C':['C0','C1','C2','C3'],
                  'D':['D0','D1','D2','D3']})
print(left)
print(right)

res = pd.merge(left,right,on='key')
print(res,'\n')

print(20*'-')
'''
merging two df by key/kyes.(may be used in database)

consider two keys

indicator: 显示出合并方式
'''
left1 = DataFrame({'key1':['K0','K1','K2','K3'],
                   'key2':['K0','K1','K0','K1'],
                  'A':['A0','A1','A2','A3'],
                  'B':['B0','B1','B2','B3']})

right2 = DataFrame({'key1':['K0','K1','K2','K3'],
                   'key2':['K0','K0','K0','K0'],
                  'C':['C0','C1','C2','C3'],
                  'D':['D0','D1','D2','D3']})
print(left1)
print(right2)
res1 = pd.merge(left1,right2,on=['key1','key2'])
print(res1,'\n')# 默认how='inner' 即：只选出公共部分
# how: 'right' 'left' 'outer' 'inner'
res2 = pd.merge(left1,right2,on=['key1','key2'],how='outer')
#outer：把不是共同存在的数据置为nan
print(res2,'\n')
res3 = pd.merge(left1,right2,on=['key1','key2'],how='right')
# 基于right存在的on值进行合并
print(res3,'\n')
res4 = pd.merge(left1,right2,on=['key1','key2'],how='left',indicator='indicator_column')
# 同上（基于left）
# indicator 默认为False，可自定义名称
print(res4,'\n')


print(20*'-')

'''
merging two df by key/kyes.(may be used in database)

based on index
默认inner
'''
left3 = DataFrame({'key':['K0','K1','K2','K3'],
                  'A':['A0','A1','A2','A3'],
                  'B':['B0','B1','B2','B3']},
                  index=['A','B','C','D'])
right4 = DataFrame({'key':['K0','K1','K2','K3'],
                  'C':['C0','C1','C2','C3'],
                  'D':['D0','D1','D2','D3']},
                  index=['B','C','D','E'])

res_1 = pd.merge(left3,right4,left_index=True,right_index=True,how='outer')
print(res_1)


print(20*'-')
'''
merging two df by key/kyes.(may be used in database)

handle overlapping
'''
boys = DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls = DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})
print(boys)
print(girls)
res5 = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')
# suffixes 添加标签特征
print(res5)




