'''
pyplot
    经典高层封装
pylab
    将matplotlib和numpy合并的模块，模拟MATLAB编程环境
面向对象的方式（Object-Oriented）
    matplotlib的精髓，更基础和底层的方式


实战中综合使用pyplot和OO的方式
'''

from pylab import *
#可以直接使用numpy和matplotlib的方法
x=arange(0,10,1)
y=randn(len(x))

plot(x,y)

title('pylab')

show()


