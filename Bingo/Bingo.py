import pygame, sys, os, random, math

#-----------------------------------#
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Bingo Board')

WINDOW_SIZE = (800, 800)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

display = pygame.Surface((400, 400))
#-----------------------------------#
 
font = pygame.font.SysFont(None, 20)

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

click = False
mouse = [0, 0]
tiles = []
tile_size = 80

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def random_board(challenges):
    temp_list = challenges.copy()
    while len(temp_list) < 25: # if there are less then 25 items in challenges, the code will break.
        temp_list.append(0)
    output = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for row in range(0, len(output)):
        for column in range(0, len(output[row])):
            index = random.randint(0, (len(temp_list) - 1))
            output[row][column] = temp_list[index]
            temp_list.pop(index)
    return output

def generate_tiles():
    tiles = []
    board = random_board(input_list)

    for row in range(0, 5):
        for column in range(0, 5):
            tiles.append(Tile(((column * tile_size), (row * tile_size)), board[row][column]))
    return tiles

class Tile:
    def __init__(self, loc, title):
        self.x = loc[0]
        self.y = loc[1]
        self.title = title
        self.state = False
    
    def toggle(self):
        if self.state:
            self.state = False
        else:
            self.state = True

    def rect(self, size):
        return pygame.Rect(self.x, self.y, size, size)


tiles = generate_tiles()
#----------------------This is turned off because Bingo_extra doesn't work with this-------------------------------------#
while True:
    display.fill((0, 0, 0))

    mouse[0], mouse[1] = pygame.mouse.get_pos()
    mouse[0] = (mouse[0] / 2)
    mouse[1] = (mouse[1] / 2)

    for item in tiles:
        if item.state:
            pygame.draw.rect(display, (40, 40, 40), item.rect(tile_size))
        else:
            pygame.draw.rect(display, (80, 80, 80), item.rect(tile_size))
        pygame.draw.rect(display, (100, 100, 100), item.rect(tile_size), 2)
        draw_text('{}'.format(item.title), font, (255, 255, 255), display, (item.x + 35), (item.y + 20))
        if click:
            if item.rect(80).collidepoint((mouse[0], mouse[1])):
                item.toggle()

    click = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
            if event.button == 3:
                tiles = generate_tiles()

    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    mainClock.tick(60)