# -*- coding: utf-8 -*-
a="123"
f=None
try:
    f=open("text.txt")
    try:
        content=f.read()
        content.index("hello")
        i=1/0
    #except Exception as ex:#捕获所有异常
    except ValueError as ex:
        print(ex)
    finally:
        print("最里层的finally")
    #f.write("world %d"%a)
    #f.close()
except (FileNotFoundError,ZeroDivisionError) as ex:
    print(ex)
    print("外面的try捕获了异常")
else:#没有异常时执行的代码
    print("else")
finally:#最终要执行的代码，不管前面是否出现exception
    print("finally")
    if f:
        f.close()
        


