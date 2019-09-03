'''
散点图
正相关 负相关 不相关
实例：
'''
import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt

'''
身高-体重 散点图
'''
height = [161,170,182,175,173,165]
weight = [50,58,80,70,69,55]

#plt.scatter(height,weight)

#plt.show()

'''
案例3 负相关
'''
N = 100
x = np.random.randn(N)
y1 = -x + np.random.randn(N)*0.5
#plt.scatter(x,y1)


'''
外观调整
    c 颜色 默认蓝色
    s 点大小（面积） 默认20
    marker 点的形状 默认圆点
    alpha 透明度 0（透明）~1（不透明）变化 默认1
    edgecolors 边缘颜色 默认none
'''
plt.scatter(x,y1,s=100,c=['r','b','y'],marker='<',alpha=0.5,edgecolors='red')


plt.show()


