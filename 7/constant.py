#window
FPS = 120
winX, winY = 1200, 900

#colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#table
count = 0
time = 0
aboard = 5
paragraph = 50
widthLine = 3

#parameters
Nballs = 5
Nboxes = 5
maxCount = 100
maxTime = 10

#workers
Clock = None
Win = None
font = None
fontHead = None

#records
Data = []

#level
while True:
	level = input("level: ")
	if level == 'hard':
		speed = 5
		break
	elif level == 'normal':
		speed = 3
		break
	elif level == 'easy':
		speed = 2
		break
	else:
		speed = 0
		continue


#table
line_basket = [
		(aboard - widthLine, aboard - widthLine),
		(aboard - widthLine + winY, aboard - widthLine),
		(aboard - widthLine + winY, - aboard + widthLine + winY),
		(aboard - widthLine, - aboard + widthLine + winY)
		]

line_table = [
		(aboard - widthLine + winY, aboard - widthLine),
		(-aboard + widthLine + winX, aboard - widthLine),
		(-aboard + widthLine + winX, - aboard + widthLine + winY),
		(aboard - widthLine + winY, - aboard + widthLine + winY)
		]

line_current = [
		(aboard - widthLine + winY, 3*paragraph),
		(aboard - widthLine + winX, 3*paragraph)
		]

