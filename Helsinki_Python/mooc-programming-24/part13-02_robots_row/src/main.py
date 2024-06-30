# WRITE YOUR SOLUTION HERE:

# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
width, height = robot.get_width(), robot.get_height()
padding = 10
for i in range(10):
    window.blit(robot, (width + (width * i) + padding, height))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()