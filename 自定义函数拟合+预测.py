import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif']=['SimHei'] #正常显示汉字的操作
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号的操作

#自定义函数形式(自变量,*参数)
def func(x,a,b):
    return b/(1+(b/12.53-1)*np.exp(-a*b*(x-1999)))

#输入需要拟合的x、y数据
x=np.arange(1999,2018)
y=np.array([12.53,12.63,12.72,12.8,12.88,12.96,13.04,13.11,13.18,13.25,13.31,
            13.38,13.44,13.51,13.57,13.64,13.71,13.79,13.86])

#拟合方法：
#bounds设定参数的边界值
popt,pcov = curve_fit(func,x,y,bounds=((0,0),(1,20)))

a=popt[0]#popt得出第一个参数的值
b=popt[1]#popt得出第二个参数的值
yvals=func(x,a,b)#拟合出x对应的y值
print('系数a：',a)
print('系数b：',b)


#作图
plot1=plt.scatter(x,y,label='原始数据')
plot2=plt.plot(x,yvals,linestyle='--',label='拟合曲线',color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#预测（你想要的x，参数a，参数b，。。。）
print(func(2019,a,b))