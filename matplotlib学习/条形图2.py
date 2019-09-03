import numpy as np
import matplotlib.pyplot as plt

index = np.arange(4)

sales_BJ = [52, 55, 63, 53]
sales_SH = [44, 66, 55, 41]

bar_width = 0.3

plt.bar(index, sales_BJ, bar_width, color='b')
# plt.bar(index+bar_width,sales_SH,bar_width,color='r')
plt.bar(index, sales_SH, bar_width, color='r', bottom=sales_BJ)
plt.show()

'''
# 作业
a = np.random.randint(0,50,5)
b = np.random.randint(0,50,5)
axis = np.arange(5)
height = 0.3
print(a,b)
plt.bar(x=0,bottom=axis,height=height,width=a,color='red',orientation='horizontal')
plt.bar(x=a,bottom=axis,height=height,width=b,color='blue',orientation='horizontal')

plt.show()
'''
