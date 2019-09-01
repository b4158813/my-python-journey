import numpy as np
from CALCULATE_ALL import Solution
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示汉字的操作
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号的操作

solution1 = Solution()
# t1 p1不变，改变p2
nt_1 = solution1.calculate_1(3331.22, 2136.79, 151.95)
nt_2 = solution1.calculate_1(3331.22, 2198.08, 151.95)
nt_3 = solution1.calculate_1(3331.22, 2413.47, 151.95)
nt_4 = solution1.calculate_1(3331.22, 2518.49, 151.95)

print(nt_1)
print(nt_2)
print(nt_3)
print(nt_4)

nt_1 = eval(str(nt_1)[:-1])
nt_2 = eval(str(nt_2)[:-1])
nt_3 = eval(str(nt_3)[:-1])
nt_4 = eval(str(nt_4)[:-1])

p2 = [0.006, 0.01, 0.05, 0.1]
nt_list = [nt_1, nt_2, nt_3, nt_4]
plt.plot(p2, nt_list, marker='o')
plt.title('T1、P1不变时，ηt随终压变化曲线', fontsize=15)
plt.xlabel('终压P2/MPa', fontsize=15)
plt.ylabel('朗肯循环热效率ηt/%', fontsize=15)
plt.xlim(0, 0.12)
plt.ylim(25, 40)
plt.text(0.07, 35, 'T1=450℃\nP1=4MPa', fontsize=20, color='g')
plt.grid(linestyle='--', color='grey', alpha=0.5)
plt.legend()
plt.show()
