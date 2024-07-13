# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()

positions = [{'x': 320 - robot.get_width() / 2, 'y': 0}, {'x': 320 - robot.get_width() / 2, 'y': 480 - robot.get_height()}]
directions = [{'right': False, 'left': False, 'up': False, 'down': False} for _ in range(2)]

clock = pygame.time.Clock()

def action(screen, position, direction):
    if direction['right'] and position['x'] + robot.get_width() <= 640:
        position['x'] += 2
    if direction['left'] and position['x'] >= 0:
        position['x'] -= 2
    if direction['up'] and position['y'] >= 0:
        position['y'] -= 2
    if direction['down'] and  position['y'] + robot.get_height() <= 480:
        position['y'] += 2

    screen.blit(robot, (position['x'], position['y']))

def decision(event, directions):
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_a:
            directions[0]['left'] = True
        if event.key == pygame.K_w:
            directions[0]['up'] = True
        if event.key == pygame.K_d:
            directions[0]['right'] = True
        if event.key == pygame.K_s:
            directions[0]['down'] = True

        if event.key == pygame.K_LEFT:
            directions[1]['left'] = True
        if event.key == pygame.K_RIGHT:
            directions[1]['right'] = True
        if event.key == pygame.K_UP:
            directions[1]['up'] = True
        if event.key == pygame.K_DOWN:
            directions[1]['down'] = True

    if event.type == pygame.KEYUP:

        if event.key == pygame.K_a:
            directions[0]['left'] = False
        if event.key == pygame.K_w:
            directions[0]['up'] = False
        if event.key == pygame.K_d:
            directions[0]['right'] = False
        if event.key == pygame.K_s:
            directions[0]['down'] = False

        if event.key == pygame.K_LEFT:
            directions[1]['left'] = False
        if event.key == pygame.K_RIGHT:
            directions[1]['right'] = False
        if event.key == pygame.K_UP:
            directions[1]['up'] = False
        if event.key == pygame.K_DOWN:
            directions[1]['down'] = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        decision(event, directions)

    screen.fill((0, 0, 0))

    for position, direction in zip(positions, directions):
        action(screen, position, direction)
    
    pygame.display.flip()

    clock.tick(60)