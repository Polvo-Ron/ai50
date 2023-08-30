"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
finals = (X,O)
EMPTY = None

win_com = [[(0,0),(0,1),(0,2)], # Three of the moves
           [(0,0),(1,0),(2,0)], # to win
           [(0,0),(1,1),(2,2)],
           [(0,2),(1,2),(2,2)],
           [(0,2),(1,1),(2,0)],
           [(0,1),(1,1),(2,1)],
           [(1,0),(1,1),(1,2)],
           [(2,0),(2,1),(2,2)]]

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
    i     = -1
    j     = -1
    items = 0
    for _ in board:
        i += 1
        j = -1
        for x in _:
            j += 1
            items += 1
            if board[i][j] == EMPTY:
                possible_actions.append((i,j))

    if items != 9:
        raise NotImplementedError("Invalid board")
    else:
        return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    valids = (0,1,2)
    i,j = action
    if i in valids and j in valids:
       if board[i][j] == EMPTY:
        cboard = copy.deepcopy(board)
        cboard[i][j] = player(board)
        return cboard
       else:
        raise NotImplementedError ("Invalid Movement")
    else:
        raise NotImplementedError ("Invalid Board")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    i0 = j0 = i1 = j1 = i2 = j2 = elem = 0

    for rows in board:
        for column in rows:
            elem += 1
    if elem != 9:
        raise NotImplementedError("Invalid Board")

    for win in win_com: 
        i0,j0 = win[0]  # obtains the winner 
        i1,j1 = win[1]  # combination
        i2,j2 = win[2]
        if (board[i0][j0] == X and
            board[i1][j1] == X and
            board[i2][j2] == X ):
            return X 
        elif (board[i0][j0] == O and
              board[i1][j1] == O and
              board[i2][j2] == O):
              return O
    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    pend = elem = 0
    rslt = EMPTY
    for rows in board:
        for column in rows:
            if column == EMPTY:
                pend += 1
            elem += 1
    if elem != 9:
        raise NotImplementedError("Invalid Board")
    rslt = winner(board) 
    if rslt in finals or pend == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    elem = 0
    rslt = EMPTY
    for rows in board:
        for column in rows:
            elem += 1
    if elem != 9:
        raise NotImplementedError("Invalid Board")
    rslt = winner(board) 
    if rslt == X:
        return 1  # X wins
    elif rslt == O:
        return -1 # O wins
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        v = -1000000
        if terminal(board):
            return utility(board) # 1, -1, 0
        for action in actions(board):
            v = max(v, min_value(result(board, action))) # result return a board (state)
            return  v 

    def min_value(board):
        v = 1000000
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
            return  v 
    try:
        if player(board) == X: # the maximizing player
            vv = min_value(board)
            return vv
        else:                  # the minimizing player
            vv = max_value(board)
            return vv 
    except NotImplementedError as e:
        print (e)
        print ('An error has ocurred' ) 


act = []

board =     [[X,O, X],
            [O,X ,EMPTY],
            [O,X,O ]]
try:
    v = minimax(board)
except NotImplementedError as e:
    print (e)
    print ('An error has been detected' ) 
else:
    print(v)
    #for rows in rows:
    #    print(rows)
    #    print([rows[i] for i in range(len(rows))]) 
finally:
    print('Done')

