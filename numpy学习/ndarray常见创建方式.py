'''
zeros函数
    填充0，维度定义使用元组

ones函数
    填充1

empty函数
    填充随机值
'''

import numpy as np

arr1 = np.zeros((3,4))# 第一个维度为3，第二个维度为4,注意定义使用元组
arr2 = np.ones((5,6,2),dtype=np.int32)
arr3 = np.empty((7,4))# 七行四列随机值(十分接近0）
print(arr1)
print(arr2)
print(arr3)

'''
NAN空值（缺失值）
'''

print(30*'-')

'''
arange函数（ 类似于range() ）
range(2,20,3) # 从2开始，到20结束，包头不包尾，步长3,共（20-2）/3 = 6 个数据
arange(2,20,3) # 同上
'''

arr4 = np.arange(2,20,3)
print(arr4)

'''
linspace函数 生成一个等差数列
linspace(2,20,3) # 从2开始，到20结束，包头包尾，共3个数据
'''
arr5 = np.linspace(2,20,3)# 公差为（20-2）/（3-1）= 9
print(arr5)
arr5_1 = np.linspace(2,20,3,endpoint=False)# 此处不包尾，公差为 (20-2)/(4-1) = 6
print(arr5_1)

'''
logspace函数 生成一个等比数列
logspace(2,20,3) # 第一个值代表10的2次方，第二个值代表10的20次方，第三个值代表数据个数
'''
arr6 = np.logspace(2,20,3)# 公比为10^((20-1)/(3-1))=10^9
print(arr6)

'''
reshape方法
'''
arr7 = np.arange(2,20,2).reshape((3,3))# 把自定的多维数组重整成3*3的数组
print(arr7)
arr7_1 = np.arange(2,20,2).reshape((3,-1))# 重整成三行的数组,-1是自动计算维度值
print(arr7_1)

'''
random随机数生成方法（生成0~1的随机数）
（实际调用random.random_sample() 生成每一位随机数的方法）
'''
arr8 = np.random.random((2,3,4))
print(arr8)
arr9 = np.random.random_sample((2,3))# 同上
print(arr9)









