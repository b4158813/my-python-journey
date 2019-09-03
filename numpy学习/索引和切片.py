'''
数组的索引和切片
    注意：切片索引是 视图
'''

import numpy as np

arr = np.random.random((3,3))# 创建一个3*3随机矩阵
print('arr={0}\n'.format(arr))
print(arr[1][0:2])# 取出第二行 前两个数据

arr2 = np.random.randint(1,100,(3,3,3))

print('arr2 = {0}'.format(arr2))
print(arr2[0])
print(arr2[0, 0, 0])
print(arr2[0, 0:, 1:])# 这是我们想要的（通常情况的切片） 注意与下面不同
print(arr2[0][0:][1:])
# 这个是先进入arr2[0]（记为a） 再进入a的[0:]（记为b） 再进入b的[1:]（记为c） 得到的是c
# 可以理解为：每次都是按一维机制运作（只看第几行）

print(20*'-')

'''
布尔索引（筛选作用）
'''
print(arr2>0.3)# 满足条件的输出True，不满足的输出False
print(arr[arr>0.3],'\n')# True位置上的数据取出来 组成新的数组

arr3 = np.array(['Tom','Alice','Python'])
print(arr3)
arr3[arr3 == 'Tom'] = 1# 把'Tom'替换为1
print(arr3, '\n')

arr4 = np.array(['Tom','Alice','Python',np.nan])
print(arr4)
arr4[arr4 == 'nan'] = '1'# 把'nan'值替换为1
print(arr4, '\n')


print(20*"-")
'''
花式索引
    前一个取出行，后一个按位取出对应列
    与索引器不同
    
索引器
'''
arr_new = np.arange(32).reshape((8,4))
print(arr_new, "\n")

print(arr_new[[0,3,5]], "\n")# 输出对应行
print(arr_new[[0,3,5],[0,3,2]],'\n')# 对应行取出列的元素 [0][0] [3][3] [5][2]

x= arr_new[np.ix_([0,3,5],[0,3,2])]# ix_生成一个索引器（用于取出特定行列的数据）
print(x)


print(30*'-')
'''
一些方法
'''
A = np.arange(12).reshape((3,4))
print(A,'\n')
for row in A:
    print(row)# 迭代每一行
print('打住')
for column in A.T:
    print(column)# 迭代每一列
for item in A.flat:# 把A转变成一行的序列
    print(item)# 迭代每一项
print('\n', A.flatten())