'''Рисует непрерывно движущиеся шарики и новые фигуры.
При щелчке внутри шарика добавляет одно очко.
При щелчке внутри новой фигуры добавляет два очка.
'''

import pygame
from pygame.draw import *
from random import randint
import csv

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
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

points = 0
balls = []
rects = []


def new_ball():
    '''Рисует новый шарик в случайных координатах
    и случайного радиуса'''
    ball = {'x': randint(100, 1100), 'y': randint(100, 900),
            'r': randint(10, 100), 'dx': 1, 'dy': 1, 'color': COLORS[randint(0, 5)]}
    return ball


def new_rect():
    '''Рисует новый квадрат в случайных координатах
    и случайных размеров'''
    global rct
    rct = {'x': randint(100, 1100), 'y': randint(100, 900),
           'width': randint(10, 50), 'height': randint(10, 50),
           'dx': 2, 'dy': 2, 'color': COLORS[randint(0, 5)]}
    return rct


def click_ball(event):
    '''Вычисляет, где произошел клик.
    Если внутри шарика, то выводит надпись "+1"
    и добавляет 1 очко к счетчику.
    '''
    global points
    if (ball['x'] ** 2 - event.pos[0] ** 2) + (ball['y'] ** 2 - event.pos[1] ** 2) <= ball['r'] ** 2:
        font1 = pygame.font.SysFont('courier', 45)
        follow1 = font1.render("+1", 1, WHITE)
        screen.blit(follow1, event.pos)
        pygame.display.update()
        print('+')
        points += 1
    else:
        print('-')


def click_rect(event):
    '''Вычисляет, где произошел клик.
    Если внутри прямоугольника, то выводит надпись "+2"
    и добавляет 2 очка к счетчику.
    '''
    global points
    if 0 <= event.pos[0] - rct['x'] <= rct['width']:
        if 0 <= event.pos[1] - rct['y'] <= rct['height']:
            font2 = pygame.font.SysFont('courier', 45)
            follow2 = font2.render("+2", 1, WHITE)
            screen.blit(follow2, event.pos)
            pygame.display.update()
            print('+2')
            points += 2
        else:
            print('-')


pygame.display.update()
clock = pygame.time.Clock()
finished = False

# начало цикла
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_ball(event)
            click_rect(event)

    # определяем количество шариков
    while len(balls) < 3:
        new_ball()
        balls.append(new_ball())

    # определяем количество прямоугольников
    while len(rects) < 3:
        new_rect()
        rects.append(new_rect())

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

    # рисуем прямоугольники итерацией по словарям в списке rects
    for rct in rects:
        rect(surface=screen, color=rct['color'], rect=(rct['x'], rct['y'], rct['width'], rct['height']))
        rct['x'] += rct['dx']
        rct['y'] += rct['dy']
        # для отражения прямоугольника при столкновении с границами экрана по осям х и у
        if rct['x'] <= 0 or rct['x'] >= (screen.get_width() - rct['width']):
            if -4 < rct['dx'] < 4:
                rct['dx'] *= -2
            else:
                rct['dx'] *= -0.75
        if rct['y'] > (screen.get_height() - rct['height']) or rct['y'] <= 0:
            if -3 < rct['dy'] < 3:
                rct['dy'] *= -2
            else:
                rct['dy'] *= -0.75

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

print("Вы набрали ", points, " очков")
name = input('Введите свое имя: ')

with open('game_results.csv', 'a+', newline='') as csvfile:
    resultwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    resultwriter.writerow('{} - {} очков'.format(name, points))

