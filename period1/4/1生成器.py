# coding = utf-8

'''
生成器
'''

'''
生成器特点：
    1.节约内存
    2.迭代到下一次的调用时，所使用的参数都是从第一次所保留下的
'''

# 第一种生成器创建方法：

# 这是创建列表
a = [x for x in range(5)]
print(a)

# 这是创建一个生成器
b = (x for x in range(5))
print(b)# 不会输出列表，而是一个生成器

for n in b:
    print(n)# 生成器生成到最后一位之后就会停止

print(30*'-')
# 第二种生成器创建方法：

# 斐波那契数列生成常规方法
def fib(times):
    n = 0
    a,b =0,1
    while n < times:
        print(b)
        a,b = b,a+b
        n += 1
    return 'done'
fib(5)

print(30*'-')
# yield生成器
def fib(times):
    n = 0
    a,b = 0,1
    while n < times:
        yield b# 该函数成为一个生成器
        a,b = b,a+b
        n += 1
    return 'done'
g = fib(5)# fib函数变成了生成器
for x in g:
    print(x)





