# WRITE YOUR SOLUTION HERE:
# # WRITE YOUR SOLUTION HERE:

import pygame
import math

pygame.init()

screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width, height = robot.get_width(), robot.get_height()

angle_padding = 2 * math.pi / 10
x, y = [0] * 10, [0] * 10
    

clock = pygame.time.Clock()

angle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))    
    for i in range(10):
        x[i] = 320 + math.cos(angle_padding * i + angle) * 100 - width / 2
        y[i] = 240 + math.sin(angle_padding * i + angle) * 100 - height / 2
        screen.blit(robot, (x[i], y[i]))
    pygame.display.flip()

    angle += 0.01

    clock.tick(60)

    