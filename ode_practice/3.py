import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def dfunc(z, t):
    x, y = z
    dxdt = np.e ** t - 5 * x - y
    dydt = x + 3 * y
    return [dxdt, dydt]


def solve_ode():
    t = np.linspace(0, 1, 1000)
    z0 = [1.,0.]
    z = odeint(dfunc, z0, t)

    plt.plot(z[:, 0], z[:,1], label='track_pic')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(linestyle='--', color='grey', alpha=0.5)
    plt.show()


solve_ode()
