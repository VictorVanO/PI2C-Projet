


def newBoard():
    board = []
    for i in range(8):
        for j in range(8):
            board[i][j]=''
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

def coupPossible(boardList):

    return true