# coding:utf-8
'''
1、游戏主界面
2、坦克
		我方坦克
		敌方坦克
3、炮弹
4、隔离墙
5、爆炸

这些类都是pygame中的sprite的子类
'''
import pygame,sys,time
from random import randint


class TankMain(object):
	"""坦克大战的主窗口"""
	width = 600
	height = 500
	my_tank_missile = []
	my_tank = None
	# enemy_list = []
	wall = None
	enemy_list = pygame.sprite.Group()  # 地方坦克的组群
	explode_list = []
	enemy_missile_list = pygame.sprite.Group()
	# 开始游戏的方法
	def start_game(self):
		pygame.init()  # pygame模块初始化，加载系统资源
		# 创建一个窗口，窗口的大小(宽,高)，窗口的特性（0，REZIZEBLE,FULLSCREEEN）,颜色位数（32位）
		screen=pygame.display.set_mode((TankMain.width,TankMain.height),0,32)
		# 给窗口设置一个标题
		pygame.display.set_caption("坦克大战")
		# 创建一堵墙
		TankMain.wall = Wall(screen,80,160,30,120)

		TankMain.my_tank = Mytank(screen) # 创建一个我方坦克，坦克显示在屏幕中下部位置
		if len(TankMain.enemy_list) == 0:
			for i in range(1,6):  # 游戏开始时初始化五个敌方坦克
				TankMain.enemy_list.add(Enemytank(screen))  # 把敌方坦克放到组里
		while True:
			if len(TankMain.enemy_list) < 5:
				TankMain.enemy_list.add(Enemytank(screen))
			# color RGB（0，0，0），（255，255，255）
			# 设置屏幕背景色为黑色
			screen.fill((0,0,0))

			# 用draw方法画矩形：（面向过程编程）
			# pygame.draw.rect(screen,(0,255,0),pygame.Rect(400,30,100,30),5)


			# 显示左上角的文字
			for i,text in enumerate(self.write_text(),0):
				screen.blit(text, (0,5+(15*i)))
			# 显示游戏中的墙，并且对墙和其他对象进行碰撞检测
			TankMain.wall.display()
			TankMain.wall.hit_other()

			self.get_event(TankMain.my_tank,screen)  # 获取事件，根据获取的事件做处理

			if TankMain.my_tank:
				TankMain.my_tank.hit_enemy_missile()# 我方坦克和地方炮弹进行碰撞检测
			if TankMain.my_tank and TankMain.my_tank.live:
				TankMain.my_tank.display()  # 在屏幕上显示我方坦克
				TankMain.my_tank.move()  # 在屏幕上移动我方坦克
			else:
				TankMain.my_tank = None

			# 显示和随机移动所有的敌方坦克
			for enemy in TankMain.enemy_list:
				enemy.display()
				enemy.random_move()
				enemy.random_fire()

			# 显示所有的我方炮弹
			for m in TankMain.my_tank_missile:
				if m.live:
					m.display()
					m.hit_tank()  # 炮弹打中敌方坦克
					m.move()
				else:
					TankMain.my_tank_missile.remove(m)

			# 显示所有的敌方炮弹
			for m in TankMain.enemy_missile_list:
				if m.live:
					m.display()
					m.move()
				else:
					TankMain.enemy_missile_list.remove(m)

			for explode in TankMain.explode_list:
				explode.display()
			# 显示重置
			time.sleep(0.03)#每次休眠0.03秒调到下一帧
			pygame.display.update()

	# 获取所有的事件（敲击键盘，鼠标点击）
	def get_event(self,mytank,screen):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.stop_game()  # 程序退出
			if event.type == pygame.KEYDOWN and (not mytank) and event.key == pygame.K_n:
				TankMain.my_tank = Mytank(screen)
			if event.type == pygame.KEYDOWN and mytank:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					mytank.direction = "L"
					mytank.stop = False
					# Mytank.move()
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					mytank.direction = "R"
					mytank.stop = False
					# Mytank.move()
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					mytank.direction = "U"
					mytank.stop = False
					# Mytank.move()
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					mytank.direction = "D"
					mytank.stop = False
					# Mytank.move()
				if event.key == pygame.K_ESCAPE:  # 敲击Esc程序退出
					self.stop_game()
				if event.key == pygame.K_SPACE:
					m = mytank.fire()
					m.good =True  # 我方坦克发射的炮弹，好炮弹
					TankMain.my_tank_missile.append(m)
			if event.type == pygame.KEYUP and mytank:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_a or event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_d:
					mytank.stop = True
	# 关闭游戏的方法
	def stop_game(self):
		sys.exit()
		pass

	# 在屏幕左上角显示文字内容
	def write_text(self):
		font = pygame.font.SysFont("隶书", 12)  # 定义一个字体
		text_sf1 = font.render("敌方坦克数量为:%d"%len(TankMain.enemy_list),True,(255,0,0))  # 根据字体创建一个文字的图像
		text_sf2 = font.render("我方坦克炮弹数量为:%d"%len(TankMain.my_tank_missile),True,(255,0,0))  # 根据字体创建一个文字的图像
		return text_sf1,text_sf2

