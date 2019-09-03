'''
直方图
    表示数据分布情况
    如：某年级同学的升高分布情况
    类别通常是是自定义 连续的
'''


'''
data:必选参数，绘图数据
bins:直方图的长条形数目，可选项，默认为10
normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
facecolor:长条形的颜色
edgecolor:长条形边框的颜色
alpha:透明度
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
'''
mu = 100
sigma = 20
x = mu+sigma*np.random.randn(20000)

plt.hist(x,bins=100,color='green',edgecolor='black', normed=False)

plt.show()
'''

'''
2-D直方图
    分析双变量联合分布
'''
'''
a = np.random.randn(1000)+2
b = np.random.randn(1000)+3
plt.hist2d(a,b,bins=50)

plt.show()
'''

a = 10+np.sqrt(3)*np.random.randn(2000)
plt.hist(a,bins=50,normed=False,edgecolor='black',alpha = 0.6,facecolor='pink')

plt.show()