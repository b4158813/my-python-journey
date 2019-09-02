# __next__()和send方法：
# next() 等价于 send(None)
def fib(times):
    n = 0
    a,b = 0,1
    while n < times:
        yield b# 该函数成为一个生成器
        a,b = b,a+b
        n += 1
    return 'done'
g = fib(5)
print(next(g))
print(g.__next__())# 同上

#  生成器生成结束后再生成就会报错（已经迭代结束）

print(g.send('hehe'))
# 生成器第一步的时候只能send(None)
# send方法能往生成器里面传参数
