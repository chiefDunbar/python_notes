import pygame
from datetime import datetime
import math


pygame.init()
screen = pygame.display.set_mode((640, 480))
center = (640 / 2, 480 / 2)

clock = pygame.time.Clock()

def display_circle():
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), center, 10)
    pygame.draw.circle(screen, (255, 0, 0), center, 100, 3)

def display_second(second):
    angle = 2 * math.pi * second / 60 - math.pi / 2
    end = (center[0] + 90 * math.cos(angle), center[1] + 90 * math.sin(angle))
    pygame.draw.line(screen, (0, 0, 255), center, end, 2)

def display_minute(minute):
    angle = 2 * math.pi * minute / 60 - math.pi / 2
    end = (center[0] + 80 * math.cos(angle), center[1] + 80 * math.sin(angle))
    pygame.draw.line(screen, (0, 0, 255), center, end, 3)

def display_hour(hour):
    hour %= 12
    angle = 2 * math.pi * hour / 12 - math.pi / 2
    end = (center[0] + 50 * math.cos(angle), center[1] + 50 * math.sin(angle))
    pygame.draw.line(screen, (0, 0, 255), center, end, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        current_time = datetime.now()
        
        display_circle()
        display_second(current_time.second)
        display_minute(current_time.minute)
        display_hour(current_time.hour)
        pygame.display.flip()

        clock.tick(1)
        