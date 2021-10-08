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


#загрузка изображений
bg = pygame.image.load('images/bg.png')
Parts = [pygame.image.load('images/body.png'),
         pygame.image.load('images/head.png'),
         pygame.image.load('images/hand.png'),
         pygame.image.load('images/hair.png'),
         pygame.image.load('images/mouth.png'),
         pygame.image.load('images/nose.png'),
         pygame.image.load('images/eye.png')]



#функция отрисовки
def drawWindow():
    win.blit(bg, (0,0))

run = True

while run:

    clock.tick(FPS)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    drawWindow()


    pygame.display.update()

pygame.quit()