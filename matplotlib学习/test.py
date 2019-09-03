import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

plt.rcParams['font.sans-serif']=['SimHei'] #正常显示汉字的操作
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号的操作

fig=plt.figure()
ax=fig.add_subplot(111)

x=np.array([3.05,3.09,3.18,3.29,3.42,3.54,3.69])
y1=np.array([0.236,0.297,0.240,0.424,0.389,0.332,0.630])
y2=[49.97,62.43,74.18,80.58,84.05,86.17,87.61]

#ax.set_xlim(0,4)
#ax.set_ylim(0,0.7)
#ax.plot(x,y1)
xnew=np.linspace(x.min(),x.max(),300)
poew_smooth=spline(x,y1,xnew)
l1=ax.plot(xnew,poew_smooth)
l2=ax.scatter(x,y1,marker='o')
ax.grid(linestyle='--',alpha=0.8)
ax.set_xlabel('Pd/kW',fontsize=20)
ax.set_ylabel('效率%',fontsize=20)

ax.tick_params(labelsize=18)
plt.show()