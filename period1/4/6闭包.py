'''
闭包（python可以嵌套定义函数）
-内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包
-Python内函数也是对象

-闭包不能修改外部作用域的局部变量
'''
def addx(x):# x是引用环境
    def adder(y): return x + y
    return adder

# adder为闭包

c = addx(8)# c现在是一个函数

type(c)# function

c(10)# 相当于addx(8)(10)