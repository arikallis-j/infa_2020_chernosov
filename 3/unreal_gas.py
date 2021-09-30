from random import randint
import turtle
number_of_turtles = 5
steps_of_time_number = 1000
v = 100
A = 100
R = 10
s = 5


turtle.penup()
turtle.goto(-A-R,-A-R)
turtle.pendown()
for k in range(4):
	turtle.forward(2*(A+R))
	turtle.left(90)
def check_turtle(this_turtle):
	x,y = this_turtle.pos()
	for i in range(number_of_turtles):
		global pool
		other_turtle = pool[i]
		if (this_turtle != other_turtle):
			x1,y1 = other_turtle.pos()
			r = ((x1-x)**2 + (y1-y)**2)**0.5
			if r<R:
				other_turtle.left(180 + randint(-20,+20))
				this_turtle.left(180 + randint(-20,+20))
				other_turtle.forward(3*s)
				this_turtle.forward(3*s)
			else:
				pass
def check_wall(turtle):
	x,y = turtle.pos()
	if abs(x)>A or abs(y)>A:
		turtle.left(180 + randint(-45,+45))




pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(v)
    unit.goto(randint(-A, A), randint(-A, A))
    unit.left(randint(0,360))


while True:
    for unit in pool:
    	
    	check_turtle(unit)
    	check_wall(unit)
    	unit.forward(s)

