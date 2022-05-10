import pytest
import ia_v2

def test_getMessage():
    assert ia_v2.getMessage({'players': ['CAVA', 'CKC'], 'current': 1, 'board': [[20, 28], [36]]},'CKC')==12 #only 1 move
    assert ia_v2.getMessage({'players': ['CAVA', 'CKC'], 'current': 1, 'board': [[56], [48]]},'CKC')==None #no possible move 
    assert ia_v2.getMessage({'players': ['CAVA', 'CKC'], 'current': 1, 'board': [[41, 42, 43, 44, 48], [40]]},'CKC')==56 #take corner

def test_getNewBoard():
    assert ia_v2.getNewBoard()==[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
def test_makeMove():
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'O', 'X', ' ', ' ', ' '],
            [' ', ' ', ' ', 'X', 'O', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert ia_v2.makeMove(board, 'X', 2, 2)==False

