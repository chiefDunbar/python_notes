# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
w, h = robot.get_width(), robot.get_height()

x = 0
y = 0
clock = pygame.time.Clock()

velocity = 1
move_x = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if move_x:
        x += velocity

        if velocity == 1 and x + w >= 640:
            move_x = False
        if velocity == -1 and x <= 0:
            move_x = False

    else:
        y += velocity

        if velocity == 1 and y + h >= 480:
            move_x = True
            velocity = -velocity
        if velocity == -1 and y <= 0:
            move_x = True
            velocity = -velocity



    clock.tick(300)