# -*- coding: utf-8 -*-

#1到100 的偶数相加

i = 1
sum = 0

while i <= 100:
    if i%2 == 0:
        sum = sum + i
    else:
        pass
    i = i+1
print('从1到100的和为：%s'%sum)

#打印矩形

y = 1
while y <= 10:
    x = 1
    while x <= 10:
        print('*',end="")#print默认换行，即print('...',end="\n")
        x+=1
    print('')#换行
    y = y+1


#打印直角三角形

x = 1
while x <=5:
    y=1
    while y <=x:
        print('*',end="")
        y+=1
    print('')
    x+=1
