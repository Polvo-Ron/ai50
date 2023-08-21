import math
import time
X = "X"
O = "O"
EMPTY = None
valids = ('X','O',None)
num_veces = 0
def player_1(board):
    """
    Returns player who has the next turn on a board.
    """
    cont    = 0
    counter = {'X':(0),'O':(0),None:(0)}

    #print(counter)
    for rows in board:
        for column in rows:
            if column in valids:
                #print(column)
                #print(counter[column])
                cont = counter[column]
                cont += 1
                counter.update( {column:(cont)})
            else:
                raise NotImplementedError("Invalid Symbol")
    #print(counter)

    if counter[None] + counter['X'] + counter['O'] != 9:
        raise NotImplementedError("Invalid Board")
    
    if counter[None] == 9:
        return X
    elif counter['X'] >  counter['O']:
        return O
    elif counter['O'] >= counter['X']:
        return X
    else:
        return X

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


board =     [[X, EMPTY, EMPTY],
            [X, EMPTY, O],
            [EMPTY, EMPTY, EMPTY]]
try:
    inic = time.process_time_ns()
    while True:
        act = player(board)
        num_veces += 1
        if num_veces % 100000 == 0:
            break
    prim = time.process_time_ns()
    while True:
        act = player_1(board)
        num_veces += 1
        if num_veces % 100000 == 0:
            break
    seg = time.process_time_ns()
    while True:
        act = player(board)
        num_veces += 1
        if num_veces % 100000 == 0:
            break
    ter = time.process_time_ns()
    while True:
        act = player_1(board)
        num_veces += 1
        if num_veces % 100000 == 0:
            break
    cuar = time.process_time_ns()
    print( 'player',prim-inic) 
    print('player 1',seg-prim)
    print( 'player',ter-seg) 
    print('player 1',cuar-ter)

except NotImplementedError as e:
    print (e)
    print ('An error has ocurred' ) 
else:
    print(act)

    print('Done')

# $ python test_loop.py 
# player 109375000
# player 1 265625000
# player 109375000
# player 1 265625000
# O
# Done