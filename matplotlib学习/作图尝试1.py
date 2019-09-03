import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.arange(0,100) # 产生一个0~100的列表赋值给x
fig, ax = plt.subplots(2,2) # 初始化一个figure框，并划分子图（2*2）
#ax.set_xlim(0,10)
#ax.set_ylim(-1.1,1.1)
plt.xlim(0,20)

ax1 = ax[0,0]
ax2 = ax[0,1]
ax3 = ax[1,0]
ax4 = ax[1,1] # 初始化四个图表对象，并分配到四个子图中
ax1.grid() # 加入网格，不传参默认为黑色细实线

#作图：
ax1.plot(x,x) # 一次函数
ax2.plot(x,x**2) # 二次函数
ax3.plot(x,np.exp(x)) # 指数函数
ax4.plot(x,np.sin(x)) # 正弦函数





plt.show # 将图片显示出来的函数
