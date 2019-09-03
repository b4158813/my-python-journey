import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示汉字的操作
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号的操作

omega_e = [3.5103, 5.6549, 7.3304, 8.7965, 12.1475]

x = np.array([3.1416, 5.2360, 7.5398, 9.2153, 12.5664])
y = 0.957 * x + 0.418

plt.plot(x, omega_e, marker='x', label='实际情况')
plt.plot(x, y, marker='o',linestyle='--',label='拟合直线')
plt.xlabel('手摇电机角速度/(rad/s)',fontsize=15)
plt.ylabel('电动马达角速度/(rad/s)',fontsize=15)
plt.legend()
plt.show()
