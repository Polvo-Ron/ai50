import math

X = "X"
O = "O"
EMPTY = None


def actions_set(board):
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
                print(f'{i},{j}')
                possible_actions.append((i,j))

    if items != 9:
        raise NotImplementedError("Invalid board")
    else:
        return possible_actions

act = []

board =     [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, O],
            [EMPTY, EMPTY, EMPTY]]
try:
    act = actions_set(board)
    #actions(board)
except NotImplementedError as e:
    print (e)
    print ('An error has ocurred' ) 
else:
    print(act)
    #for rows in act:
    #    print(rows)
    print([act[i] for i in range(len(act))]) 
    for i in act:
        hd, *tl = act
        print('head',hd)
        print('tail',tl)
        ln = len(tl)
        print(ln)
        act = tl
finally:
    print('Done')

