# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self,name):
        self.name=name
        
    def work(self,axe_type):
        print(self.name+"开始工作了")
        #person完成work，需要使用一把斧头
        
        #在原始社会，人需要一把石斧
        #axe=StoneAxe("花岗岩斧头")
        
        #使用钢铁的斧头
        #axe=SteelAxe("加爵牌斧头")
        #axe.cut_tree()

        #已经有工厂,person去找工厂生成一把斧头
        axe=Factory.create_axe(axe_type)
        axe.cut_tree()
    
class Axe(object):
    
    def __init__(self,name):
        self.name=name
        
    def cut_tree(self):
        print("%s斧头开始砍树"%(self.name))

class StoneAxe(Axe):
    
    def cut_tree(self):
        print("使用石头做的斧头砍树")
        
class SteelAxe(Axe):
    
    def cut_tree(self):
        print("使用钢铁做的斧头砍树")
        
#工厂类
#全局函数
class Factory(object):
    #根据用户指定的类型来生产斧头
    @staticmethod
    def create_axe(type):
        if type=="stone":
            return StoneAxe("花岗岩斧头")
        elif type=="steel":
            return SteelAxe("加爵斧头")
        else:
            print("传入的类型不对")
p=Person("zs")
p.work("steel")


























