import pygame
from pygame.draw import *

pygame.init()

FPS = 30
A = 400
M = 2
a = A//2

grey = (197,197,197)
yellow  = (255,255,0)
red  = (255,0,0)
black = (2,2,2)


r, R, P = M*8, M*12, M*50
x, X, H = M*(20)+a, M*(-20)+a, M*(0) + a
y, Y, I = M*(-10)+a, M*(-10)+a, M*(0) + a

#C, D, c, d = 0,0,0,0
#A, B, a, b = 0,0,0,0
E, F, e, f = -20*M+a,20*M+a,40*M,10*M

screen = pygame.display.set_mode((A, A))
screen.fill(grey)

circle(screen, yellow, (H,I), P, P)
circle(screen, black, (H,I), P, 1)
circle(screen, red, (x,y), r, r)
circle(screen, black, (x,y), r, 1)
circle(screen, red, (X,Y), R, R)
circle(screen, black, (X,Y), R, 1)
circle(screen, black, (x,y), r//2, r//2)
circle(screen, black, (X,Y), R//2, R//2)
rect(screen, black, (E, F, e, f))
polygon(screen, black, [(X+20,Y-R-3), (X-60,Y-60-R),
                               (X+20,Y-R-3)], R)
polygon(screen, black, [(x-18,y-r+3), (x+60,y-60-r),
                               (x-18,y-r+3)], r)
#rect(screen, (255, 0, 255), (100, 100, 200, 200))
#circle(screen, (255, 255, 255), (200, 175), 50, 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()