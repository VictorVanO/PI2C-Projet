#ref : https://inventwithpython.com/invent4thed/chapter15.html

from msilib.schema import Directory
from winreg import DisableReflectionKey


width, height = 8


def drawBoard(board):
    print('  12345678')
    print(' +--------+')
    for y in range(height):
        print('%s|' % (y+1), end='')
        for x in range(width):
            print(board[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')

def getNewBoard():
    board = []
    for i in range(width):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if 

def moves(board, tile):
    moves = []
    for x in range(width):
        for y in range(height):
            if moves(board, tile, x, y) != False:

                

def opponentMove():
    pass
