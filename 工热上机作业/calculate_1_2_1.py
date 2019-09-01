import numpy as np
from CALCULATE_ALL import Solution
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示汉字的操作
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号的操作

solution1 = Solution()
# p1 p2不变，改变初温
nt_300 = solution1.calculate_1(2962.0, 1959.0, 151.95)
nt_350 = solution1.calculate_1(3095.08, 2027.95, 151.95)
nt_400 = solution1.calculate_1(3215.71, 2085.58, 151.95)
nt_450 = solution1.calculate_1(3331.22, 2136.79, 151.95)
nt_500 = solution1.calculate_1(3444.99, 2183.85, 151.95)
nt_550 = solution1.calculate_1(3558.58, 2227.89, 151.95)
print(nt_300)
print(nt_350)
print(nt_400)
print(nt_450)
print(nt_500)
print(nt_550)
nt_300 = eval(str(nt_300)[:-1])
nt_350 = eval(str(nt_350)[:-1])
nt_400 = eval(str(nt_400)[:-1])
nt_450 = eval(str(nt_450)[:-1])
nt_500 = eval(str(nt_500)[:-1])
nt_550 = eval(str(nt_550)[:-1])

T = [300, 350, 400, 450, 500, 550]
nt_list = [nt_300, nt_350, nt_400, nt_450, nt_500, nt_550]
plt.plot(T, nt_list, marker='o')
plt.title('P1、P2不变时，ηt随初温变化曲线', fontsize=15)
plt.xlabel('初温T/℃', fontsize=15)
plt.ylabel('朗肯循环热效率ηt/%', fontsize=15)
plt.xlim(250, 600)
plt.ylim(35, 40)
plt.text(275, 38.75, 'P1=4MPa\nP2=6kPa', fontsize=20, color='g')
plt.grid(linestyle='--', color='grey', alpha=0.5)
plt.legend()
plt.show()
