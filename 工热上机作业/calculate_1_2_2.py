import numpy as np
from CALCULATE_ALL import Solution
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示汉字的操作
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号的操作

solution1 = Solution()
# t1 p2不变，改变p1
nt_1mpa = solution1.calculate_1(3370.80, 2347.19, 151.95)
nt_2mpa = solution1.calculate_1(3357.83, 2244.16, 151.95)
nt_4mpa = solution1.calculate_1(3331.22, 2136.79, 151.95)
nt_6mpa = solution1.calculate_1(3303.45, 2070.01, 151.95)
nt_8mpa = solution1.calculate_1(3274.30, 2019.51, 151.95)
nt_10mpa = solution1.calculate_1(3243.63, 1977.62, 151.95)
print(nt_1mpa)
print(nt_2mpa)
print(nt_4mpa)
print(nt_6mpa)
print(nt_8mpa)
print(nt_10mpa)
nt_1mpa = eval(str(nt_1mpa)[:-1])
nt_2mpa = eval(str(nt_2mpa)[:-1])
nt_4mpa = eval(str(nt_4mpa)[:-1])
nt_6mpa = eval(str(nt_6mpa)[:-1])
nt_8mpa = eval(str(nt_8mpa)[:-1])
nt_10mpa = eval(str(nt_10mpa)[:-1])

T = [1, 2, 4, 6, 8, 10]
nt_list = [nt_1mpa, nt_2mpa, nt_4mpa, nt_6mpa, nt_8mpa, nt_10mpa]
plt.plot(T, nt_list, marker='o')
plt.title('T1、P2不变时，ηt随初压变化曲线', fontsize=15)
plt.xlabel('初压P1/MPa', fontsize=15)
plt.ylabel('朗肯循环热效率ηt/%', fontsize=15)
plt.xlim(0, 11)
plt.ylim(30, 45)
plt.text(0.5, 41.5, 'T1=450℃\nP2=6kPa', fontsize=20, color='g')
plt.grid(linestyle='--', color='grey', alpha=0.5)
plt.legend()
plt.show()
