'''
ndarray分割方法
'''
import numpy as np

a = np.arange(12).reshape((3,4))
print(a)
print(np.split(a,2,axis=1))# 按列分割
print(np.split(a,3,axis=0))# 按行分割
print(np.array_split(a,3,axis=1))# 不均等分割方法
print(np.vsplit(a,3))# 等价于axis=0按行分割
print(np.hsplit(a,2))# 等价于axis=1按列分割

