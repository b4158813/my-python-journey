x1=eval(input('输入第一个数：'))
y1=eval(input('输入第二个数：'))

x=x0=max(x1,y1)
y=y0=min(x1,y1)
while True:
    r=x%y
    x=y
    y=r
    if r==0:
        break


print('x和y的最大公约数为：',x)
print('x和y的最小公倍数为：',(x0*y0)/x)