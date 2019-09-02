def gen(times):
    n = 0
    while n < times:
        temp = yield n*2
        print(temp)# 将传入的参数接受并输出
        n += 1
    return 'done'
