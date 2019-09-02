import pandas as pd
import numpy as np
import matplotlib as plt
from pandas import DataFrame,Series

'''
plot data

Series
'''
data = Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()


'''
DataFrame
'''
data = DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
data = data.cumsum()
print(data.head())

#data.plot()
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2',ax=ax)
plt.pyplot.show()

'''
plot methods:
    'bar','hist','box','kde','area','scatter','hexbin','pie'
'''




