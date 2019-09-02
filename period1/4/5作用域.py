'''
命名空间（namespace）
-防止命名冲突

全局变量和局部变量
-函数内的变量叫局部变量
-函数外的变量叫局部变量
-globals() 和 locals() # 用于打印出全局变量和局部变量
-局部变量和全局变量的冲突（LEBG）
    locals -> enclosing function -> globals -> builtins
    查看内建模块 dir(__builtin__)
'''

a = 50

def fun():
    a = 20
    b = 30
    print(locals())
fun()

print(a)

def fun2():
    global a
    a = 100

fun2()
print(a)
