# -*- coding: utf-8 -*-

#编程实现九九乘法表：
for i in range(1,10):
    for j in range(1,10):
        print("%d*%d=%d\t"%(j,i,i*j),end="")
        if i==j:
            print("")
            break
    
#用函数实现求100-200里面所有素数：
def sushu():
    for i in range(100,201):
        j=2
        while j<i:
            if i%j==0:
                break
            elif j==i-1:
                print("%d"%i,end=",")
            j+=1
print("100-200内素数为：",end="")
sushu()

print("")
#函数实现判断用户输入的年份是否是闰年：
def year(n):
    if n%400==0 or (n%4==0 and n%100!=0):
        print("%s是闰年"%n)
        return
    print("%s不是闰年"%n)
u=int(input("请输入年份："))
year(u)
