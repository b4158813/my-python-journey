import numpy as np
from numpy.linalg import inv #矩阵求逆的方法


a=np.array([[1,0,0],[0,2,0],[0,0,3]])
b=inv(a) #矩阵求逆


print(a)
print(b)

