'''
闭包可以说是延长了外部函数参数（应用环境）的生命周期
'''

def outter(num):
    def inner(num_in):
        print('num_in is %d'%num_in)
        return num + num_in
    return inner

fun = outter(10)

print(fun(20))# fun(20)等于outter(10)(20)

