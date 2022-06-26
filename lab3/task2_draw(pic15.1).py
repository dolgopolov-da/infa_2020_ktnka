import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen_width = 500
screen_height = 800
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
    background = pygame.Surface((500, 800))
    rect(background, "paleturquoise4", (x, y, screen_width, y))
    rect(background, "lightsalmon1", (x, y * 0.8, screen_width, y * 0.2))
    rect(background, "palevioletred", (x, y * 0.5, screen_width, y * 0.3))
    rect(background, "orchid", (x, y * 0.3, screen_width, y * 0.2))
    rect(background, "purple", (x, y * 0.2, screen_width, y * 0.1))
    rect(background, "royalblue4", (x, 0, screen_width, y * 0.2))
    screen.blit(background, (0, 0))


def draw_seagull():
    '''Рисует большую чайку'''
    ellipse(screen, "white", (220-130/2, 580-70/2, 130, 70)) # body
    ellipse(screen, "white", (290-70/2, 575-25/2, 70, 25)) # neck
    ellipse(screen, "white", (335-50/2, 565-30/2, 50, 30)) # head
    circle(screen, "black", (343, 565), 4) # eye

    # draw leg 1 part 1
    leg1_1 = pygame.Surface((50, 25), pygame.SRCALPHA, 32)
    leg1_1 = leg1_1.convert_alpha()
    ellipse(leg1_1, "white", (0, 0, 50, 25))  # leg1
    leg1_1 = pygame.transform.rotate(leg1_1, -60)
    screen.blit(leg1_1, (200, 600))

    # draw leg 1 part 2
    leg1_2 = pygame.Surface((50, 15), pygame.SRCALPHA, 32)
    leg1_2 = leg1_2.convert_alpha()
    ellipse(leg1_2, "white", (0, 0, 50, 15))  # leg1
    leg1_2 = pygame.transform.rotate(leg1_2, -25)
    screen.blit(leg1_2, (220, 635))

    # draw leg 2 part 1
    leg2_1 = pygame.Surface((40, 20), pygame.SRCALPHA, 32)
    leg2_1 = leg2_1.convert_alpha()
    ellipse(leg2_1, "white", (0, 0, 40, 20))  # leg1
    leg2_1 = pygame.transform.rotate(leg2_1, -60)
    screen.blit(leg2_1, (225, 590))

    # draw leg 2 part 2
    leg2_2 = pygame.Surface((50, 15), pygame.SRCALPHA, 32)
    leg2_2 = leg2_2.convert_alpha()
    ellipse(leg2_2, "white", (0, 0, 50, 15))  # leg1
    leg2_2 = pygame.transform.rotate(leg2_2, -25)
    screen.blit(leg2_2, (240, 615))




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
