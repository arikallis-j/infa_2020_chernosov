import pygame
from pygame.draw import *

pygame.init()

FPS = 30
A = 800
bg = pygame.image.load("2.png")

screen = pygame.display.set_mode((2*A, A))
screen.fill((255,255,255))
screen.blit(bg, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()