# 坦克大战游戏中所有对象的父类
class BaseItem(pygame.sprite.Sprite):
	def __init__(self,screen):
		pygame.sprite.Sprite.__init__(self)
		# 所有对象共享的属性
		self.screen = screen

	# 在游戏屏幕中显示当前游戏对象
	def display(self):
		if self.live:
			self.image = self.images[self.direction]
			self.screen.blit(self.image,self.rect)


# 坦克的公共父类
class Tank(BaseItem):
	# 定义类属性，所有坦克对象高和宽都是一样的
	width = 50
	height = 50
	def __init__(self,screen,left,top):
		super().__init__(screen)
		self.direction = 'D'  # 坦克方向，默认方向往下（上下左右）
		self.speed = 5  # 坦克移动的速度
		self.stop = True
		self.images = {}  # 坦克的所有图片，key为方向，value为图片
		self.images['L'] = pygame.image.load("images/tankL.png")
		self.images['R'] = pygame.image.load("images/tankR.png")
		self.images['U'] = pygame.image.load("images/tankU.png")
		self.images['D'] = pygame.image.load("images/tankD.png")
		self.image = self.images[self.direction]  # 坦克的图片由方向决定
		self.rect = self.image.get_rect()
		self.rect.left = left
		self.rect.top = top
		self.live = True  # 决定坦克是否生存
		self.oldtop = self.rect.top
		self.oldleft = self.rect.left


	def stay(self):
		self.rect.top = self.oldtop
		self.rect.left = self.oldleft


	def move(self):
		if not self.stop:  #如果坦克不是停止状态
			self.oldleft = self.rect.left
			self.oldtop = self.rect.top
			if self.direction == "L":
				if self.rect.left > 0: # 判断坦克是否在屏幕左边的边界上
					self.rect.left -= self.speed
				else:
					self.rect.left = 0
			elif self.direction == "R":
				if self.rect.right < TankMain.width:
					self.rect.right += self.speed
				else:
					self.rect.right = TankMain.width
			elif self.direction == "U":
				if self.rect.top > 0:
					self.rect.top -= self.speed
				else:
					self.rect.top = 0
			elif self.direction == "D":
				if self.rect.bottom < TankMain.height:
					self.rect.bottom += self.speed
				else:
					self.rect.bottom = TankMain.height

	def fire(self):
		m = Missile(self.screen,self)
		return m

class Mytank(Tank):
	def __init__(self,screen):
		super().__init__(screen,275,400)  # 创建一个我方坦克，坦克显示在屏幕中下部位置
		self.stop = True
		self.live = True

	def hit_enemy_missile(self):
		hit_list = pygame.sprite.spritecollide(self,TankMain.enemy_missile_list,False)
		for m in hit_list:#我方坦克中弹了
			m.live = False
			TankMain.enemy_missile_list.remove(m)
			self.live = False
			explode = Explode(self.screen,self.rect)
			TankMain.explode_list.append(explode)


class Enemytank(Tank):
	def __init__(self,screen):
		super().__init__(screen,randint(1,5)*100,200)
		self.step = 10  # 坦克按照某个方向连续移动的步数
		self.get_random_direction()
		self.speed = 3  # 设置敌方坦克速度

	# 获得一个随机的方向
	def get_random_direction(self):
		r = randint(0, 4)  # 得到一个坦克移动方向和停止的随机数
		if r == 4:
			self.stop = True
		elif r == 1:
			self.direction = "L"
			self.stop = False
		elif r == 2:
			self.direction = "R"
			self.stop = False
		elif r == 0:
			self.direction = "U"
			self.stop = False
		elif r == 3:
			self.direction = "D"
			self.stop = False

	# 敌方坦克按照一个随机的方向连续移动6步，然后才能再次改变方向
	def random_move(self):
		if self.live:
			if self.step == 0:
				self.get_random_direction()
				self.step = 6
			else:
				self.move()
				self.step -= 1
	def random_fire(self):
		r = randint(0,50)
		if r == 10:
			m = self.fire()
			TankMain.enemy_missile_list.add(m)
		else:
			return


