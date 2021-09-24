import random as r
import math as m
import turtle as t
import time as tm
t.shape('turtle')


###1
"""
t.color('red', 'red')
s = 50
a = 360
while True:
	t.forward(s*(r.random()-0.5))
	t.left(a*(r.random()-0.5))
"""


###2
"""
t.color('blue', 'blue')
r = 30
x0,y0 = t.pos()
t.penup()
t.goto(x0 - 400,y0)
t.pendown()
N = (	(1,1,1,1,1,1,0,0,0),
		(0,0,0,1,1,0,0,0,1),
		(0,0,1,1,0,1,1,0,0),
		(0,0,1,0,0,0,1,1,1),
		(0,1,0,1,1,0,0,1,0),
		(0,1,1,0,1,1,0,1,0),
		(1,0,0,0,1,1,0,1,1),
		(1,0,1,0,0,0,0,0,1),
		(1,1,1,1,1,1,0,1,0),
		(0,1,1,1,0,0,1,1,0),
		(1,1,1,1,1,1,1,1,1),
		(0,0,0,0,0,0,0,0,0),
		(0,0,0,0,0,0,0,1,0)   )

A = (0,90,90,0,90,135,225,135,315)
def drawn(n):
	b  =  str(n)
	N = []
	for k in range(len(b)):
		N.append(b[k])
	for i in range(len(N)):
		if N[i]=='-':
			draw(12)
		elif N[i]==' ':
			draw(11)
		else:
			draw(int(N[i]))
def draw(n):
	t.tracer(False)
	x,y = t.pos()
	NUM = N[n]
	for k in range(9):
		if NUM[k]!=0:
			t.pendown()
		else:
			t.penup()

		if k==6 or k==8:
			t.forward(r*(2**0.5))
		else:
			t.forward(r)
		t.right(A[k])
	t.penup()
	t.goto(x + 2*r,y)
	t.pendown()
	t.tracer(True)
	tm.sleep(1)
t.right(270)
drawn("-502 345 535")
"""


###3
class trl:
	def __init__(self):
		super(trl, self).__init__()
		self.turtle = t.Turtle(shape='turtle')
		self.x = A*(r.random()-0.5)
		self.y = A*(r.random()-0.5)
		self.vx = V*(r.random()-0.5)
		self.vy = V*(r.random()-0.5)

		self.turtle.penup()
		self.turtle.goto(self.x,self.y)


	def move(self, dt):
		self.x = self.x + dt*self.vx
		self.y = self.y + dt*self.vy
		self.turtle.goto(self.x,self.y)


def chech(turtle):
	for i in range(N):
		x0 = TRL[i].x
		y0 = TRL[i].y
		vx0 = TRL[i].vx
		vy0 = TRL[i].vy
		for j in range(N):
			if i==j:
				pass
			else:
				x1 = TRL[j].x
				y1 = TRL[j].y
				vx1 = TRL[j].vx
				vy1 = TRL[j].vy
				r = ((x1-x0)**2 + (y1-y0)**2)**0.5
				CH = ((R-r)>0)
				if CH:
					pass


N = 500
V = 5
A = 800
R = 5
TRL = []
dt = 10
t.tracer(False)
for k in range(N):
	TRL.append(trl())
t.tracer(True)
while True:
	t.tracer(False)
	for k in range(N):
		TRL[k].move(dt)
	t.tracer(True)
"""
from random import randint
import turtle


number_of_turtles = 5
steps_of_time_number = 1000


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(v)
    unit.goto(randint(-A, A), randint(-A, A))


while True:
    for unit in pool:
    	s = 50
    	unit.forward(s*(r.random()-0.5))
    	unit.left(360*(r.random()-0.5))
"""