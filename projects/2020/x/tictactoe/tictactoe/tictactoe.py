"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    count_sp = 0
    for rows in board:
        for column in rows:
            if column == X:
                count_x += 1
            elif column == O:
                count_o += 1
            elif column == EMPTY:
                count_sp += 1
            else:
                raise NotImplementedError("Invalid Symbol")
    if count_sp + count_x + count_o != 9:
        raise NotImplementedError("Invalid Board")
    
    if count_sp == 9:
        return X
    elif count_x >  count_o:
        return O
    elif count_o >= count_x:
        return X
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    i     = 0
    j     = 0
    items = 0
    for rows in board:
        i += 1
        for j in range(len(rows)):
            items += 1
            if rows[j] == EMPTY:
                possible_actions.append((i,j))
    if items != 9:
        raise NotImplementedError("Invalid board")
    else:
        return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

act = []

board =     [[X, X, O],
            [X, EMPTY, O],
            [O, X, O]]
try:
    act = actions(board)
except NotImplementedError as e:
    print (e)
    print ('An error has ocurred' ) 
else:
    for rows in act:
        print([rows[i] for i in range(len(rows))]) 
finally:
    print('Done')

