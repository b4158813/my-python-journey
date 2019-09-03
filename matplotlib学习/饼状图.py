'''
饼状图
    显示一个数据系列中各项的大小与各项总和的比例
    数据点显示为整个饼状图的百分比
'''

import matplotlib.pyplot as plt

labels = 'A','B','C','D'
fracs = [15,30,45,10]

explode = [0,0.05,0.08,0]

plt.axes(aspect=1) #将x与y轴比例设置为1:1

plt.pie(x=fracs, labels=labels, autopct='%.0f%%',explode=explode,shadow=True)

plt.show()




