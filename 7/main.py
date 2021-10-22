import pygame
from pygame.draw import *
from classes import *
Data = init()
Picture = picture()
run = True
while run:
    Clock.tick(FPS)
    time = pygame.time.get_ticks()
    Picture.win.time = time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif time//1000>=maxTime:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Picture.basket.click(event)
    Picture.draw()
    pygame.display.update()

Picture.win.draw()
pygame.display.update()
Picture.win.new_record()
dataDown()

pygame.quit()