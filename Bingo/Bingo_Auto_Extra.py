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

tiles = []
tile_size = 80
board = []

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
    return tiles, board

def find_average(ave):
    temp_num = 0
    for i in range(0, len(ave)):
        temp_num += ave[i]
    temp_num = int(temp_num / len(ave))
    return temp_num

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

saved_num = 0
saved_board = []
finished = True
current_val = 1
new_board = []
highest_num = 0
total_boards = -1
average_list = []
average = 0
last_board = 0

tiles, board = generate_tiles()
#----------------------This is turned off because Bingo_extra doesn't work with this-------------------------------------#
while True:
    display.fill((0, 0, 0))

    for item in tiles:
        if item.state:
            pygame.draw.rect(display, (40, 40, 40), item.rect(tile_size))
        else:
            pygame.draw.rect(display, (80, 80, 80), item.rect(tile_size))
        pygame.draw.rect(display, (100, 100, 100), item.rect(tile_size), 2)
        draw_text('{}'.format(item.title), font, (255, 255, 255), display, (item.x + 35), (item.y + 20))

    if not current_val > 25:
        if finished:
            total_boards += 1
            current_val = 1
            tiles, board = generate_tiles()
            new_board = []

            for row in range(0, len(board)):
                for column in range(0, len(board[row])):
                    new_board.append(board[row][column])
            new_board.sort(reverse=True)
            for i in range(0, 5):
                if new_board[i] == 30 or new_board[i] == 29 or new_board[i] == 28 or new_board[i] == 27 or new_board[i] == 26:
                   tiles, board = generate_tiles()
                   break 
            new_board.sort()
            finished = False

        if new_board[(current_val - 1)] == current_val:
            for row in range(0, 5):
                for column in range(0, 5):
                    if board[row][column] == current_val:
                        tiles[((row * 5) + column)].toggle()
            current_val += 1
        else:
            finished = True
        
        if finished:
            if highest_num < current_val:
                highest_num = current_val
    else:
        last_board = total_boards
        average_list.append(total_boards)
        current_val = 1
        total_boards = -1
        highest_num = 1
        average = find_average(average_list)
        finished = True

    draw_text('Boards checked: {}'.format(total_boards), font, (0, 255, 0), display, (5), (5))
    draw_text('Highest number: {}'.format(highest_num - 1), font, (255, 0, 0), display, (5), (85))
    draw_text('Average boards: {}'.format(average), font, (0, 0, 255), display, (5), (165))
    draw_text('Times finished: {}'.format(len(average_list)), font, (255, 255, 0), display, (5), (245))
    draw_text('Last boards checked: {}'.format(last_board), font, (255, 0, 255), display, (5), (325))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    mainClock.tick(1000)