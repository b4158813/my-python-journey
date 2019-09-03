import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示汉字的操作
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号的操作
# sns.set()

omega = np.linspace(40, 0, 5)
diameter = np.array([5, 5, 7, 9, 9])

plt.bar(omega, diameter, width=4)
plt.xlabel('电阻箱阻值/Ω', fontsize=15)
plt.ylabel('光斑直径/cm', fontsize=15)
plt.tick_params(labelsize=15)
for a, b in zip(omega, diameter):
    plt.text(a, b, '%dcm' % b, ha='center', va='bottom', fontsize=15)

plt.show()
