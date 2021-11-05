import math
from random import choice
from random import randint

import pygame

def rnd(x,y):
    return randint(x,y)

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
SAND = 0xFCDD76
BROWN = 0x801818
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, SAND]
BALLS_COLOR = [BLUE,RED]
GUN_COLOR = [BLUE,RED]
POINT_COLOR = [BLUE,RED]
TARGET_COLOR = GREEN
DOWN_COLOR = GREY
WIDTH = 800
HEIGHT = 600
ABOARD = 50
R_BALL, R_GUN, R_TANK , R_POINT = 5, 10, 20, 2

G = 1
N_target, N_gun = 2, 2
X0, Y0 = WIDTH//2, HEIGHT//2
gun_x, gun_y = WIDTH//2, HEIGHT - ABOARD - R_TANK
V_point = 10

class Ball:
    def __init__(self, screen: pygame.Surface, type,  x=gun_x, y=gun_y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.type = type
        self.screen = screen
        self.x = x
        self.y = y
        self.r = R_BALL
        self.vx = 0
        self.vy = 0
        self.color = BALLS_COLOR[type-1]
        self.live = 30
        self.reflect = 0
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x>(WIDTH - 2*self.r - 2) or self.x<(2*self.r + 2):
            self.vx *= -1
            self.reflect += 1
        if self.y>(HEIGHT - ABOARD) or self.y<(ABOARD):
            self.vy *= -1
            self.reflect += 1

        self.vy += 0
        self.vy -= G

        self.x += self.vx
        self.y -= self.vy



    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        hit = False
        R_2 = (self.x-obj.x)**2 + (self.y-obj.y)**2
        R = R_2**0.5
        if R<(self.r+obj.r):
            hit = True
        return hit


class Gun:
    def __init__(self, screen, type):
        self.type = type
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GUN_COLOR[type-1]
        self.x = gun_x + 100 * 2*(type - 1)
        self.y = gun_y
        self.r = R_GUN
        self.kill = False

        self.gORp = 1
        self.x_point = WIDTH//2 + 100 * 2*(type - 1)
        self.y_point = HEIGHT//2
        self.r_point = R_POINT
        self.color_point = POINT_COLOR[type-1]

    def move(self, X_MOVE, Y_MOVE):
        if self.gORp == -1:
            self.x_point += X_MOVE * V_point
            self.y_point += Y_MOVE * V_point

        if self.kill:
            return 0
        elif self.gORp == 1:
            self.x +=X_MOVE*V_point
    def fire2_start(self):
        if self.kill:
            return 0
        self.f2_on = 1

    def fire2_end(self):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        if self.kill:
            return 0
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.type, self.x,self.y)
        new_ball.r += 5
        self.an = math.atan2((self.y_point-new_ball.y), (self.x_point-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10


    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""
        if self.kill:
            return 0
        if self.x!=self.x_point:
            self.an = math.atan((self.y_point-self.y) / (self.x_point-self.x))
        if self.f2_on:
            self.color = GUN_COLOR[self.type-1]
        else:
            self.color = GUN_COLOR[self.type-1]

    def draw(self):
        if self.kill:
            self.color = GREY

        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x - 2*R_TANK, HEIGHT - ABOARD - R_TANK, 4*R_TANK, R_TANK)
        )
    def point(self):
        if self.kill:
            self.color = GREY
        pygame.draw.circle(
            self.screen,
            self.color_point,
            (self.x_point, self.y_point),
            self.r_point
        )

    def power_up(self):
        if self.kill:
            return 0
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = GREY
        else:
            self.color = GUN_COLOR[self.type-1]
    def killed(self):
        self.kill = True

class Target:
    def __init__(self, screen, type):
        self.type = type
        self.x = rnd(600, 700)
        self.y = rnd(300, 500)
        self.r = rnd(2, 50)
        self.color = TARGET_COLOR
        self.points = 0
        self.live = 1
        self.screen = screen
        self.vx = rnd(2, 5)
        self.vy = rnd(2, 5)
        self.ax = G
        self.ay = -G
        if type==1:
            self.ax = 0
        if type==2:
            self.ay = 0
    def hit(self, points=1):
        self.points += points

    def move(self):
        if self.x>(WIDTH - 2*self.r - 2) or self.x<(2*self.r + 2):
            self.vx *= -1
            self.ax *= -1/10
        if self.y>(HEIGHT - ABOARD - self.r) or self.y<(ABOARD + self.r):
            self.vy *= -1
            self.ay *= -1/10


        self.vx += self.ax
        self.vy -= self.ay

        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = []
guns = []
clock = pygame.time.Clock()

for k in range(N_gun):
    guns.append(Gun(screen, k+1))
for k in range(N_target):
    targets.append(Target(screen,k+1))
finished = False

while not finished:
    screen.fill(WHITE)
    for gun in guns:
        gun.draw()
    for target in targets:
        target.draw()
    for b in balls:
        b.draw()
    for gun in guns:
        gun.point()
    pygame.draw.rect(screen, DOWN_COLOR, (0, HEIGHT - ABOARD, WIDTH, ABOARD))
    pygame.display.update()

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT:
                guns[0].fire2_end()
            if event.key == pygame.K_LSHIFT:
                guns[0].gORp *= -1
            if event.key == pygame.K_RALT:
                guns[1].fire2_end()
            if event.key == pygame.K_RSHIFT:
                guns[1].gORp *= -1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL]:
        guns[0].fire2_start()
    x_move, y_move = 0, 0
    if keys[pygame.K_d]:
        x_move += 1
    if keys[pygame.K_a]:
        x_move -= 1
    if keys[pygame.K_s]:
        y_move += 1
    if keys[pygame.K_w]:
        y_move -= 1
    guns[0].move(x_move,y_move)
    if keys[pygame.K_RCTRL]:
        guns[1].fire2_start()
    x_move, y_move = 0, 0
    if keys[pygame.K_RIGHT]:
        x_move += 1
    if keys[pygame.K_LEFT]:
        x_move -= 1
    if keys[pygame.K_DOWN]:
        y_move += 1
    if keys[pygame.K_UP]:
        y_move -= 1
    guns[1].move(x_move,y_move)


    for target in targets:
        target.move()

    for b in balls:
        b.move()
        if b.reflect>1:
            balls.remove(b)
        for target in targets:
            if b.hittest(target) and target.live:
                target.live = 0
                target.hit()
                target.__init__(screen,target.type)
        for gun in guns:
            if b.hittest(gun) and gun.type!=b.type:
                gun.killed()

    for gun in guns:
        gun.power_up()


pygame.quit()
