"""
БРОУНОВСКОЕ ДВИЖЕНИЕ ЧЕРЕПАХИ
"""

import random as r
import turtle as t

t.shape('turtle')
t.color('red', 'red')

s = 50
a = 360
while True:
	t.forward(s*(r.random()-0.5))
	t.left(a*(r.random()-0.5))
