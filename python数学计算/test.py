from sympy import *
import matplotlib.pyplot as plt
import numpy as np

t=Symbol('t')
w0=Symbol('w0')
delta=Symbol('δ')
x=Function('f')(t)
#ans=integrate(sin(x*cos(x)),(x,0,pi))
# ans=Derivative(x*cos(a*x),a)

ans=dsolve(Eq(x.diff(t,t)+0.5*delta*x.diff(t)+w0**2),x)

print(ans)


#fig=plt.figure()
#ax=fig.add_subplot()

#ax.plot()
