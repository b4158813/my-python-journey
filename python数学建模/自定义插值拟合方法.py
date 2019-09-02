import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示汉字的操作
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号的操作


# 自定义函数形式(自变量,*参数)
def func(x, a, b):
    # return b/(1+(b/12.53-1)*np.exp(-a*b*(x-1999)))
    return a * x + b


# 输入需要拟合的x、y数据
x = np.array([4.3982,6.9115,9.0059,10.2625,12.7758])
y = np.array([4.1888,7.1209,9.4248,10.8909,11.9381])

# 拟合方法：
# bounds设定参数的边界值
popt, pcov = curve_fit(func, x, y)  # bounds=((0,0),(0,2))

a = popt[0]  # popt得出第一个参数的值
b = popt[1]  # popt得出第二个参数的值
# c = popt[2]  # poot得出第三个参数的值
yvals = func(x, a, b)  # 拟合出x对应的y值
print('系数a：', a)
print('系数b：', b)
# print('系数c：', c)

# 作图
plot1 = plt.plot(x, y, label='原始数据',marker='o')
plot2 = plt.plot(x, yvals, linestyle='--', label='拟合曲线', color='red')
plt.xlabel('手摇角速度/(rad/s)',fontsize=15)
plt.ylabel('电动马达角速度/(rad/s)',fontsize=15)
plt.legend()
plt.show()

# 预测（你想要的x，参数a，参数b，。。。）
# print(func(2019,a,b))
