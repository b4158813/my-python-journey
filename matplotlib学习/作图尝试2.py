import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

s = np.linspace(3,0,10000)
a = np.linspace(0.5*np.pi,6*np.pi,10000)
R = 0.3
t = np.linspace(0,3,10000)
#a = np.linspace(0,10,1000)
x = -s*np.sin(np.pi-a)+R*np.cos(a)
y = -s*np.cos(np.pi-a)+R*np.sin(a)

fig,ax = plt.subplots()
plt.plot(y,x)
plt.grid()

plt.draw()