'''
n维数组(ndarray)
'''
import numpy as np

arr = np.array([[1,2,3,4],[2,3,4,5]])

print(arr)
print(arr.ndim)# 多维数组的维度

print(arr.shape)# 多维数组的形状

print(arr.size)# 多维数组元素个数

print(arr.dtype)# 多维数组的数据类型

arr2 = np.array([['1','2','3','4']],dtype=np.int32)# dtype 数组数据类型
print(arr2)

arr3 = np.array(['Python','cctv','baidu','hello world'],dtype='|S4')# 字符串 且只保留四位
print(arr3)


