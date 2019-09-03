'''
条形图
    分析比较多个项目分类的数据大小
    用于较小的数据集分析
    如：不同季度的销量，不同国家的人口等
'''
import numpy as np
import matplotlib.pyplot as plt


'''
x        每个柱x轴左边界
bottom      每个柱y轴下边界
height      柱高度(Y轴方向) 
width       柱宽度(X轴方向)
以上参数可以设置为数值或者list

orientation   条形图方向

'''
N = 5
y = [20,10,30,25,15]

index = np.arange(N)
p1 = plt.bar(x=0, bottom=index, height=0.5, color='red', width=y, orientation='horizontal')
#也可直接用barh函数画
plt.show()