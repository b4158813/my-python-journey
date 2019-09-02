'''
普通一元一次方程
'''

def line(a,b,x):
    return a*x+b

print(line(1,1,0))
print(line(1,1,1))


print(30*'-')

'''
闭包实现一元一次方程
'''

def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

line1 = line_conf(1,1)
line2 = line_conf(4,5)

print(line1(5))# 1*5+1
print(line2(5))# 4*5+5

