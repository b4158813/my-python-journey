import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig,ax=plt.subplots()
xinfo=[0.062,0.072,0.083,0.1,0.113,0.13]

yinfo=[80,85,90,95,100,105]

ax.plot(xinfo,yinfo,marker='o',linestyle='--')
ax.set_xlabel('压强')
ax.set_ylabel=('温度')

plt.show()