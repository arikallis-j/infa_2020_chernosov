import pygame

pygame.init()

#отрисовка кадров
FPS = 60
clock = pygame.time.Clock()
alpha = 150
speed = 5

#экран
back_color = (255,255,255)
X_win = 1000
Y_win = 1000
win = pygame.display.set_mode((X_win,Y_win))
pygame.display.set_caption("make-a-person")

#загрузка изображений
bg = pygame.image.load('images/bg.png')
parts_img = [pygame.image.load('images/bodyq.png'),
             pygame.image.load('images/head.png'),
             pygame.image.load('images/hand.png'),
             pygame.image.load('images/hair.png'),
             pygame.image.load('images/mouth.png'),
             pygame.image.load('images/nose.png'),
             pygame.image.load('images/eye.png'),
             pygame.image.load('images/eye.png')]

#координаты частей       
body = [0,0]
head = [0,0]
hand = [0,0]
hair = [0,0]
mouth = [0,0]
nose = [0,0]
eyeLeft = [0,0]
eyeRight = [0,0]
parts = [body,head, hand, hair, mouth, nose, eyeLeft, eyeRight]
J = [7,6,5,4,3,2,1,0]
n = 0


#обновление порядка покрытия
def update():
    global n
    global J
    AlphaBet = J
    AlphaBet.remove(n)
    AlphaBet.insert(7,n)
    J = AlphaBet


#функция отрисовки
def drawWindow():
    win.blit(bg, (0,0))
    for j in range(8):
        for i in range(8):
            if i==J[j]:
                win.blit(parts_img[i],(parts[i][0],parts[i][1]))

#функция проверки выхода
def check_stand():
    global run
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

#функция проверки клавищ
def check_move():
    global n
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        n = 0
    elif keys[pygame.K_2]:
        n = 1
    elif keys[pygame.K_3]:
        n = 2
    elif keys[pygame.K_4]:
        n = 3
    elif keys[pygame.K_5]:
        n = 4
    elif keys[pygame.K_6]:
        n = 5
    elif keys[pygame.K_7]:
        n = 6
    elif keys[pygame.K_8]:
        n = 7
    elif keys[pygame.K_0]:
        exit()

    x, y = parts[n][0], parts[n][1]

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed
    parts[n][0], parts[n][1] = x, y



#бесконечный цикл
run = True

while run:
    clock.tick(FPS)
    check_stand()
    check_move()
    update()
    drawWindow()
    pygame.display.update()

pygame.quit()