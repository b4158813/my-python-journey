import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示汉字的操作
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号的操作

omega=['461.1512','497.678','500.154']
theta_t=[66.442,66.44,64.592]
theta_r=[-64.2,-64.5,-64.3]
theta_r=[64.2,64.5,64.3]
error=[-3.374,-2.920,-3.442]

plt.bar(omega,theta_t,width=0.5)
plt.bar(omega,theta_r,width=0.5)
plt.plot(omega,error,linestyle='--',marker='o',label='相对误差/%')
plt.plot(omega,theta_r,marker='o',label='实际曲线')
plt.plot(omega,theta_t,marker='x',label='理论曲线')

# for a,b in zip(omega,theta_t):
#     plt.text(a, b, '%.3f' % b, ha='center', va='bottom', fontsize=15)
# for a, b in zip(omega, theta_r):
#         plt.text(a, b, '%.1f' % b , ha='center', va='bottom', fontsize=15)
for a,b in zip(omega,error):
    plt.text(a, b, '%.3f' % b+'%', ha='center', va='bottom', fontsize=15)

plt.xlabel('角速度Ω/(rad/s)',fontsize=15)
plt.ylabel('θ/°',fontsize=15)
plt.tick_params(labelsize=15)
plt.legend()
plt.show()