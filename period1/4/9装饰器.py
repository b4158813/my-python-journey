'''
装饰器：
- 装饰器其实就是一个闭包，把一个函数当做参数然后返回一个替代版函数
- 装饰器有两个特性：
    1.可以把被装饰的函数替换成其他函数
    2.可以在加载模块的时候立即执行

功能：
1.引入日志
2.函数执行时间统计
3.执行函数前预备处理
4.执行函数后清理功能
5.权限校验等场景
6.缓存
'''


'''
写法：

def w1(func):
    def inner():
        #验证1
        #验证2
        #验证3
        func()
    return inner

@w1
                    
                    装饰器语法，省去了以下过程：
                            传入函数f1到函数w1 ->
                            对f1添加验证功能进行修饰 ->
                            返回添加验证功能之后的f1
                    
        
def f1():# 这个f1就会自动添加验证功能
    print("f1")
'''

def deco(func):
    def wrapper():
        print(func.__name__)
        func()
    return wrapper

def fun():
    print('---1---')

ret = deco(fun)
ret()
# 以上两行为装饰器工作原理


@deco# “语法糖” 更简便语法
def fun2():
    print('---2---')

fun2()

print(fun2)# 现在已经变成被装饰后的函数