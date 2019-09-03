'''
copy & deep copy
'''
import numpy as np

a = np.array([1,2,3,4])
b = a
c = a
d = b
a[0]=11
print(b is a)
print(c is a)
print(d is a)
# 赋值ndarray是一个视图
b = a.copy()# deep copy 深拷贝，这是一个副本
a[3] = 44
print(b is a)