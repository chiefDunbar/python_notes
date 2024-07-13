# WRITE YOUR SOLUTION HERE:

import pygame
import random

def appear():
    x = random.randint(0, 640 - width)
    y = random.randint(0, 480 - height)
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    return (x, y)

def on_robot(previous, pos):
    return previous[0] <= pos[0] <= previous[0] + width and previous[1] <= pos[1] <= previous[1] + height


pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
width, height = robot.get_width(), robot.get_height()
previous = appear()


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and on_robot(previous, event.pos):
            previous = appear()
        
        if event.type == pygame.QUIT:
            exit()
