import numpy as np
from sympy import dsolve, symbols, diff, pprint
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def solve_ode_analysis():
    t = symbols('t')
    y = symbols('y')(t)
    ans = dsolve(y.diff(t) + y - t - 1, y)
    pprint(ans)


def draw_analysis():
    t = np.linspace(0, 10, 1000)
    y = (1 + t * np.e ** (t)) * np.e ** (-t)
    plt.plot(t, y,linestyle='-.', label='analysis_solution')


def func(y, t):
    return -y + t + 1


def solve_ode():
    t = np.linspace(0, 10, 1000)
    y0 = [1]
    y = odeint(func, y0, t)

    plt.plot(t, y, linestyle='--', label='numerical_solution')
    plt.grid(linestyle='--', color='grey', alpha=0.5)
    plt.legend(loc='upper left')
    plt.show()


solve_ode_analysis()
draw_analysis()
solve_ode()
plt.xlabel('x')
plt.ylabel('y')
plt.title('y_numerical&analysis_solution_comparison')
plt.show()
