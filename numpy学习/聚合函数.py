'''
聚合函数
    对一组值（比如一个数组）进行操作，返回一个单一值作为结果的函数

如： max、min、mean或average（平均值）、std（标准差）
    argmin、argmax、median（中位数）
'''
import numpy as np
arr = [[1,2,3,4],[3,4,5,6]]
print(arr, '\n')
print('arr_v_average = %s'%np.mean(arr, axis = 0))# 按列求平均值
print('arr_h_average = %s'%np.mean(arr,axis = 1))# 按行求平均值
print('arr_v_sum = %s'%np.sum(arr,axis = 0))# 按列求和
print('arr_h_sum = %s'%np.sum(arr,axis = 1))# 按行求和
print('arr_v_max = %s'%np.max(arr,axis = 0))# 按列取最大值
print('arr_v_std = %s'%np.std(arr,axis = 0))# 同上


