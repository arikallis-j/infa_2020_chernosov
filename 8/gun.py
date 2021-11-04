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
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
BALLS_COLOR = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

G = 1
N_target = 2
X0, Y0 = WIDTH//2, HEIGHT//2

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(BALLS_COLOR)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x>(WIDTH - 2*self.r - 2) or self.x<(2*self.r + 2):
            self.vx *= -1
        if self.y>(HEIGHT - 2*self.r - 2) or self.y<(2*self.r + 2):
            self.vy *= -1

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
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        return 0
        # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.x = rnd(600, 700)
        self.y = rnd(300, 500)
        self.r = rnd(2, 50)
        self.color = RED
        self.points = 0
        self.live = 1
        self.screen = screen
        self.vx = rnd(2, 5)
        self.vy = rnd(2, 5)
    def hit(self, points=1):
        self.points += points

    def move(self):
        if self.x>(WIDTH - 2*self.r - 2) or self.x<(2*self.r + 2):
            self.vx *= -1
        if self.y>(HEIGHT - 2*self.r - 2) or self.y<(2*self.r + 2):
            self.vy *= -1

        r = ((self.x - X0) ** 2 + (self.y - Y0) ** 2)**0.5

        ax = 10 * (X0 - self.x) / r**3
        ay = 10 * (Y0 - self.y) / r**3

        self.vx += ay
        self.vy -= ax

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

clock = pygame.time.Clock()
gun = Gun(screen)
for k in range(N_target):
    targets.append(Target(screen))
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for target in targets:
        target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for target in targets:
        target.move()
    for b in balls:
        b.move()
        if b.y > HEIGHT + b.r:
            balls.remove(b)
        for target in targets:
            if b.hittest(target) and target.live:
                target.live = 0
                target.hit()
                target.__init__(screen)
    gun.power_up()

pygame.quit()
