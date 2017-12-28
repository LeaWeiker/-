#coding=utf-8

#引入pygame模块
import pygame
import time
import random

#引入键盘操作
from pygame.locals import *







#创建一个玩家类
class PlayerPlane(object):
	#初始化飞机
	def __init__(self,screen):

		#飞机图片
		planeImageName = 'img/plane.gif'
		self.image = pygame.image.load(planeImageName).convert()
		#设置默认的坐标（左上角为（0,0））
		self.x = 610
		self.y = 700
		self.chuangkou = screen
		self.name = 'player'
		self.bullet = []

	#将飞机画出来
	def draw(self):
		self.chuangkou.blit(self.image,(self.x,self.y))
		for temp in self.bullet:
			temp.draw()

	#飞机移动
	def keyHandle(self,keyValue):
		if  keyValue == 'left':
			print("---左移---")
			self.x -= 20
		elif keyValue == 'right':
			print("---右移---")
			self.x += 20
		elif keyValue == 'up':
			print("---上移---")
			self.y -= 20
		elif keyValue == 'down':
			print("---下移---")
			self.y += 20
		elif keyValue == 'space':
			print("---发射---")
			self.bullet.append(Bullet(self.chuangkou,self.name,self.x,self.y))



#创建子弹类
class Bullet(object):

	 def __init__(self,screen,planeName,x,y):
	 	print("调用初始化")
	 	if planeName == 'enemy':
	 		bulletImageName = './img/e_bullet.gif'
	 	elif planeName == 'player':
	 		bulletImageName = 'img/bullet.gif'

	 	self.bullet_img = pygame.image.load(bulletImageName).convert()
	 	self.x = x
	 	self.y = y
	 	self.chuangkou = screen
	 	self.planeName = planeName

	 def draw(self):
	 	if self.planeName == 'enemy':
	 		self.y+=4
	 	elif self.planeName == 'player':
	 		self.y -= 3
	 	self.chuangkou.blit(self.bullet_img,(self.x+65,self.y-50))



#创建敌军类
class Enemy(object):
	def __init__(self,screen,x,y):
		EnemyName = 'img/Enemy.gif'
		self.Enemy = pygame.image.load(EnemyName).convert()
		self.x = x
		self.y = y
		self.chuangkou = screen
		self.name = 'enemy'
		self.bullet = []
		self.derection = 'right'

	def draw (self):
		self.chuangkou.blit(self.Enemy,(self.x,self.y))
		for temp in self.bullet:
			temp.draw()

	def move (self):
		if self.derection == 'right':
			self.x += 4
		elif self.derection == 'left':
			self.x -= 4

		if self.x > 1348:
			self.derection = 'left'
		elif self.x <0:
			self.derection ='right'
		randomNum = random.randint(1,100)
		if randomNum in [1,5,50]:
			self.bullet.append(Bullet(self.chuangkou,self.name,self.x-60,self.y+90))




if __name__ == '__main__':

	screen = pygame.display.set_mode((1400,890),0,32)
	bgImageFile = './img/background.jpg'
	background = pygame.image.load(bgImageFile).convert()

	player = PlayerPlane(screen)
	Enemy = Enemy(screen,0,0)


	#显示背景
	#screen.blit(background)
	#pygame.display.update()
	
	while True:

		#飞机放在里面相当于创建了很多个飞机，所以不能写在这里
		#player = PlayerPlane()
		screen.blit(background,(0,0))

		#键盘操作,导入键盘检测
		#判断是否点击了退出按钮
		for event in pygame.event.get():

			if event.type == QUIT:
				print("exit")
				exit()

			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					print("left")
					player.keyHandle('left')

				elif event.key == K_d or event.key == K_RIGHT:
					print("right")
					player.keyHandle('right')
					
				elif event.key == K_w or event.key == K_UP:
					print("up")
					player.keyHandle("up")
					
				elif event.key == K_s or event.key == K_DOWN:
					print("down")
					player.keyHandle("down")

				elif event.key == K_SPACE:
					print("space")
					player.keyHandle("space")


		player.draw()
		Enemy.draw()
		Enemy.move()
		for temp in player.bullet:
			temp.draw()

		pygame.display.update()
		time.sleep(0.01)
