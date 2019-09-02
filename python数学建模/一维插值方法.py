import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.arange(37, 43.5, 0.5)
# x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
y = np.array([3.4, 3, 3, 2.27, 2.1, 1.83, 1.53, 1.7, 1.8, 1.9, 2.35, 2.54, 2.9])
xnew = np.linspace(37, 43, 101)
plt.plot(x, y, "ro")

# for kind in ["nearest", "zero", "slinear", "quadratic", "cubic"]:  # 插值方式
for kind in ['cubic']:
    # "nearest","zero"为阶梯插值
    # slinear 线性插值
    # "quadratic","cubic" 为2阶、3阶B样条曲线插值
    f = interpolate.interp1d(x, y, kind=kind)
    # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
    ynew = f(xnew)
    plt.plot(xnew, ynew, label=str(kind))
plt.legend(loc="lower left", fontsize=15)
plt.tick_params(labelsize=10)
plt.show()
