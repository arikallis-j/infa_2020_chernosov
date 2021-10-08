import pygame
from pygame.draw import *
from random import randint
from math import sin, cos, pi
pygame.init()

FPS = 120
A, B = 1200, 900
win = pygame.display.set_mode((A,B))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

widthLine = 3
font = pygame.font.SysFont('serif', 50)

count = 0
aboard = 5
paragraph = 50

level = "hard"
if level == "hard":
    speed = 5
elif level == "normal":
    speed = 3
elif level == "easy":
    speed = 2
else:
    speed = 0

Nballs = 5
Nboxes = 5

BALLS = []
BOXES = []

def aboards():
    pygame.draw.lines(win, 
                      YELLOW, 
                      True,
                      [(aboard - widthLine, aboard - widthLine),
                       (aboard - widthLine + B, aboard - widthLine),
                       (aboard - widthLine + B, - aboard + widthLine + B),
                       (aboard - widthLine, - aboard + widthLine + B)],
                       width = widthLine)
    pygame.draw.lines(win, 
                      YELLOW, 
                      True,
                      [(aboard - widthLine + B, aboard - widthLine),
                       (-aboard + widthLine + A, aboard - widthLine),
                       (-aboard + widthLine + A, - aboard + widthLine + B),
                       (aboard - widthLine + B, - aboard + widthLine + B)],
                       width = widthLine)
    pygame.draw.lines(win, 
                      YELLOW, 
                      True,
                      [(aboard - widthLine + B, 100),
                       (aboard - widthLine + A, 100)],
                       width = widthLine)

def table():
    level_text = "Level: " + level
    score_text = "Score: " + str(count)

    Score = font.render(score_text, True, YELLOW)
    Level = font.render(level_text, True, YELLOW)
    win.blit(Score, (B + 2*aboard, 0))
    win.blit(Level, (B + 2*aboard, paragraph))



def create_ball():
    global speed
    r = randint(10, 100)
    alpha = randint(0, 360)
    x = randint(r, B-r)
    y = randint(r, B-r)
    vx = round(speed*cos(alpha*pi/180))
    vy = round(speed*sin(alpha*pi/180))
    color = COLORS[randint(0, 5)]
    return {
            'type': "ball",
            'r': r,
            'xy': [x,y],
            'v': [vx,vy],
            'color': color,
            'boards': [aboard + r, B - aboard - r, aboard + r, B - aboard - r],
            'count': 1
            }

def create_box():
    global speed
    r = randint(10, 100)
    alpha = randint(0, 360)
    x = randint(r, B-r)
    y = randint(r, B-r)
    vx = round(speed*cos(alpha*pi/180) + speed**2/2)
    vy = round(speed*sin(alpha*pi/180) + speed**2/2)
    color = COLORS[randint(0, 5)]
    return {
            'type': "box",
            'r': r,
            'xy': [x,y],
            'xyrr': [x, y ,r ,r],
            'v': [vx,vy],
            'boards': [aboard,B -r,aboard, B - aboard - r],
            'color': color,
            'count': 5
            }

def balls_full():
    while len(BALLS)<Nballs:
        BALLS.append(create_ball())

def boxes_full():
    while len(BOXES)<Nboxes:
        BOXES.append(create_box())

def drawBase(obj):
    circle(win, 
           obj['color'], 
           obj['xy'], 
           obj['r'])

def drawOther(obj):
    rect(win, 
         obj['color'], 
        (obj['xy'], 
        (obj['r'],obj['r'])))

def move(obj):
    x,y = obj['xy']
    r = obj['r']
    xwall = x < obj['boards'][0]  or x > obj['boards'][1]
    ywall = y < obj['boards'][2] or y > obj['boards'][3]
    if xwall:
        obj['v'][0] = (-1)*obj['v'][0]
    if ywall:
        obj['v'][1] = (-1)*obj['v'][1]

    obj['xy'][0] += obj['v'][0]
    obj['xy'][1] += obj['v'][1]
    #crush(obj)


def dance():
    aboards()
    table()
    balls_full()
    boxes_full()
    for ball in BALLS:
        drawBase(ball)
        move(ball)
    for box in BOXES:
        drawOther(box)
        move(box)

def click():
    global count
    x1, y1 = event.pos
    for ball in BALLS:
        x,y = ball['xy']
        r = ball['r']
        run = ( (x1-x)**2 + (y1-y)**2 - r**2 ) < 0
        if run:
            count += ball['count']
            BALLS.remove(ball)
    for box in BOXES:
        x,y = box['xy']
        r = box['r']
        run = ( (x1-x)**2 + (y1-y)**2 - r**2 ) < 0
        if run:
            count += box['count']
            BOXES.remove(box)

pygame.display.update()
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click()
    win.fill(BLACK)
    dance()    

    pygame.display.update()
    

pygame.quit()