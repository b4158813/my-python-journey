# -*- coding: utf-8 -*-

#计算阶乘的方法：
#循环的方法：
n=4
result=1
i=1
while i<=4:
    result=result*i
    i+=1
print(result)

#递归方法:
#1、在函数内部调用自己本身
#2、递归函数本质是一个方法的循环调用，注意：有可能出现死循环
#3、一定要定义递归的边界（什么时候退出循环）
def rac(n):
    if n==1 or n==0:
        return 1
    return n*rac(n-1)

n=int(input("要算几的阶乘："))
print("%d的阶乘为：%d"%(n,rac(n)))

'''
def hello():
    print("hello")
    hello()
hello()
'''

def get_num(n):#获取斐波那契数列中第n个数字的值
    if n==1 or n==2:
        return 1
    else:
        return get_num(n-1)+get_num(n-2)
#把获取的斐波那契数字存放到列表中
nums=[]
for i in range(1,21):#range默认从0开始，这里要加个1，且包头不包尾
    nums.append(get_num(i))#get_num获得一个斐波那契数字
print("%s"%nums)






























