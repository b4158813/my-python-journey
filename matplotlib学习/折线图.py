'''
折线图
    主要反映数据随时间变化的关系
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates #
'''
x = np.linspace(-10,10,5)
y = x**2

plt.plot(x,y)# plot默认为折线图

plt.show()
'''

'''
sin函数图像
'''
x = np.linspace(0,10,100)
y = np.sin(x)

plt.plot(x,y)
plt.show()


