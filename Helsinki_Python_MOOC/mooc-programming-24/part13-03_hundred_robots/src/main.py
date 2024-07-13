# WRITE YOUR SOLUTION HERE:



import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
window.fill((0, 0, 0))

robot = pygame.image.load("robot.png")
width, height = robot.get_width(), robot.get_height()

x_init_padding, x_padding = width, width - width // 4
y_init_padding, y_padding = height, height // 4

for r in range(1, 11):
    for c in range(10):
        window.blit(robot, (x_init_padding + x_padding * c, y_init_padding + y_padding * r))
        x_init_padding += x_padding // 20

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()