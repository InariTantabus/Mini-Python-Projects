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

def hilo(a, b, c): # I didn't write this
    if c < b: b, c = c, b
    if b < a: a, b = b, a
    if c < b: b, c = c, b
    return a + c

def complement(r, g, b): # I didn't write this
    k = hilo(r, g, b)
    return tuple(k - u for u in (r, g, b))

def generate_color_pallet(base_color):
    colors = []
    color_rects = []
    color_types = [1, 2, 3, 4]
    colors.append(base_color)
    color_rects.append(pygame.Rect(0, 0, 40, 40))
    for v in range(0, 4):
        temp_color = ()
        temp_color_list = [0, 0, 0]
        current_type = color_types[random.randint(0, len(color_types) - 1)]
        offset = (random.randrange(-5, 5), random.randrange(-5, 5), random.randrange(-5, 5))
        temp = 0
        if current_type == 1: # off base
            temp = max(base_color)
            for i in range(0, 3):
                if not base_color[i] == temp:
                    temp_color_list[i] = (base_color[i] + offset[i])
                    if temp_color_list[i] > 256:
                        temp_color_list[i] = 256
                    if temp_color_list[i] < 0:
                        temp_color_list[i] += (2  * (offset[i] * -1))
            temp_color = (temp_color_list[0], temp_color_list[1], temp_color_list[2])
            colors.append(temp_color)
            color_types.remove(1)
        elif current_type == 2: # opposite
            temp_color = complement(base_color[0], base_color[1], base_color[2])
            colors.append(temp_color)
            color_types.append(5)
            color_types.remove(2)
        elif current_type == 3: # grey
            for i in range(0, 3):
                temp += base_color[i]
            temp = int(temp / 3)
            temp_color = (temp, temp, temp)
            colors.append(temp_color)
            color_types.remove(3)
        elif current_type == 4: # random
            val_1 = random.randint(0, 255)
            val_2 = random.randint(0, 255)
            val_3 = random.randint(0, 255)
            rand_color = (val_1, val_2, val_3)
            colors.append(rand_color)
            color_types.append(6)
            color_types.remove(4)
        elif current_type == 5: # off opposite
            temp_color = complement(base_color[0], base_color[1], base_color[2])
            temp = max(temp_color)
            for i in range(0, 3):
                if not temp_color[i] == temp:
                    temp_color_list[i] = (temp_color_list[i] + offset[i])
                    if temp_color_list[i] > 256:
                        temp_color_list[i] = 256
                    if temp_color_list[i] < 0:
                        temp_color_list[i] += (2  * (offset[i] * -1))
            temp_color = (temp_color_list[0], temp_color_list[1], temp_color_list[2])
            colors.append(temp_color)
            color_types.remove(5)
        elif current_type == 6: # off random
            temp = max(rand_color)
            for i in range(0, 3):
                if not rand_color[i] == temp:
                    temp_color_list[i] = (rand_color[i] + offset[i])
                    if temp_color_list[i] > 256:
                        temp_color_list[i] = 256
                    if temp_color_list[i] < 0:
                        temp_color_list[i] += (2  * (offset[i] * -1))
            temp_color = (temp_color_list[0], temp_color_list[1], temp_color_list[2])
            colors.append(temp_color)
            color_types.remove(6)
        color_rects.append(pygame.Rect(((v + 1) * 40), 0, 40, 40))
    print(colors)
    return colors, color_rects

colors, color_rects = generate_color_pallet((134, 80, 140))
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
            colors, color_rects = generate_color_pallet((134, 80, 140))

    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    mainClock.tick(60)