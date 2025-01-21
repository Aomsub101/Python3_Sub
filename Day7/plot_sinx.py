import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return math.sin(x)

pygame.init()

POINTS = 200
COLOR = (255 ,255, 255)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draw sine graph")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))
    x = -6
    prev_x = 0
    prev_y = WINDOW_HEIGHT//2
    # range_x [-6, 6]
    # range_y [-1, 1]
    for i in range(POINTS + 1):
        y = WINDOW_HEIGHT//2 - (f(-6 + (12 * x / WINDOW_WIDTH)) * WINDOW_HEIGHT//4)
        pygame.draw.line(screen, COLOR, (prev_x, prev_y), (x, y))
        prev_x = x
        prev_y = y
        x += WINDOW_WIDTH/POINTS

    pygame.display.flip()

pygame.quit()
