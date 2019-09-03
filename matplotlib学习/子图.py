'''
Matplotlib对象简介
	FigureCanvas
	Figure
	Axes
'''

'''
fig=plt.figure()
	Figure实例
	可以添加Axes实例

ax=fig.add_subplot(111)
	返回Axes实例
	参数1：子图总行数
	参数2：子图总列数
	参数3：子图位置
'''

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,100)

fig=plt.figure()

ax1=fig.add_subplot(221)
ax1.plot(x,x)

ax2=fig.add_subplot(222)
ax2.plot(x,-x)

ax3=fig.add_subplot(223)
ax3.plot(x,x**2)

ax4=fig.add_subplot(224)
ax4.plot(x,np.log(x))
