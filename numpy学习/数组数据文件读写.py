'''
数组以二进制格式读写
'''
import numpy as np

arr = np.random.randint(1,100,(3,3))
np.save('data',arr)# 保存：自动添加后缀.npy（二进制文件）
arr2 = np.load('data.npy')# 读取：需要设置文件后缀

print(30*'-')
'''
存取文本文件
    np.loadtxt
    #fname 文件名
    #dtype 数据类型
    #comments 注释行符号的定义
    #delimiter 数据分隔符的定义
    #converters 转换函数
    #skiprows 跳过行数
    #usecols 使用的哪些列
'''

arr3 = np.loadtxt('example.csv',delimiter=',')#须定义分隔符 否则会报错
print(arr3,'\n')
arr4 = np.genfromtxt('example.csv',delimiter=',')# 类似于loadtxt


from io import StringIO
c = StringIO('0 1\n2 3')# 定义一个数据流
print(np.loadtxt(c))


'''
数据写入文本文件
    注意 分隔符
'''
arr5 = np.arange(0,36,dtype=np.float)
np.savetxt('arr.csv',arr5.reshape((9,4)),delimiter=',',fmt='%d')
print(np.loadtxt('arr.csv',delimiter=','))

print(10*'-')
# 如果数组为二维以上的数组，则必须转换为二维数组才能进行存储
arr_1 = np.random.randint(1,100,(3,3,3))
arr_1_save = np.savetxt('arr_1.csv',arr_1.reshape((9,3)),delimiter=',',fmt='%d')
print(arr_1,'\n')
print(np.loadtxt('arr_1.csv',delimiter=','))













