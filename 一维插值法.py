import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
plt.rcParams['font.sans-serif']=['SimHei'] #正常显示汉字的操作
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号的操作

def input_method():
    global kind
    print('''
            请输入需要的插值方法：
            1. 1阶B样条插值法（线性插值法）
            2. 2阶B样条插值法
            3. 3阶B样条插值法
            4. 最邻近插值法
            5. 阶梯插值法
            ''')
    while True:
        num=eval(input())
        if num==1:
            kind='slinear'
            break
        elif num==2:
            kind='quadratic'
            break
        elif num==3:
            kind='cubic'
            break
        elif num==4:
            kind='nearest'
            break
        elif num==5:
            kind='zero'
            break
        else:
            print('输入错误！请重新输入：')
            continue
def plot_method(xnew,ynew,kind):
    plt.plot(xnew, ynew, label=kind)
    plt.legend()

x=np.linspace(0,10,11)
# x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
y=np.sin(x)
plt.scatter(x,y)

xnew=np.linspace(0,10,101)

input_method()
f=interpolate.interp1d(x,y,kind=kind)

ynew=f(xnew)

plot_method(xnew,ynew,kind)

print(f(1.5))
