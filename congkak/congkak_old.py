#this is the board. Layout is:
#       board2  (enemy)
#       board1  (me)
# boardformat is [home][6,5,4,3,2,1] with 0 at right most

#board = [p1 = {0:[n,n,n,n,n,n,n], 1:0}, p2 = {0:[n,n,n,n,n,n,n], 1:0}]

#functions

# initiates new board, with 7 in each pit, 0 in home


def start(n,m):
    p1 = {0:[n,n,n,n,n,n,n], 1:0}
    p2 = {0:[m,n,n,n,n,n,n], 1:0}

    board = [p1,p2]
    return board

def score(board,player,amount):
    return board


def end(board):
    win = 0
    p1 = board[0]
    p2 = board[1]

    if p1[1] == p2[1]:
        win = 0
    elif p1[1] > p2[1]:
        win = 1
    else:
        win = 2
    
    return win

# boardformat is [home][6,5,4,3,2,1] with 0 at right most

#this function makes a move on the board
def playermove(board,player,pit):
    currentplayer = player
    print('oldboard',board)

    #copy of old board for reference
    oldboard = board.copy()

    #find how many marbles, n in selected pit
    n = board[player][0][pit]
    spaces = 7 - pit
    
    # removes marbles in selected pit
    board[player][0][pit] = 0
    print('remove selected pit\n',board)

    #treating overflows
    j = 0
    #modifier for picking up and placing in next
    mod = 1

    # This is the overflow loop (there are marbles to be placed on the other side of the current board)
    while n >= spaces:
        #debug statements
        print('start of overflow loop',j)
        print('playerside',player)
        print('starting pit',pit)
        print('n',n)
        print('spaces',spaces)
        
        
        for i in range(7):
            try:
                board[player][0][pit+i+mod] = board[player][0][pit+i+mod] + 1
                n -= 1
                print(board)
            except IndexError:
                exceed = True
                score(board,player,1)
                break
        
        if exceed is True:
            print('home')
            if player == currentplayer:
                board[player][1] += 1
                n -=1
                print(board)
        exceed = False

        
        
        #swap board sides 
        if player == 0:
            player += 1
        else:
            player -= 1
        
        # n -= spaces
        pit = 0
        mod = 0
        j+=1
        # print('board side',player)
        # print('spaces',spaces)
        # print('initial state',initial)
        
        # print('state of current overflow loop: \n',board)

    #underflow
    print('start of underflow loop')
    print('playerside',player)
    print('starting pit',pit)
    print('n',n)
    print('spaces',spaces)

    for i in range(n):
        try:  
            board[player][0][pit+i+mod] = board[player][0][pit+i+mod] + 1
            print(board)
        except IndexError:
            exceed = True
            break
    
    if exceed is True:
        print('home')
        if player == currentplayer:
                board[player][1] += 1
                if n == 2:
                    n -=2
                else:
                    n -=1

    exceed = False
    print('newboard',board)

    return board

#3 rules of congkak
def free():
    return

def steal():
    return

def skip():
    return

# pstart = input('Player1 or Player2 start, player1 default (y for player1 start)')
pstart = 1

if pstart in ['y',1]:
    player = 0
else: 
    player = 1

test = 22
pit = 0

board = start(7,test)
print('test start has {}'.format(test))
game = True
print('starting board')
print(board)
print('\n')
while game is True:
    board = playermove(board,player,pit)
    game = False
    