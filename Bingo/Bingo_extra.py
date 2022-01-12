import sys, os
import Bingo as b

running = True
saved_num = 0
saved_board = []

while running:
    if saved_num >= 25:
        print(saved_num)
        print(saved_board)
        running = False

    board = b.random_board(b.input_list)
    new_board = []

    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            new_board.append(board[row][column])
    
    new_board.sort()

    for num in range(0, len(new_board)):
        if (num + 1) == new_board[num]:
            continue
        else:
            if saved_num < num:
                saved_num = num
                saved_board = board
            break