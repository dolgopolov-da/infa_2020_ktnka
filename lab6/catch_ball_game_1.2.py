'''Рисует непрерывно движущийся шарик (шарики).
При щелчке внутри шарика добавляет одно очко.
'''

import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x = randint(100, 1100)
y = randint(100, 900)
r = randint(10, 100)
color = COLORS[randint(0, 5)]
points = 0

def new_ball():
    '''Рисует новый шарик в случайных координатах
    и случайного радиуса'''
    circle(screen, color, (x, y), r)


def click(event):
    '''Вычисляет, где произошел клик.
    Если внутри шарика, то выводит надпись "+1"
    и добавляет 1 очко к счетчику
    '''
    global points
    if (x**2 - event.pos[0]**2) + (y**2 - event.pos[1]**2) <= r**2:
        font = pygame.font.SysFont('courier', 45)
        follow = font.render("+1", 1, WHITE)
        screen.blit(follow, event.pos)
        pygame.display.update()
        print('+')
        points += 1
    else:
        print('-')


pygame.display.update()
clock = pygame.time.Clock()
finished = False

dx = 1 # величина перемещения шарика за 1 кадр по оси х
dy = 1 # величина перемещения шарика за 1 кадр по оси у

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print("Вы набрали ", points, " очков")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    new_ball()
    x += dx
    y += dy

    if x > (screen.get_width() - r) or x < r: # для отражения шарика при столкновении с границей экрана по оси х
        dx *= -1
    if y > (screen.get_height() - r) or y < r: # для отражения шарика при столкновении с границей экрана по оси у
        dy *= -1
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()