'''
数组与标量、数组之间的运算
'''
import numpy as np

arr = np.arange(0,20,2)

print(arr+2)# 每一项+2

arr2 = np.arange(0,40,4)
print(arr+arr2)# 矩阵相加
print(arr-arr2)# 矩阵相减
print(arr*arr2)# 同类型每个元素相乘（元素级运算），并不是矩阵相乘
print(arr/arr2)# python2.x 需要引入__future__模块中的division 保证算数合法性

arr_1 = np.random.random((3,2))
arr_2 = np.random.random((2,3))
# print(arr_1+arr_2) 两个不同类型的矩阵不能相加减或元素级相乘 等

'''
矩阵相乘
    须满足矩阵相乘条件！
    行轴 axis[0]
    列轴 axis[1]
'''
arr_3 = arr_2.dot(arr_1)# dot方法 矩阵相乘
# 或 np.dot(arr_2,arr_1)
print('{0} * \n{1} = \n{2}'.format(arr_2,arr_1,arr_3))

print(10*'-'+'来看一个实例')

arr_new1 = np.array([[89,95,83],[79,75,77],[74,51,88]])
arr_new2 = np.array([[10,1],[6,10],[9,1]])
arr_multiply = np.dot(arr_new1,arr_new2)
print(arr_multiply)









