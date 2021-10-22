import pygame
from random import randint
from math import sin, cos, pi
from constant import *
from inic import *


def f(x):
	print(x)
def rect(*arg):
	pygame.draw.rect(*arg)
def circle(*arg):
	pygame.draw.circle(*arg)

def argf(color,x,y,r):
	return ["None arguments"]
def argball(color,r,x,y):
	return Win, color, ( [x,y], [r,r])
def argbox(color,r,x,y):
	return Win, color, [x,y], r


def draw_aboard():
    pygame.draw.lines(Win, YELLOW, True, line_basket, width = widthLine)
    pygame.draw.lines(Win, YELLOW, True, line_table, width = widthLine)
    pygame.draw.lines(Win, YELLOW, True, line_current, width = widthLine)

def draw_timeline():
	time_text = "Time: " + str(round(maxTime*10 - time//100)/10) 
	Time = font.render(time_text, True, YELLOW)
	Win.blit(Time, (winY + 2*aboard, paragraph))

def draw_level():
	level_text = "Level: " + level
	Level = font.render(level_text, True, YELLOW)
	Win.blit(Level, (winY + 2*aboard, 0))

def draw_score():
	score_text = "Score: " + str(count)
	Score = font.render(score_text, True, YELLOW)
	Win.blit(Score, (winY + 2*aboard, 2*paragraph))

class target():
	"""docstring for target"""
	def __init__(self,id):
		self.id = id
		self.nameClass = "nameClass"
		self.r = randint(10, 100)
		self.color = COLORS[randint(0, len(COLORS)-1)]

		self.func = f
		self.argfunc = argf
		self.alpha = randint(0, 360)*pi/180
		self.x = randint(self.r, winY-self.r)
		self.y = randint(self.r, winY-self.r)
		self.vx = round(speed*cos(self.alpha))
		self.vy = round(speed*sin(self.alpha))
		
		self.right = 0
		self.left = 0
		self.bottom = 0
		self.top = 0

		self.count = 0
		self.arg = self.argfunc(self.color,self.x,self.y,self.r)

	def draw(self):
		self.func(*self.arg)

	def move(self):
		xwall = self.x < self.right or self.x > self.left
		ywall = self.y < self.bottom or self.y > self.top
		if xwall:
			self.vx = (-1)*self.vx
		if ywall:
			self.vy = (-1)*self.vy

		self.x += self.vx
		self.y += self.vy
		self.arg = self.argfunc(self.color,self.r,self.x,self.y)


class ball(target):
	"""docstring for ball"""
	def __init__(self,id):
		super(ball, self).__init__(id)
		self.nameClass = "ball"
		self.count = 1

		self.right = aboard + self.r 
		self.left = winY - aboard - self.r
		self.bottom = aboard + self.r 
		self.top = winY - aboard - self.r
		self.argfunc = argbox
		self.arg = self.argfunc(self.color,self.r,self.x,self.y)
		self.func = circle
		
class box(target):
	"""docstring for box"""
	def __init__(self,id):
		super(box, self).__init__(id)
		self.nameClass = "box"
		self.count = 5
		self.vx += round(speed**2/2)
		self.vy += round(speed**2/2)

		self.right = aboard
		self.left = winY - self.r
		self.bottom = aboard
		self.top = winY - aboard - self.r
		self.argfunc = argball
		self.arg = self.argfunc(self.color,self.r,self.x,self.y)
		self.func = rect


class basket():
	"""docstring for basket"""
	def __init__(self):
		self.BALLS = [ ball(i) for i in range(Nballs) ]
		self.BOXES = [ box(i) for i in range(Nboxes) ]
		self.BASKET = self.BALLS + self.BOXES
		self.id = len(self.BASKET)
	def draw(self):
		for targ in self.BASKET:
			targ.draw()
			targ.move()
	def click(self, event):
		global count
		x1, y1 = event.pos
		for targ in self.BASKET:
			x, y, r, name = targ.x, targ.y, targ.r, targ.nameClass
			run = ( (x1-x)**2 + (y1-y)**2 - r**2 ) < 0
			if run:
				count += targ.count
				new = name + "(" + str(self.id) + ")"
				self.BASKET.remove(targ)
				self.BASKET.append(eval(new))


class table():
	"""docstring for table"""
	def __init__(self):
		self.arg = "dkdsk"

	def draw(self):
		draw_aboard()
		draw_timeline()
		draw_level()
		draw_score()

class win():
	"""docstring for """
	def __init__(self):
		self.X = winX
		self.Y = winY
		self.color = BLACK
		self.win = Win
		self.time = time
	def draw(self):
		global time
		self.win.fill(self.color)
		time = self.time
	def new_record(self):
		from inic import Data
		print("Your record: "+str(count))
		name = input("Your name: ")
		if not(name in Data['leaders'][level]) or Data['leaders'][level][name]<count:
			Data['leaders'][level][name] = count
		for lev in Data['leaders']:
			print("\n"+'"'+lev+'"')
			for res in Data['leaders'][lev]:
				print(res + " : " + str(Data['leaders'][lev][res]))


class picture():
	"""docstring for Game"""
	def __init__(self):
		self.basket = basket()
		self.table = table()
		self.win = win()
		self.PICTURE = [self.win,self.basket, self.table]

	def draw(self):
		for part in self.PICTURE:
			part.draw()

		