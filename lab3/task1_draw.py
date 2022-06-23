import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen_height = 500
screen_width = 500
screen = pygame.display.set_mode((screen_height, screen_width))

x, y = screen_height / 2, screen_width / 2
R = screen_height / 4

R_left_eye_max = R / 6
R_left_eye_min = R / 12
x_left_eye = x - 50
y_left_eye = y - 40

R_right_eye_max = R / 8
R_right_eye_min = R / 14
x_right_eye = x + 50
y_right_eye = y - 40

x_left_eyebrow = x_left_eye + R_left_eye_max * 0.7
y_left_eyebrow = y_left_eye - R_left_eye_max * 0.9

x_right_eyebrow = x_right_eye - R_left_eye_max * 0.7
y_right_eyebrow = y_right_eye - R_left_eye_max * 0.8

x_mouth = x
y_mouth = y + R * 0.6
'''
y_left_eyebrow = y_left_eye - ((R_left_eye_max ** 2 - x_left_eyebrow ** 2) ** 0.5)
x_start_pos_left_eyebrow = x_left_eyebrow + R_left_eye_max
y_start_pos_left_eyebrow = y_left_eyebrow + R_left_eye_max
x_end_pos_left_eyebrow = x_left_eyebrow - 2*R_left_eye_max
y_end_pos_left_eyebrow = y_left_eyebrow - 2*R_left_eye_max
start_pos_left_eyebrow = (x_start_pos_left_eyebrow, y_start_pos_left_eyebrow)
end_pos_left_eyebrow = (x_end_pos_left_eyebrow, y_end_pos_left_eyebrow)
'''



def main():
    draw_face(x, y, R)
    draw_left_eye(x_left_eye, y_left_eye, R_left_eye_max, R_left_eye_min)
    draw_right_eye(x_right_eye, y_right_eye, R_right_eye_max, R_right_eye_min)
    draw_left_eyebrow(x_left_eyebrow, y_left_eyebrow)
    #draw_left_eyebrow(x_left_eyebrow, y_left_eyebrow, x_start_pos_left_eyebrow, y_start_pos_left_eyebrow, x_end_pos_left_eyebrow, y_end_pos_left_eyebrow)
    draw_right_eyebrow(x_right_eyebrow, y_right_eyebrow)
    draw_mouth(x_mouth, y_mouth)


def draw_face(x, y, R):
    rect(screen, "gray", (0, 0, screen_height, screen_width))
    circle(screen, "yellow", (x, y), R)
    circle(screen, "black", (x, y), R, 2)


def draw_left_eye(x_left_eye, y_left_eye, R_left_eye_max, R_left_eye_min):
    circle(screen, "red", (x_left_eye, y_left_eye), R_left_eye_max)
    circle(screen, "black", (x_left_eye, y_left_eye), R_left_eye_min)
    circle(screen, "black", (x_left_eye, y_left_eye), R_left_eye_max, 1)


def draw_right_eye(x_right_eye, y_right_eye, R_right_eye_max, R_right_eye_min):
    circle(screen, "red", (x_right_eye, y_right_eye), R_right_eye_max)
    circle(screen, "black", (x_right_eye, y_right_eye), R_right_eye_min)
    circle(screen, "black", (x_right_eye, y_right_eye), R_right_eye_max, 1)


def draw_left_eyebrow(x_left_eyebrow, y_left_eyebrow):
    line(screen, "black", [x_left_eyebrow + 15, y_left_eyebrow + 10],
         [x_left_eyebrow - 60, y_left_eyebrow - 40], 10)


def draw_right_eyebrow(x_right_eyebrow, y_right_eyebrow):
    line(screen, "black", [x_right_eyebrow - 15, y_right_eyebrow + 5],
         [x_right_eyebrow + 75, y_right_eyebrow - 25], 10)


def draw_mouth(x_mouth, y_mouth):
    line(screen, "black", (x_mouth - R/2, y_mouth), (x_mouth + R/2, y_mouth), 15)


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