import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x=np.arange(1,11,1)

fig=plt.figure()
ax=fig.add_subplot(111)

l1,=ax.plot(x,x*2)
l2,=ax.plot(x,x*3)
l3,=ax.plot(x,x*4)

ax.grid(linestyle='-.',color='pink',alpha=0.8,linewidth=2)
ax.legend(handles=[l1,l2,l3],labels=['Normal','Fast','Faster'],loc=0,ncol=3,fontsize=20,shadow=True)# 图例：位置默认最优，分为三列显示
#ax.set_xlim(0,10)

ax.tick_params(labelsize=20)

plt.show()

