'''
ndarray 拼接的各种方式
'''
import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])
C=np.vstack((A,B))# vertical stack
print(C)
print(A.shape,C.shape,'\n')# 合并之后变成两行三列矩阵
D = np.hstack((A,B))# horizontal stack
print(D,'\n',D.shape)
print(10*'-')
print(A.T.shape)# 转置之后还是序列，不改变维度
print(A[np.newaxis,:].shape)# newaxis方法，在行上加了一个维度
print(A[:,np.newaxis].shape)# 在列上加了一个维度

print(30*'-')
A_ = np.array([1,1,1])[:, np.newaxis]
B_ = np.array([2,2,2])[:, np.newaxis]
C_ = np.vstack((A_,B_))
D_ = np.hstack((A_,B_))
print(A_,'\n'*2,B_,'\n'*2,C_,'\n'*2,D_)


print(30*'-')
E = np.concatenate((A,B,B,A),axis=0)# concatenate合并，在后面定义在哪个维度进行合并
E_ = np.concatenate((A_,B_,A_,B_),axis=1)# 按行拼接
print(E,'\n',E_)

print(30*'-')
print(A,'\n',B,'\n')
print(np.c_[A,B],'\n')
print(np.r_[A,B],'\n')
