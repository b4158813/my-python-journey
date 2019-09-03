import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def dfunc(z,t):
    x,y = z
    return [t,abs(20*np.cos(3*t))]

def solve_ode():
    t = np.linspace(0,10,1000)
    z0=[0,0]
    z = odeint(dfunc,z0,t)

    plt.plot(z[:,0],z[:,1],label='track')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(linestyle='--',color='grey',alpha=0.5)
    plt.legend()
    plt.show()

solve_ode()