'''
Pandas常用操作
'''
import numpy as np
import pandas as pd
from pandas import DataFrame,Series

a = DataFrame({'C++':[50,50,20], 'Java':[20,30,40], 'Vb':[10,20,30]})
print(a,'\n')
a.index = [2,3,4]# 通过index对象更改属性值
print(a,'\n')
a.columns = ['Java','C','Vb']
print(a,'\n')

a['C'] = np.nan# 修改一列的数据
print(a,'\n')

'''
头部、尾部、快速统计
'''
print(20*'-')
b = DataFrame(np.random.randint(1,100,(20,6)))
print(b,'\n')
print(b.head(2),'\n')# 前2行数据（不填为前5行数据）
print(b.tail(3),'\n')# 后三行数据（不填为后5行数据）
print(b.describe(),'\n')# 快速统计汇总
print(b.T.describe(),'\n')# 转置后快速统计

print(20*'-')
'''
排序
    axis，0行，1列
    ascending默认True升序，False则为降序
'''
print(b.sort_index(axis=1, ascending=False),'\n')# 按轴排序，列轴降序排序
print(b.sort_values(by=0))# 按值排序,按0轴的值从小到大排序

print(20*'-')
'''
按照标签获取一个交叉的区域
    loc方法：先行后列,切片时包头包尾
'''
print(b,'\n')
print(b.loc[[0,2,4,6],:],'\n')# 取0，2，4，6行的所有内容
print(b.loc[0:3,[0,2,4,6]],'\n')# 标签切片取0~3行且是0，2，4，6列的值

c = DataFrame(np.random.randint(1,100,(6,6)),columns=['a','b','c','d','e','f'])
print(c,'\n')
print(c.loc[0,'a'],'\n')# 0行a列
print(c['a'][0])# 同上（a列0行）


'''
通过位置选择
    iloc方法：先行后列，输入位置，与标签无关,切片时包头不包尾
    iat方法：快速获取指定位置的数据
'''
print(c.iloc[0,3:5])
print(c.iat[2,2])# 获取第三行第三列的值

print(20*'-')
'''
bool索引
'''
print(c,'\n')
print(c[c.a>50],'\n')# 过滤出第a列数据大于50的数据
print(c[c>50],'\n')# 把所有不满足条件的置空


print(20*'-')
'''
过滤操作
'''
d = c.copy()
d['g'] = [1,2,3,4,5,6]# 添加第g列数据
print(d,'\n')
print(d[d['g'].isin([1,4])], '\n')# 把第g列数据为1和4的两行提取出来

print(20*'-')
'''
新增一个列
'''
e = Series([i for i in range(6)])
print(e,'\n')
d['h'] = e# 设置添加第h行的数据
print(d,'\n')
d.loc[5,'h'] = 123# 通过标签更改数据
d.iloc[4,7] = 321
print(d,'\n')
d[d>50] = 0# 把大于50的数据都变为0
print(d)
