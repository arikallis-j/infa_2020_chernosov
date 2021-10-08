import pygame

pygame.init()

#отрисовка кадров
FPS = 60
clock = pygame.time.Clock()


#экран
back_color = (255,255,255)
X_win = 1000
Y_win = 1000

win = pygame.display.set_mode((X_win,Y_win))
pygame.display.set_caption("make-a-person")



run = True

while run:

    clock.tick(FPS)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    win.fill(back_color)


    pygame.display.update()

pygame.quit()