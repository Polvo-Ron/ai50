import math

X = "X"
O = "O"
EMPTY = None

def actions_set(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = {}
    inter_actions    = []
    i     = -1
    j     = -1
    items = 0
    nbr   = 0
    for _ in board:
        i += 1
        j = -1
        for x in _:
            j += 1
            items += 1
            if board[i][j] == EMPTY:
                print(f'{i},{j}')
                nbr += 1
                inter_actions.append((nbr,i,j))
                possible_actions.update( {nbr:(i,j)} )
    print("In set routine")
    print(possible_actions)

    if items != 9:
        raise NotImplementedError("Invalid board")
    else:
        possible_actions = {tup[0] : (tup[1],tup[2]) for tup in inter_actions}
        return possible_actions


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
                print(f'{i},{j}')
                possible_actions.append((i,j))

    if items != 9:
        raise NotImplementedError("Invalid board")
    else:
        return possible_actions

act = []
dic = {}

board =     [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, O],
            [EMPTY, EMPTY, EMPTY]]
try:
    act = actions(board)
    #actions(board)
except NotImplementedError as e:
    print (e)
    print ('An error has ocurred' ) 
else:
    print(act)
    #for rows in act:
    #    print(rows)
    print([act[i] for i in range(len(act))]) 
    print('longitud de la lista',len(act))
    for i in act:
        hd, *tl = act
        print('head',hd)
        print('tail',tl)
        ln = len(tl)
        print(ln)
        act = tl
finally:
    print('Done')

# to build a dictionary
try:
    dic = actions_set(board)
    #actions(board)
except NotImplementedError as e:
    print (e)
    print ('An error has ocurred' ) 
else:
    print(dic)
    #for rows in act:
    #    print(rows)
    #print([dic[i] for i in range(len(dic))]) 
    print('tupla',dic[1])
    for i in dic.items():
        print(i)
        orden,tp = i
        x,y = tp
        print("valor extraído",orden,x,y)
        hd, *tl = dic
        print('head',hd)
        print('tail',tl)
        #print('tupla',dic[int(hd)])
        ln = len(tl)
        print(ln)
        dic = tl
finally:
    print('Done')