import turtle as t
t.shape('turtle')

S = 'f+f+f+f'
SIZE = 10
ANGLE = 60
t.penup()
t.goto(-200,-200)
t.pendown()
def move():
	t.forward(SIZE)
def left():
	t.left(ANGLE)
def right():
	t.right(ANGLE)
def do(s):
	for a in s:
		if (a in actions):
			actions[a]()
def judge(s,p):
	ns = ''
	for r in s:
		if (r in rules[p]):
			ns += rules[p][r]
		else:
			ns += r
	return ns

actions = { 'f': move,
			'+': left,
			'-': right}

rules = [
			{
				'f' : 'f+f+f+f'
			},

			{
				'f' : 'f+f--f+f' #снежинка коха
			},

		]

def tree(s,p):
	p = str(p)
	for i in range(9):
		s = judge(s,int(p[i])-1)
	t.tracer(False)
	do(s)
	t.tracer(True)

tree('f',111)

t.exitonclick()
