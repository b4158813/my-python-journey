import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示汉字的操作
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号的操作
# sns.set()

omega = np.arange(40, -1, -1)
strip1 = np.array(
    [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 1, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0])
strip2 = np.array(
    [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0])

plt.bar(omega, strip1,color='r')
plt.bar(omega, strip2-strip1,color='b',bottom=strip1,alpha=0.5)
plt.xlabel('电阻箱阻值/Ω', fontsize=15)
plt.ylabel('边缘明暗条纹数量/个', fontsize=15)
plt.tick_params(labelsize=15)
plt.legend()
# for a, b in zip(omega, strip1):
#     plt.text(a, b, '%d个' % b, ha='center', va='bottom', fontsize=15)

plt.show()
