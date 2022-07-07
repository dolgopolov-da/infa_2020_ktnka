'''Рисует непрерывно движущиеся шарики.
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

points = 0
balls = []

def new_ball():
    '''Рисует новый шарик в случайных координатах
    и случайного радиуса'''
    ball = {'x':randint(100, 1100), 'y':randint(100, 900),
            'r':randint(10, 100), 'dx':1, 'dy':1, 'color':COLORS[randint(0, 5)]}
    #circle(screen, color, (x, y), r)
    return ball


def click(event):
    '''Вычисляет, где произошел клик.
    Если внутри шарика, то выводит надпись "+1"
    и добавляет 1 очко к счетчику
    '''
    global points
    if (ball['x']**2 - event.pos[0]**2) + (ball['y']**2 - event.pos[1]**2) <= ball['r']**2:
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


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print("Вы набрали ", points, " очков")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    # определяем количество шариков
    while len(balls) < 3:
        new_ball()
        balls.append(new_ball())

    # рисуем шарики итерацией по словарям в списке balls
    for ball in balls:
        circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])
        ball['x'] += ball['dx']
        ball['y'] += ball['dy']

        # для отражения шарика при столкновении с границами экрана по осям х и у
        if ball['x'] > (screen.get_width() - ball['r']) or ball['x'] < ball['r']:
            ball['dx'] *= -1
        if ball['y'] > (screen.get_height() - ball['r']) or ball['y'] < ball['r']:
            ball['dy'] *= -1

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()