# WRITE YOUR SOLUTION HERE:
# # WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width, height = robot.get_width(), robot.get_height()
x_1, x_2, y_1, y_2 = 0, 0, height, height * 2
velocity_1, velocity_2 = 1, 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))
    
    x_1 += velocity_1
    x_2 += velocity_2

    screen.blit(robot, (x_1, y_1))
    screen.blit(robot, (x_2, y_2))
    pygame.display.flip()
    
    if velocity_1 > 0 and x_1 + width >= 640:
        velocity_1 = -velocity_1
    if velocity_1 < 0 and x_1 <= 0:
        velocity_1 = -velocity_1   
    
    if velocity_2 > 0 and x_2 + width >= 640:
        velocity_2 = -velocity_2
    if velocity_2 < 0 and x_2 <= 0:
        velocity_2 = -velocity_2
    
    clock.tick(100)

    