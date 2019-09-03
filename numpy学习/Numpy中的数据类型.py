'''
数据类型
'''

import numpy as np

arr = np.arange(2,10,2)
print(arr)
print(arr.dtype)

arr2 = arr.astype(np.float)# astype方法：把arr变成(浮点)型
print(arr2)
print(arr2.dtype)

arr3 = arr.astype('|U2')# 使用unicode编码，每个元素长度为2
print(arr3)
print(arr3.dtype)

arr4 = arr.astype('|S2')# 使用String进行编码（十六进制编码），每个元素长度为2
print(arr4)
print(arr4.dtype)

arr5 = np.array([1,2,3,'4'],dtype=np.float)# 这是可以的（把‘4’字符串变成float型）
print(arr5)

# arr6 = np.array([1,2,3,'a'],dtype=np.float) 这是错误的（a本身不是数字，不能变成float）

print(30*'-')
'''
rashape 改变array形状
'''
arr_1 = np.arange(20)# 生成0~20（不包括20）共20个数
arr_2 = arr_1.reshape((4,5))# 形状可变，元素总数不可变
print(arr_2)
print(arr_1)

'''
reshape 函数不会改变原来的ndarray，但是得到的新的ndarray是原数组的 视图

视图：多个变量使用（指向）同一个内存地址（空间）
副本：把原来的内容重新复制（拷贝）了一份，放到新的内存地址

【视图互相影响，副本互不影响】

对于ndarray的一些方法操作，手想要区分是否会改变原来的变量，以此来判断是视图还是副本
'''
arr_2[0][4] = 19# arr_2是arr_1的视图
print(arr_2)

arr_3 = arr_2.copy()# arr_3是arr_2的副本
arr_3[0][4]=1000
print(arr_3)
print(arr_2)



