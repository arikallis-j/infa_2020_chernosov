import pygame
 
pygame.init()
 
W = 1000
H = 1000
 
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Класс Surface")
pygame.display.set_icon(pygame.image.load("head.png"))
 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
FPS = 60        # число кадров в секунду
clock = pygame.time.Clock()
 
surf = pygame.Surface((W, 200))
bita = pygame.Surface((50, 10))
 
dog_surf = pygame.image.load('head.png')
dog_rect = dog_surf.get_rect(
    bottomright=(W, H))
sc.blit(dog_surf, dog_rect)

surf.fill(BLUE)
bita.fill(RED)
 
bx, by = 0, 150
x, y = 0, 0
 
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    surf.fill(BLUE)
    surf.blit(bita, (bx, by))
    dog_rect = dog_surf.get_rect(
    bottomright=(W, H))
sc.blit(dog_surf, dog_rect)
    sc.blit(dog_surf, dog_rect)
    if bx < W:
        bx += 5
    else:
        bx = 0
 
    if y < H:
        y += 1
    else:
        y = 0
 
    sc.fill(WHITE)
    sc.blit(surf, (x, y))
    pygame.display.update()
 
    clock.tick(FPS)





import pygame as pg
import sys
 
W = 1000
H = 1000
WHITE = (255,255,255)

sc = pg.display.set_mode((W, H))
sc.fill(WHITE)
 
dog_surf = pg.image.load('head.png')
dog_rect = dog_surf.get_rect(
    bottomright=(W, H))
sc.blit(dog_surf, dog_rect)
 
pg.display.update()
 
while 1:

    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
 
    pg.time.delay(20)