import random as r
import math as m
import turtle as t
import time as tm
t.shape('turtle')


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