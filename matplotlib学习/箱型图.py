'''
箱型图
    显示一组数据分散情况的统计图
    上边缘、上四分位数、中位数、下四分位数、下边缘、异常值
'''

import numpy as np
import matplotlib.pyplot as plt


np.random.seed(100)

data = np.random.normal(size=(1000,4),loc=0,scale=1)

#plt.boxplot(data,sym='o',whis=1.5)#

labels=['A','B','C','D']
plt.boxplot(data,labels=labels)
plt.show()



