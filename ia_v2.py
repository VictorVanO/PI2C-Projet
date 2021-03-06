#reference : https://inventwithpython.com/invent4thed/chapter15.html
import random
import sys

width = 8
height = 8
opponentTile, computerTile =['','']

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
    # Return true if the coordonate are on the baord
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
    # Find the score by counting the tiles. And return a dictionary with keys 'X' and 'O' with the associated score.
    blackScore = 0
    whiteScore = 0
    for x in range(width):
        for y in range(height):
            if board[x][y] == 'X':
                blackScore += 1
            if board[x][y] == 'O':
                whiteScore += 1
    return {'X':blackScore, 'O':whiteScore}

def makeMove(board, tile, xstart, ystart):
    # Put the tile on the board at xstart, ystart and flip any of the opponent's pieces.
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

def getComputerMove(board, computerTile, opponentTile):
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

# Convert the board receved into a compatible board for this ia
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
    return boardConverted

# first function to be called by communication
def getMessage(message, iaPlayer):
    global opponentTile, computerTile
    if message['current']==0 or message['current']==1: #check if new game
        opponentTile, computerTile =['','']  # reset tile for opponent and computer
    if computerTile=='' and opponentTile == '': #if tiles are not attributed then
        if message['players'][0] == iaPlayer:   #if the ia is the first player
            opponentTile, computerTile = ['O', 'X']
        else:                                   #if the ia is the second player
            opponentTile, computerTile = ['X', 'O']
    move = playGame(opponentTile, computerTile, message, iaPlayer)
    if move == None: #check if we pass the turn 
        moveConverted=move
    else:
        moveConverted = (int(move[0])*8)+int(move[1]) #else we convert the move back
    return moveConverted #return the move to be send

def findOpponentTurn(message, iaPlayer):
    turn = int(message['current'])%2
    #check (when player is first and play when current is even) or check (when player is second and play when current is odd)
    if (message['players'][0] == iaPlayer and turn == 0) or (message['players'][1] == iaPlayer and turn == 1):  
        return 'computer'
    else: # else it is the opponent turn
        return 'opponent'

def printScore(board):
    scores = getScoreOfBoard(board)

def playGame(opponentTile, computerTile, message, iaPlayer):
    turn = findOpponentTurn(message, iaPlayer)
    board = boardConvertion(message)

    while True:
        #find all the valid moves for each players
        opponentValidMoves = getValidMoves(board, opponentTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if opponentValidMoves == [] and computerValidMoves == []:
            break # No one can make move, so end the game.

        elif turn == 'computer': # Computer's turn
            if computerValidMoves != []:
                printScore(board)
                print(computerTile)
                move = getComputerMove(board, computerTile, opponentTile)
                print('le move pour les '+computerTile+' est '+str(move))
                for i in range(8):
                    print(board[i])
                makeMove(board, computerTile, move[0], move[1])
                return move
            else:
                return None
