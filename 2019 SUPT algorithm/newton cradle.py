import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt


f=open(r"C:\Users\81429\Desktop\2019 SUPT\牛顿摆\newtons_cradle_left.txt",encoding='utf-8')
data = pd.read_csv(f,sep='\t')
print(data)

t = list(data['t'])
vx = list(data['v_{x}'])
x = list(data['x'])

plt.plot(t,vx)
plt.show()

