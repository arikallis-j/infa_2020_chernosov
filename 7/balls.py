import pygame
from pygame.draw import *
from random import randint
from math import sin, cos, pi
pygame.init()

FPS = 60
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
font = pygame.font.SysFont('serif', 36)

count = 0
aboard = 5
N = 5

BALLS = []
def aboards():
    pygame.draw.lines(win, 
                      YELLOW, 
                      True,
                      [(aboard - widthLine, aboard - widthLine),
                       (aboard - widthLine + B, aboard - widthLine),
                       (aboard - widthLine + B, - aboard + widthLine + B),
                       (aboard - widthLine, - aboard + widthLine + B)],
                       width = widthLine)
def table():
    score_text = "Ваш счёт: " + str(count)
    score = font.render(score_text, True, YELLOW)
    win.blit(score, (B + aboard, 0))

def create_ball():
    speed = 5
    r = randint(10, 100)
    alpha = randint(0, 360)
    x = randint(r, B-r)
    y = randint(r, B-r)
    vx = round(speed*cos(alpha*pi/180))
    vy = round(speed*sin(alpha*pi/180))
    color = COLORS[randint(0, 5)]
    return {
            'r': r,
            'xy': [x,y],
            'v': [vx,vy],
            'color': color
            }

def balls_full():
    while len(BALLS)<N:
        BALLS.append(create_ball())

def draw(obj):
    circle(win, 
           obj['color'], 
           obj['xy'], 
           obj['r'])

def move(obj):
    x,y = obj['xy']
    r = obj['r']
    xwall = x < (aboard + r) or x > (B - aboard - r)
    ywall = y < (aboard + r) or y > (B - aboard - r)
    if xwall:
        obj['v'][0] = (-1)*obj['v'][0]
    if ywall:
        obj['v'][1] = (-1)*obj['v'][1]

    obj['xy'][0] += obj['v'][0]
    obj['xy'][1] += obj['v'][1]


def dance():
    aboards()
    table()
    balls_full()
    for ball in BALLS:
        draw(ball)
        move(ball)

def click():
    global count
    x1, y1 = event.pos
    for ball in BALLS:
        x,y = ball['xy']
        r = ball['r']
        run = ( (x1-x)**2 + (y1-y)**2 - r**2 ) < 0
        if run:
            count += 1
            BALLS.remove(ball)

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