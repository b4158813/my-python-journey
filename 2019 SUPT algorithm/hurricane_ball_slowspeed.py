import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示汉字的操作
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号的操作

omega = [62.3641, 53.4739, 46.8021,41.6795, 46.7986, 50.4552, 54.4187, 60.8718, 55.9450, 45.3922,
         46.8021, 43.1893, 62.8130, 44.1142, 50.0812, 48.8736, 51.4551]
theta_t = [76.989, 80.668, 84.864, 89.512, 84.867, 82.366, 80.192, 77.499, 79.472, 85.990, 84.864, 87.971, 76.842,
           87.103, 82.597, 83.380, 81.771]
theta_r = [-76.2, -79.6, -85.2, -87.8, -83.4, -81.0, -78.7, -79.7, -81.1, -85.4, -85.9, -88.6, -79.1, -87.5, -81.1,
           -84.7, -78.0]
theta_r = [76.2, 79.6, 85.2, 87.8, 83.4, 81.0, 78.7, 79.7, 81.1, 85.4, 85.9, 88.6, 79.1, 87.5, 81.1, 84.7, 78.0]

error = [-1.025, -1.324, 0.396, -1.913, 1.761, -1.677, -1.877, 2.825, 2.104, -0.671, 1.172, 0.702, 2.896, 0.464, -1.825,
         1.579, -4.589]

# plt.bar(omega, theta_t, width=0.3)
# plt.bar(omega, theta_r, width=0.3, alpha=0.5)
plt.plot(omega, error, linestyle='--', marker='o', label='相对误差/%')
# plt.plot(omega, theta_r, marker='o', label='实际曲线')
# plt.plot(omega, theta_t, marker='x', label='理论曲线')
# for a,b in zip(omega,theta_t):
#     plt.text(a, b, '%.3f' % b, ha='center', va='bottom', fontsize=15)
# for a, b in zip(omega, theta_r):
#     plt.text(a, b, '%.1f' % -b , ha='center', va='bottom', fontsize=15)
for a, b in zip(omega, error):
    plt.text(a, b, '%.3f' % b + '%', ha='center', va='bottom', fontsize=15)

plt.xlabel('角速度Ω/(rad/s)', fontsize=15)
plt.ylabel('θ/°', fontsize=15)
plt.tick_params(labelsize=15)
plt.legend(fontsize=15)
plt.show()
