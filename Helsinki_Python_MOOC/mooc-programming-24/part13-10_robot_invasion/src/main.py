# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width, height = robot.get_width(), robot.get_height()

robots = list()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    if random.random() >= 0.99:
        robots.append({
            'x': random.randint(0, 640 - width), 
            'y': -height})
    
    screen.fill((0, 0, 0))
    for r in robots:
        screen.blit(robot, (r['x'], r['y']))
        if r['y'] + height >= 480:
            if r['x'] < 640 / 2:
                r['x'] -= 1
            else:
                r['x'] += 1
            continue 
        r['y'] += 1
    pygame.display.flip()

    clock.tick(60)