class Missile(BaseItem):
	width = 12
	height = 12

	def __init__(self,screen,tank):
		super().__init__(screen)
		self.tank=tank
		self.direction = tank.direction  # 炮弹的方向由所发射的坦克的方向决定
		self.speed = 12  # 炮弹移动的速度
		self.images = {}  # 炮弹的所有图片，key为方向，value为图片
		self.images['L'] = pygame.image.load("images/missileL.png")
		self.images['R'] = pygame.image.load("images/missileR.png")
		self.images['U'] = pygame.image.load("images/missileU.png")
		self.images['D'] = pygame.image.load("images/missileD.png")
		self.image = self.images[self.direction]  # 坦克的图片由方向决定
		self.rect = self.image.get_rect()
		self.rect.left = tank.rect.left +(tank.width - self.width)/2
		self.rect.top = tank.rect.top + (tank.height - self.height)/2
		self.live = True  # 炮弹是否生存

	def move(self):
		if self.live:  #如果炮弹还存在
			if self.direction == "L":
				if self.rect.left > 0: # 判断坦克是否在屏幕左边的边界上
					self.rect.left -= self.speed
				else:
					self.live = False
			elif self.direction == "R":
				if self.rect.right < TankMain.width:
					self.rect.right += self.speed
				else:
					self.live = False
			elif self.direction == "U":
				if self.rect.top > 0:
					self.rect.top -= self.speed
				else:
					self.live = False
			elif self.direction == "D":
				if self.rect.bottom < TankMain.height:
					self.rect.bottom += self.speed
				else:
					self.live = False

	def hit_tank(self):
		if self.good:  # 如果炮弹是我方的炮弹
			hit_list = pygame.sprite.spritecollide(self,TankMain.enemy_list,False)
			for e in hit_list:
				e.live = False
				TankMain.enemy_list.remove(e)  # 如果敌方坦克被击中，则从列表中删除敌方坦克
				self.live = False
				explode = Explode(self.screen,e.rect)  # 产生了一个爆炸对象
				TankMain.explode_list.append(explode)


# 爆炸类
class Explode(BaseItem):
	def __init__(self,screen,rect):
		super().__init__(screen)
		self.live = True
		self.images = [pygame.image.load("images/0.png"),\
					   pygame.image.load("images/1.png"),\
                       pygame.image.load("images/2.png"),\
                       pygame.image.load("images/3.png"),\
                       pygame.image.load("images/4.png"),\
                       pygame.image.load("images/5.png"),\
					   pygame.image.load("images/6.png"),\
					   pygame.image.load("images/7.png"),\
					   pygame.image.load("images/8.png"),\
					   pygame.image.load("images/9.png"),\
					   pygame.image.load("images/10.png")]
		self.step = 0
		self.rect = rect  # 爆炸的位置和发生爆炸前，炮弹碰到的坦克位置一样，在构建爆炸的时候把坦克的rect传递进来

	# display方法在整个游戏运行过程中，循环调用，每隔0.1秒用一次
	def display(self):
		if self.live:
			if self.step == len(self.images):  # 最后一张爆炸图片已经显示了
				self.live = False
			else:
				self.image = self.images[self.step]
				self.screen.blit(self.image,self.rect)
				self.step +=1
		else:
			pass

# 游戏中的墙
class Wall(BaseItem):
	def __init__(self,screen,left,top,width,height):
		super().__init__(screen)
		self.rect = pygame.Rect(left,top,width,height)
		self.color = (255,0,0)
	def display(self):
		self.screen.fill(self.color,self.rect)
	# 针对墙和其他坦克或者炮弹的碰撞检测
	def hit_other(self):
		if TankMain.my_tank:
			is_hit = pygame.sprite.collide_rect(self,TankMain.my_tank)
			if is_hit:
				TankMain.my_tank.stop = True
				TankMain.my_tank.stay()
		if TankMain.enemy_list:
			hit_list = pygame.sprite.spritecollide(self,TankMain.enemy_list,False)
			for e in hit_list:
				e.stop = True
				e.stay()
		if TankMain.enemy_missile_list:
			hit_missile_list = pygame.sprite.spritecollide(self,TankMain.enemy_missile_list,False)
			for m in hit_missile_list:
				m.live = False
game = TankMain()
game.start_game()