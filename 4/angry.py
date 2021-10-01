import pygame
from pygame.draw import *

pygame.init()

FPS = 30

#масштаб
A = 400
a = A//2
M = 2

#цвета
grey = (197,197,197)
yellow  = (255,255,0)
red  = (255,0,0)
black = (2,2,2)

#массивы координат
Radius = [50, 8, 12, 40, 10]
Xcoord = [ 0, 20, -20,-20]
Ycoord = [0 ,-10, -10, 20 ]
Xbrows = [-6,30,10,-30]
Ybrows = [-3,-34,-8,-36]

#функция масштабирования
def mu(A):
    for k in range(len(A)):
        A[k] = A[k]*M
#функция сдвига 
def fi(A):
    for k in range(len(A)):
        A[k] = A[k] + a

#Увеличение масштаба рисунка
mu(Radius)
mu(Xcoord)
mu(Ycoord)
mu(Xbrows)
mu(Ybrows)
#Сдвиг по координатам
fi(Xcoord)
fi(Ycoord)

#отрисовка экрана
screen = pygame.display.set_mode((A, A))
screen.fill(grey)

#Его китайское лицо
circle(screen, yellow, (Xcoord[0],Ycoord[0]), Radius[0], Radius[0])
circle(screen, black, (Xcoord[0],Ycoord[0]), Radius[0], 1)

#Его левый глаз
circle(screen, red, (Xcoord[1],Ycoord[1]), Radius[1], Radius[1])
circle(screen, black, (Xcoord[1],Ycoord[1]), Radius[1], 1)
circle(screen, black, (Xcoord[1],Ycoord[1]), Radius[1]//2, Radius[1]//2)

#Его правый глаз
circle(screen, red, (Xcoord[2],Ycoord[2]), Radius[2], Radius[2])
circle(screen, black, (Xcoord[2],Ycoord[2]), Radius[2], 1)
circle(screen, black, (Xcoord[2],Ycoord[2]), Radius[2]//2, Radius[2]//2)

#Его неулыбчивый гонконгский рот
rect(screen, black, (Xcoord[3], Ycoord[3], Radius[3], Radius[4]))

#Его брежневские пышные брови
polygon(screen, black, [(Xcoord[1]+Xbrows[0], Ycoord[1]+Ybrows[0]), 
                        (Xcoord[1]+Xbrows[1],Ycoord[1]+Ybrows[1]), 
                        (Xcoord[1]+Xbrows[0],Ycoord[1]+Ybrows[0])], 
                        Radius[1])
polygon(screen, black, [(Xcoord[2]+Xbrows[2], Ycoord[2]+Ybrows[2]), 
                        (Xcoord[2]+Xbrows[3],Ycoord[2]+Ybrows[3]), 
                        (Xcoord[2]+Xbrows[2],Ycoord[2]+Ybrows[2])], 
                        Radius[2])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()