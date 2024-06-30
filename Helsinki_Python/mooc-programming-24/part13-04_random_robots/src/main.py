# WRITE YOUR SOLUTION HERE:



import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
window.fill((0, 0, 0))

robot = pygame.image.load("robot.png")
width, height = robot.get_width(), robot.get_height()

for _ in range(1000):
    x, y = random.randint(0, 640 - width), random.randint(0, 480 - height)
    window.blit(robot, (x, y)) 

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()