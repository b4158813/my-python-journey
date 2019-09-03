'''
数组的转置与轴对换
'''
import numpy as np
'''
transpose函数 用于数组转置（二维数组行列互换）
数组的T属性也是转置

转置后得矩阵是一个 视图
'''
arr = np.arange(32).reshape((8,4))
print(arr)

print(arr.transpose(),'\n')# transpose函数实现转置
print(arr.T,'\n')# T属性实现转置


