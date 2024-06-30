# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
# # WRITE YOUR SOLUTION HERE:

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")
width, height = ball.get_width(), ball.get_height()

x, y = random.randint(0, 640), random.randint(0, 480)
velocity = {'x': 1, 'y': 1}

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))    
    
    if x + width >= 640:
        velocity['x'] = -velocity['x']
    if y + height >= 480:
        velocity['y'] = -velocity['y']
    if x <= 0:
        velocity['x'] = -velocity['x']
    if y <= 0:
        velocity['y'] = -velocity['y']
    
    screen.blit(ball, (x, y)) 
    pygame.display.flip()

    x += velocity['x']
    y += velocity['y']

    clock.tick(330)

    