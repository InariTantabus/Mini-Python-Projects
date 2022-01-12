import pygame, sys, os, random

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Color Pallet Generator')

WINDOW_SIZE = (400, 80)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

display = pygame.Surface((200, 40))

colors = []
color_rects = []

def generate_color_pallet():
    colors = []
    color_rects = []
    for i in range(0, 5):
        val_1 = random.randint(0, 255)
        val_2 = random.randint(0, 255)
        val_3 = random.randint(0, 255)
        colors.append((val_1, val_2, val_3))
        color_rects.append(pygame.Rect((i * 40), 0, 40, 40))
    print(colors)
    return colors, color_rects

colors, color_rects = generate_color_pallet()
while True:
    display.fill((0, 0, 0))
    for val in range(0, len(color_rects)):
        pygame.draw.rect(display, colors[val], color_rects[val])
        
    click = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            colors, color_rects = generate_color_pallet()

    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    mainClock.tick(60)