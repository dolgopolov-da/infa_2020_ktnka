import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen_height = 800
screen_width = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# начальные координаты
x = 0
y = screen_height // 2


def main():
    '''Рисует картину целиком'''
    draw_background(x, y, screen_width)
    draw_seagull()
    draw_seagulls()
    draw_fish()


def draw_background(x, y, screen_width):
    '''Рисует задний фон'''
    rect(screen, "paleturquoise4", (x, y, screen_width, y))
    rect(screen, "lightsalmon1", (x, y * 0.8, screen_width, y * 0.2))
    rect(screen, "palevioletred", (x, y * 0.5, screen_width, y * 0.3))
    rect(screen, "orchid", (x, y * 0.3, screen_width, y * 0.2))
    rect(screen, "purple", (x, y * 0.2, screen_width, y * 0.1))
    rect(screen, "royalblue4", (x, 0, screen_width, y * 0.2))


def draw_seagull():
    ellipse(screen, "white", (220-130/2, 580-70/2, 130, 70)) # body
    ellipse(screen, "white", (290-70/2, 575-25/2, 70, 25)) # neck
    ellipse(screen, "white", (335-50/2, 565-30/2, 50, 30)) # head
    circle(screen, "black", (343, 565), 4) # eye









def draw_seagulls():
    pass


def draw_fish():
    pass


main()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
