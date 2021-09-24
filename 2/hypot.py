###1
"""
a = 179
b = 197
c = (a ** 2 + b ** 2) ** 0.5
print (c)
"""


###2
"""
import turtle
turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
"""


###3
"""
import turtle
turtle.shape('turtle')
for k in range(4):
	turtle.forward(100)
	turtle.left(90)
"""


###4
"""
import turtle
turtle.shape('turtle')
n  = 100
for i in range(n):
	turtle.forward(400/n)
	turtle.left(360/n)
"""


###5
"""
import turtle
turtle.shape('turtle')
r = 100
p = 20
n = 2
for k in range(n):
	turtle.forward(r+k*p)
	turtle.left(90)
	turtle.forward(r+k*p)
	turtle.left(90)
	turtle.forward(r+k*p)
	turtle.left(90)
	turtle.forward(r+k*p)
	turtle.left(90)
	turtle.penup()
	turtle.goto(-p*(k+1)/2, -p*(k+1)/2)
	turtle.pendown()
"""


###6
"""
import turtle as t
t.shape('turtle')
l = 200
n = 10
for k in range(n):
	t.forward(l)
	t.stamp()
	t.left(180)
	t.forward(l)
	t.left(180)
	t.left(360/n)
"""


###7
"""
import turtle as t
t.shape('turtle')
n  = 4
m = 100
f = 360/m
k = 1/100
for i in range(m*n):
	t.forward(i*f*k)
	t.left(f)
"""


###8
"""
import turtle as t
t.shape('turtle')
m = 4
n = 6
p = 10
for i in range(m*n):
	t.forward(10 + i*p)
	t.left(90)
"""

###9
"""
import turtle as t
import math as m
n = 10
p = 1
t.shape('turtle')
def nangle(n, a):
	a  *= 10
	sinf = 2* m.sin( 360/(2*n) )
	r = a / (sinf)

	for i in range(n):
		t.forward(a)
		t.left(360/n)

def Mnangle(n,p):
	t.left(90)
	for i in range(n):
		t.penup()
		t.backward(p*5)
		t.right(90)
		t.forward(20*p)
		t.left(90)
		t.pendown()
		nangle(i+3, 10 + p*(i+1))
Mnangle(n,p)
"""


###10
"""
import turtle as t
t.shape('turtle')
n = 2
m  = 100
for k in range(n):
	for i in range(m):
		t.forward(400/m)
		t.left(360/m)
	for j in range(m):
		t.forward(400/m)
		t.right(360/m)
	t.left(180/n)
"""


###11
"""
import turtle as t
t.shape('turtle')
n = 10
m  = 100
r = 400
p = 50
t.left(90)
for k in range(n):
	for i in range(m):
		t.forward((r + p*(k+1))/m)
		t.left(360/m)
	for j in range(m):
		t.forward((r + p*(k+1))/m)
		t.right(360/m)
"""


###12
"""
import turtle as t
t.shape('turtle')
n = 10
m  = 100
r = 400
p = 100
t.left(90)
for k in range(n):
	for i in range(m):
		t.forward(r/m)
		t.right(360/m)
		x,y = t.pos()
		t.goto(x+p/m,y)
"""


###13
"""
import turtle as t
t.shape('turtle')
t.speed = 0 
t.penup()
#t.goto(0,100)
t.pendown()
t.color('yellow', 'black')
t.begin_fill()
t.circle(70)
t.end_fill()

t.penup()
t.goto(-30,100-30)
t.pendown()
t.color('yellow', 'blue')
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(+30,100-30)
t.pendown()
t.color('yellow', 'blue')
t.begin_fill()
t.circle(10)
t.end_fill()


t.penup()
t.goto(0,70)
m = 20
p = 24
for k in range(m):
	t.penup()
	x,y = t.pos()
	t.goto(x,y-p/m)
	t.pendown()
	t.color('red', 'red')
	t.begin_fill()
	t.circle(2)
	t.end_fill()
	t.pendown()

t.penup()
x,y = t.pos()
t.goto(x-30,y-10)
m = 50
p = 60
for k in range(m):
	t.penup()
	x,y = t.pos()
	t.goto(x+p/m,y)
	t.pendown()
	t.color('green', 'green')
	t.begin_fill()
	t.circle(2)
	t.end_fill()
	t.pendown()
"""


###14
"""
import turtle as t
t.shape('turtle')
t.speed = 0 
def star(n,r):
	t.left(180)
	for k in range(n+2):
		t.forward(10*r)
		t.left(180-180/n)
	if n%2==0:	
		t.forward(10*r)
		t.left(180-180/n)


star(6,30)
import time
time.sleep(5)
"""