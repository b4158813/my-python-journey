import numpy as np
import matplotlib.pyplot as plt

'''
颜色表示方法
    八种默认颜色缩写
    灰色阴影
    html 十六进制（可以百度查询 颜色代码）
    RGB元组
    
样式
    颜色 color
    线条 linestyle
    点形状 marker
'''
y = np.arange(1,5)
#指定marker会画出线段
plt.plot(y,color='g',marker='o',linestyle='--')

plt.plot(y+1,marker='>',linestyle='-.')

plt.plot(y+2,color='#FF00FF',linestyle=':')

plt.plot(y+3,color=(0.1,0.2,0.3),linestyle='-')

plt.show()



