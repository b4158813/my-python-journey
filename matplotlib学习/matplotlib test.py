# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
axes1 = fig.add_subplot(111) # 参数349的意思是：将画布分割成3行4列，图像画在从左到右从上到下的第9块；111同理
line, = axes1.plot(np.random.rand(10))


# 因为update的参数是调用函数data_gen,所以第一个默认参数不能是framenum
def update(data):
    line.set_ydata(data)
    return line,


# 每次生成10个随机数据
def data_gen():
    while True:
        yield np.random.rand(10)


ani = animation.FuncAnimation(fig, update, data_gen, interval=2 * 1000)
plt.show()
