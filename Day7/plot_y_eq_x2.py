import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x**2

pygame.init()

COLOR = (255, 255, 255)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
POINTS = 200

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draw quadratic function ")

running = True
previous_point = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    x = -2
    prev_x_cord = x * WINDOW_WIDTH//4 + WINDOW_WIDTH//2
    prev_y_cord = WINDOW_HEIGHT - (f(x) * WINDOW_WIDTH//4)

    for i in range(POINTS+1):
        # range_x [-2, 2] -> [0, 601]
        # range_y [4, 4] -> [0, 600]
        x_cord = x * WINDOW_WIDTH//4 + WINDOW_WIDTH//2
        y_cord = WINDOW_HEIGHT - (f(x) * WINDOW_WIDTH//4)
        pygame.draw.line(screen, COLOR, (prev_x_cord, prev_y_cord), (int(x_cord), int(y_cord)))
        x += 4/POINTS   

        prev_x_cord = x_cord
        prev_y_cord = y_cord
    pygame.display.flip()

pygame.quit()
