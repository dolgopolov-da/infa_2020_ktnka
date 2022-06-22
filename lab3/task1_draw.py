import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen_height = 500
screen_width = 500
screen = pygame.display.set_mode((screen_height, screen_width))

def main():
    x, y = screen_height/2, screen_width/2
    R = screen_height/4

    draw_angry_smile(x, y, R)


def draw_angry_smile(x, y, R):
    draw_face(x, y, R)
    draw_left_eye(x, y, R)
    draw_right_eye(x, y, R)
    draw_left_eyebrow()
    draw_right_eyebrow()
    draw_mouth()


def draw_face(x, y, R):
    rect(screen, "gray", (0, 0, screen_height, screen_width))
    circle(screen, "yellow", (x, y), R)
    circle(screen, "black", (x, y), R, 2)


def draw_left_eye(x, y, R):
    R_left_eye_max = R / 6
    R_left_eye_min = R / 12
    x_left_eye = x - 50
    y_left_eye = y - 40
    circle(screen, "red", (x_left_eye, y_left_eye), R_left_eye_max)
    circle(screen, "black", (x_left_eye, y_left_eye), R_left_eye_min)
    circle(screen, "black", (x_left_eye, y_left_eye), R_left_eye_max, 1)


def draw_right_eye(x, y, R):
    R_right_eye_max = R / 8
    R_right_eye_min = R / 14
    x_right_eye = x + 50
    y_right_eye = y - 40
    circle(screen, "red", (x_right_eye, y_right_eye), R_right_eye_max)
    circle(screen, "black", (x_right_eye, y_right_eye), R_right_eye_min)
    circle(screen, "black", (x_right_eye, y_right_eye), R_right_eye_max, 1)


def draw_left_eyebrow():
    pass


def draw_right_eyebrow():
    pass


def draw_mouth():
    pass


main()

'''
rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)
'''


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()