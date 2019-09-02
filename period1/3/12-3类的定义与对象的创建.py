# -*- coding: utf-8 -*-

#定义了一个类：
class Car:#类名首字母大写
    def start(self):#一定要写self,但不需要传参
        print("汽车启动")
    def print_car_inf(self):
        print("车的名字是：%s,颜色为：%s"%(self.name,self.color))
c=Car()#构建一个对象，记得要有括号，一定在内存中有一块空间存放对象的数据信息
c.name="迈腾"
c.color="金色"
#c2=Car()
c.start()#调用c对象的start方法
c.print_car_inf()


