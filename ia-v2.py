#reference : https://inventwithpython.com/invent4thed/chapter15.html
import random
import sys

width = 8
height = 8
compteurDeTour = 1
'''
coup = 44
def test(message,opponentbot):
    board=message['board']
    opponents=message['opponents'] #nom des 2 joueurs ['opponent1','opponent2']
    #conversion board
    #definir si blanc ou noir
    #appeler l'ia
    #convertir le move de l'ia
    return coup
'''
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
    # Create a brand-new, blank board data structure.
    board = []
    for i in range(width):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    # Return False if the opponent's move on space xstart, ystart isinvalid.
    # If it is a valid move, return a list of spaces that would become the opponent's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # First step in the x direction
        y += ydirection # First step in the y direction
        while isOnBoard(x, y) and board[x][y] == otherTile:
            # Keep moving in this x & y direction.
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip

def isOnBoard(x, y):
    # Return True if the coordinates are located on the board.
    return x >= 0 and x <= width - 1 and y >= 0 and y <= height - 1

def getBoardWithValidMoves(board, tile):
    # Return a new board with periods marking the valid moves the opponent can make.
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    # Return a list of [x,y] lists of valid moves for the given opponent on the given board.
    validMoves = []
    for x in range(width):
        for y in range(height):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Return a dictionary with keys 'X' and 'O'.
    xscore = 0
    oscore = 0
    for x in range(width):
        for y in range(height):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def enteropponentTile():
    tile = ''
    #Randomly chose who plays first
    while not (tile == 'X' or tile == 'O'):
        if random.randint(0, 1) == 0:
            tile = 'X'
        else:
            tile = 'O'

    # The first element in the list is the opponent's tile, and the second is the computer's tile.
    if tile == 'O':
        return ['O', 'X']
    else:
        return ['X', 'O']

def whoGoesFirst():
    # Randomly choose who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'opponent'

def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart and flip any of the opponent's pieces.
    # Return False if this is an invalid move; True if it is valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    # Make a duplicate of the board list and return it.
    boardCopy = getNewBoard()

    for x in range(width):
        for y in range(height):
            boardCopy[x][y] = board[x][y]

    return boardCopy

def isOnCorner(x, y):
    # Return True if the position is in one of the four corners.
    return (x == 0 or x == width - 1) and (y == 0 or y == height - 1)

def getopponentMove(board, opponentTile):
    # Let the opponent enter their move.
    # Return the move as [x, y] (or quit)
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    # while True:
    #     print('Enter your move, "quit" to end the game, or "hints" to toggle hints.')
    #     move = input().lower()
    #     if move == 'quit' or move == 'hints':
    #         return move

    #     if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
    #         x = int(move[0]) - 1
    #         y = int(move[1]) - 1
    #         if isValidMove(board, opponentTile, x, y) == False:
    #             continue
    #         else:
    #             break
    #     else:
    #         print('That is not a valid move. Enter the column (1-8) and then the row (1-8).')
    #         print('For example, 81 will move on the top-right corner.')
    # return [x, y]

    #VIC
    while True:
        print('Enter the opponent\'s move or \'quit\' to stop the game.')
        move = input().lower()
        if move == 'quit':
            return move
        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, opponentTile, x, y) == False:
                continue
            else:
                break
        else:
            print('This is not a valid move from the opponent.')
    return [x, y]

def getComputerMove(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as an [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves) # Randomize the order of the moves.
    # Always go for a corner if available.
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # Find the highest-scoring move possible.
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def printScore(board, opponentTile, computerTile):
    scores = getScoreOfBoard(board)
    print('IA: {} points. Opponent: {} points.'.format(scores[computerTile], scores[opponentTile]))

def playGame(opponentTile, computerTile):
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    # Clear the board and place starting pieces.
    board = getNewBoard()
    board[3][3] = 'O'
    board[3][4] = 'X'
    board[4][3] = 'X'
    board[4][4] = 'O'

    while True:
        opponentValidMoves = getValidMoves(board, opponentTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if opponentValidMoves == [] and computerValidMoves == []:
            return board # No one can move, so end the game.

        elif turn == 'opponent': # opponent's turn
            if opponentValidMoves != []:
                drawBoard(board)
                global compteurDeTour
                print('Tour: {}.'.format(compteurDeTour))
                compteurDeTour += 1
                printScore(board, opponentTile, computerTile)

                move = getopponentMove(board, opponentTile)
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit() # Terminate the program.
                else:
                    makeMove(board, opponentTile, move[0], move[1])
            turn = 'computer'

        elif turn == 'computer': # Computer's turn
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, opponentTile, computerTile)
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
            turn = 'opponent'

print('Welcome to Othello !')

opponentTile, computerTile = enteropponentTile()

while True:
    finalBoard = playGame(opponentTile, computerTile)
    # Display the final score.
    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X scored %s points. O scored %s points.' % (scores['X'],scores['O']))
    if scores[opponentTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' %(scores[opponentTile] - scores[computerTile]))
    elif scores[opponentTile] < scores[computerTile]:
        print('You lost. The computer beat you by %s points.' %(scores[computerTile] - scores[opponentTile]))
    else:
        print('The game was a tie!')
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break