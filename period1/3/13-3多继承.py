# -*- coding: utf-8 -*-

##################################
#多继承

class A(object):#任何类都有父类object，可不写但习惯上最好写
    def test(self):
        print("A-----test()")
        
class B(object):
    def test(self):
        print("B-----test()")

class C(B,A):#与括号顺序有关
    def test(self):
        print("C-----test()")

c=C()
print(C.__mro__)#获取类优先级
c.test()






