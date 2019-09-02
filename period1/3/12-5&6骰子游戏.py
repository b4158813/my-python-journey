# -*- coding: utf-8 -*-
'''
每次游戏有两个人，每人3颗骰子，估计点数的个数
'''
import random
class Game:
    
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2
        print("初始化成功，游戏开始")
    
    def start_game(self):
        self.player1.cast()
        self.player2.cast()
        print(self.player1)
        print(self.player2)
#        play1_dice_count_list=[self.player1.dices[0].count,self.player1.dices[1].count,self.player1.dices[2].count]
#        play2_dice_count_list=[self.player2.dices[0].count,self.player2.dices[1].count,self.player2.dices[2].count]
#       print("玩家1抛骰子后的点数为：%s"%str(play1_dice_count_list))
#      print("玩家2抛骰子后的点数为：%s"%str(play2_dice_count_list))

    def get_win(self):
        self.player1.guess_dice()
        self.player2.guess_dice()
        #判断谁赢了
class Player:
    
    def __init__(self,name,gender,*dice):#*表示不定长的
        self.name=name
        self.gender=gender
        self.dices=dice#表示该玩家拥有的骰子的元组
    
    #玩家抛骰子
    def cast(self):
        for dice in self.dices:
            dice.move()
        
    def guess_dice(self):
        return (4,2)
    
    def __str__(self):
        play_dice_count_list=[self.dices[0].count,self.dices[1].count,self.dices[2].count]
        return "姓名为：%s,投掷的骰子点数信息为：%s"%(self.name,str(play_dice_count_list))
class Dice:
    
    def __init__(self):
        self.count=0
        
    #骰子滚动方法，滚动之后该骰子的点数确定
    def move(self):
        self.count=random.randint(1,6)
    
#游戏开始之前准备六颗骰子
d1=Dice()
d2=Dice()
d3=Dice()
d4=Dice()
d5=Dice()
d6=Dice()
#每次游戏需要两个玩家对象
p1=Player("player1","男",d1,d2,d3)
p2=Player("player2","女",d4,d5,d6)
#一共要玩五次游戏
for i in range(1,6):
    print("第%d次游戏的情况---------"%i)
    game=Game(p1,p2)
    game.start_game()

    
    
    
    
    
    
    
    
    
    
    



