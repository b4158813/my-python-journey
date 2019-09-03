'''
三元表达式
    eg.
    if 2>3
    else 0
'''
import numpy as np

xarr = np.array([1.1,2.2,3.3,4.4])
yarr = np.array([1.2,2.3,3.4,4.5])
bool_arr = np.array([True,False,False,True])
#满足True显示第一个数组中元素，否则显示第二个数组中元素
c_arr = np.c_[xarr,yarr,bool_arr]
print("c_arr = %s"%c_arr,'\n')
result = ['%.1f'%x if bl else '%.1f'%y for x,y,bl in c_arr]
print(result)# 输出一个列表

'''
改编三元表达式
'''
result1 = ['%.1f'%x if bl else '%.1f'%y for x,y,bl in c_arr if x>2 if x<3]
print(result1)
print(30*'-')
'''
np.where函数方法（实现数据过滤操作）
    np.where(表达式数组，当前表达式为True提取数的数组，当前表达式为False提取数据的数组)
'''
print(np.where(bool_arr, xarr, yarr))# 得出同样的结果，输出一个数组















