#reference : https://inventwithpython.com/invent4thed/chapter15.html
import random
import sys
import communication

width = 8
height = 8
compteurDeTour = 1


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
    # Renvoi True si les coordonnées sont sur le plateau
    return x >= 0 and x <= width - 1 and y >= 0 and y <= height - 1

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
    blackScore = 0
    whiteScore = 0
    for x in range(width):
        for y in range(height):
            if board[x][y] == 'X':
                blackScore += 1
            if board[x][y] == 'O':
                whiteScore += 1
    return {'X':blackScore, 'O':whiteScore}

def enterOpponentTile():
    tile = ''
    
    #Randomly chose who plays first
    while not (tile == 'X' or tile == 'O'):
        if random.randint(0, 1) == 0:
            tile = 'X'
        else:
            tile = 'O'

    # The first element in the list is the opponent's tile, and the second is the computer's tile.
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

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

# Ajout fonction conversion
def boardConvertion(message):
    plateau = message['board']
    boardConverted=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    for i in plateau[0]:
        x=i//8
        y=i-(8*x)
        boardConverted[x][y]='X'
    for i in plateau[1]:
        x=i//8
        y=i-(8*x)
        boardConverted[x][y]='O'
    print(boardConverted[0][0])
    return boardConverted

def findOpponentMove(boardConverted,board):
    opponentMove =''
    for i in range(8):
        for j in range(8):
            if boardConverted[i][j]!='' & board[i][j]=='':
                return [i, j]

def getMessage(message, iaPlayer):
    move = playGame(opponentTile, computerTile, message, iaPlayer)
    moveConverted = (int(move[0])*8)+int(move[1])
    return moveConverted #à completer

def findOpponentTurn(message, iaPlayer):
    if message['players'][0] == iaPlayer:
        return 'computer' # ia joue en premier
    else:
        return 'opponent' # ia joue en deuxieme

def printScore(board, opponentTile, computerTile):
    scores = getScoreOfBoard(board)

def playGame(opponentTile, computerTile, message, iaPlayer):
    turn = findOpponentTurn(message, iaPlayer)

    # Clear the board and place starting pieces.
    board = getNewBoard()
    board[3][3] = 'O'
    board[3][4] = 'X'
    board[4][3] = 'X'
    board[4][4] = 'O'

    while True:
        #Récupère les coups possibles pour chaque joueur
        opponentValidMoves = getValidMoves(board, opponentTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if opponentValidMoves == [] and computerValidMoves == []:
            break # No one can move, so end the game.

        elif turn == 'opponent': # opponent's turn
            if opponentValidMoves != []:
                printScore(board, opponentTile, computerTile)
                boardConverted = boardConvertion(message)
                move = findOpponentMove(boardConverted,board)
                if move == 'quit': # pas prévu
                    sys.exit() # Terminate the program.
                else:
                    makeMove(board, opponentTile, move[0], move[1])
            turn = 'computer'

        elif turn == 'computer': # Computer's turn
            if computerValidMoves != []:
                printScore(board, opponentTile, computerTile)
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
                return move
            turn = 'opponent'


opponentTile, computerTile = enterOpponentTile()