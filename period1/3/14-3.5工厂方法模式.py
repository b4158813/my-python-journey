# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
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
        axe=Steel_Axe_Factory().create_axe()
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
        
#工厂方法模式
class Factory(object):
    #根据用户指定的类型来生产斧头
    def create_axe():
        pass
    
class Stone_Axe_Facory(Factory):
    
    def create_axe(self):
        return StoneAxe("花岗岩斧头")
    
class Steel_Axe_Factory(Factory):
    
    def create_axe(self):
        return SteelAxe("钢铁斧头")
    
p=Person("zs")
p.work("steel")



























