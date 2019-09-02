from sympy import *

t=Symbol('t')
P=Function('P')(t)
a=Symbol('a',positive=True)
b=Symbol('b',positive=True)
C1=Symbol('C1')
P0=Symbol('P0')
t0=Symbol('t0')
ans=dsolve(Eq(P.diff(t),a*P*(b-P)),P)
print(ans)
pprint(ans)


C=solve(Eq(P, b*exp(b*(C1 + a*t))/(exp(b*(C1 + a*t)) - 1)),C1)
print(C)

AN=simplify(b*exp(b*(log(-P0*exp(-a*b*t0)/(b - P0))/b + a*t))/(exp(b*(log(-P0*exp(-a*b*t0)/(b - P0))/b + a*t)) - 1))

