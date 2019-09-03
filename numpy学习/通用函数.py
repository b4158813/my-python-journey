'''
通用函数
-常见通用函数：
    abs,fabs 计算绝对值
    sqrt 计算x算数平方根
    square 计算x平方
    exp 计算e的x次方
    log,log10,log2,log1p 计算对数（自然、常用、2为低）
    sign 计算各元素正负号
    ceil 计算大于等于该值得最小整数
    floor 计算小于等于该值得最大整数
    rint 四舍五入到最近整数
    add 等于两矩阵相加
    等等……
'''
import numpy as np

arr = np.random.randint(-50,50,(2,3,4))
print('arr = %s'%(arr),'\n')

arr_fabs = np.fabs(arr)# 算绝对值，也可用abs（较慢，但可计算复数）
print('arr_fabs = %s'%arr_fabs,'\n')

arr1 = np.random.randint(0,4,(2,3,4))
print('arr1 = %s'%arr1,'\n')
arr_power = np.power(arr,arr1)# x的y次方
print('arr^arr1 = %s'%arr_power,'\n')

arr2 = np.empty((2,2,2))
arr2[1,1] = np.nan
print('arr2 = %s'%arr2)
print(np.isnan(arr2))# 判断数组是否具备nan值


print(30*'-')
a = np.arange(14,2,-1).reshape((3,4))
print(a)
print(np.cumsum(a))# 输出指定斐波那契数列形式的数列
print(np.diff(a))# 输出每两个相邻数只差组成的矩阵(后-前）
print(np.nonzero(a))# 输出非零元素的下标
print(np.sort(a))# 每行进行从小到大排序
print(np.clip(a,5,9))# 所有<5的数变成5，>9的数变成9，保留之间的数






