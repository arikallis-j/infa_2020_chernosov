"""
ПОСТРОЕНИЕ ФРАКТАЛОВ

STR - начальная строчка
SIZE - размер отрисовки
ANGLE - угол поворота налево/направо
RUN - количество итераций для рисовки дерева

move, left, right - переобозначение вперед/налево/направо
judge - функция, применяющее правило к строке
do - функция, исполняющая строку
tree - рисование дерево по одному правилу

Actions - словарь возможных функций
Rules - правила изменения строки
"""

import turtle as t
t.shape('turtle')
t.penup()
t.goto(-200,-200)
t.pendown()


STR = 'f+f+f+f'
SIZE = 10
ANGLE = 60

RUN = 9

def move():
	t.forward(SIZE)
def left():
	t.left(ANGLE)
def right():
	t.right(ANGLE)

def do(s):
	for a in s:
		if (a in Actions):
			Actions[a]()

def judge(s,p):
	ns = ''
	for r in s:
		if (r in Rules[p]):
			ns += Rules[p][r]
		else:
			ns += r
	return ns

def tree(p):
	p = p - 1
	s = STR
	for i in range(RUN):
		s = judge(s,p)
	#t.tracer(False)
	do(s)
	#t.tracer(True)

def ill_tree(p):
	p = str(p)
	s = STR
	for i in range(len(p)):
		s = judge(s,int(p[i])-1)
	#t.tracer(False)
	do(s)
	#t.tracer(True)


Actions = { 'f': move,
			'+': left,
			'-': right}

Rules = [
			{
				'f' : 'f+f+f+f' #дракон, №1
			},

			{
				'f' : 'f+f--f+f' #снежинка коха №2
			},

		]

tree(2)
#ill_tree(12212)

t.exitonclick()
