import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint, solve_bvp, solve_ivp
import numpy as np
import seaborn as sns

# sns.set()


def dyfunc(y, t):
    '''
    要把y看出一个向量，y = [dy0,dy1,dy2,...]分别表示y的n阶导
    对于二阶微分方程，肯定是由0阶和1阶函数组合而成的，所以下面把y
    看成向量的话，y0表示最初始的函数，也就是我们要求解的函数，y1表示
    一阶导，对于高阶微分方程也可以以此类推
    '''
    y_o, y1 = y
    # 注意返回的顺序是[一阶导， 二阶导]，这就形成了一阶微分方程组
    dydt = [y1, 2 * y1 - 2 * y_o + np.e ** (2 * t) * np.sin(t)]
    return dydt


def solve_second_ode():
    t = np.linspace(0, 1, 1000)  # x范围
    y0 = [-0.4, -0.6]  # 初值[-0.4，-0.6]表示y(0)=-0.4,y'(0)=-0.6
    y = odeint(dyfunc, y0, t)

    # 返回y，其中y[:,0]是y[0]的值，就是最终解，y[:,1]是y'(x)的值
    l1, = plt.plot(t, y[:, 1], label='y\'')
    l2, = plt.plot(t, y[:, 0], label='y')
    plt.grid(linestyle='--',color='grey',alpha=0.5)
    plt.legend(fontsize=20,shadow=True)
    plt.show()


solve_second_ode()
