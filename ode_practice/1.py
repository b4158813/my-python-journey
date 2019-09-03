import numpy as np
from sympy import symbols,dsolve,diff,pprint,E
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dfunc(y,x):
	return (np.e**(x+1)-y)/(x+1)

def solve_ode_draw():
	x = np.linspace(0,4,1000)
	y0 = [2*np.e]
	y = odeint(dfunc,y0,x)

	plt.plot(x+1,y,label='y_numerical',linestyle='-.')
	plt.legend()


def solve():
	x = symbols('x')
	y = symbols('y')(x)
	ans = dsolve(x*y.diff(x)+y-E**(x),y)
	pprint(ans)

def draw_ana():
	x = np.linspace(1,5,1000)
	y = (np.e**(x)+np.e)/x
	plt.plot(x,y,label='y_analysis',linestyle='--')
	plt.legend()
	
solve()
solve_ode_draw()
draw_ana()
plt.grid(linestyle='--',color='grey',alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y_numerical&analysis solution compare')
plt.show()