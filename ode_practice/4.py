import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def dfunc(y, x):
    return -2 * y + 2 * x ** 2 + 2 * x


def solve_ode():
    x = np.linspace(0, 0.5, 1000)
    y0 = [1]
    y = odeint(dfunc,y0,x)

    plt.plot(x,y[:,0],label='y')
    plt.grid(linestyle='--',color='grey',alpha=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


solve_ode()
