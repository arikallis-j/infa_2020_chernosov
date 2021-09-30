"""
ЧЕРЕПАХА ПРИНТЕР

Массив N задает числа от 0 до 9,
а также пробел и знак минус

Функция draw отрисовывает заданные
цифры и знаки

Функция artist принимает в качестве аргумента
строку с цифрами и знаками, или же число,
и возвращает отрисовку всех цифр и знаков
"""


import random as r
import turtle as t
import time as tm

t.shape('turtle')
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


def artist(n):
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
artist("-502 345 535")
