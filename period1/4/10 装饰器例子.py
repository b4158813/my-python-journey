'''
一些例子
'''


def makeBold(func):
    def wrapped():
        return '<b>' + func() + '</b>'
    return wrapped

def makeItalic(func):
    def wrapped():
        return '<i>' + func() + '</i>'
    return wrapped

@makeBold
def fun1():
    return 'hello world-1'

@makeItalic
def fun2():
    return 'hello world-2'

@makeBold
@makeItalic
def fun3():
    return 'hello world-3'


print(fun1())
print(fun2())
print(fun3())
