from copy import deepcopy,copy
#this is the board. Layout is:
#       board2  (enemy)
#       board1  (me)
# boardformat is [home][6,5,4,3,2,1] with 0 at right most

#board = [p1 = {0:[n,n,n,n,n,n,n], 1:0}, p2 = {0:[n,n,n,n,n,n,n], 1:0}]

#functions

# initiates new board, with 7 in each pit, 0 in home


class plyer:
    
    def __init__(self,n):
        self.player = n

    def __deepcopy__(self):
        o = copy(self)
        o.player = deepcopy(self.player)
        return o

    def switch(self):
        print('old state:',self.player)
        if self.player == 0:
            self.player = 1

        elif self.player == 1:
            self.player = 0

        print('new state:',self.player)
        return self



def start(n):
    p1 = {0:[n,n,n,n,n,n,n], 1:0}
    p2 = {0:[n,n,n,n,n,n,n], 1:0}

    board = [p1,p2]
    return board

def score(board,player,points):
    board[player.player][1] += points
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
def playermove(board,player,pit,turns):
    placeholder = player.player
    #tracks the current player in the move
    currentplayer = plyer(placeholder)

    print('debug')
    print(currentplayer.player)
    print(player.player)

    # note that pit for the first overflow loop/ only underflow will have
    # to be +1 as the player adds marbles starting in pit+1

    #find how many marbles, n in selected pit
    n = board[player.player][0][pit]
    spaces = 7 - pit
    
    # removes marbles in selected pit
    board[player.player][0][pit] = 0
    print('remove selected pit\n',board)
    print('\n')
    
    #putting marbles in next pit
    print('pit',pit)
    pit += 1

    #treating overflows
    j = 0
    

    # This is the overflow loop (there are marbles to be placed on the other side of the current board)
    while n > spaces:
        #debug statements
        print('start of overflow loop',j)
        print('playerside',player.player)
        print('starting pit',pit)
        print('n',n)
        print('spaces',spaces)
        
        
        for i in range(spaces):
            print(n)
            try:
                board[player.player][0][pit+i] = board[player.player][0][pit+i] + 1
                n -= 1
            except:
                break
            print(board)
    
        if player.player == currentplayer.player:
            print('scored')
            score(board,player,1)
            n -=1
            print(board)       
        
        #swap board sides on overflow loop iteration end
        player.switch()
        
        spaces = 7
        pit = 0
        mod = 0
        j+=1
        print('board side',player.player)
        print('spaces',spaces)

    

    #underflow
    print('start of underflow loop')
    print('playerside',player,player)
    print('starting pit',pit)
    print('n',n)
    print('spaces',spaces)

    for i in range(n):
            print(n)
            try:
                board[player.player][0][pit+i] = board[player.player][0][pit+i] + 1
                n -= 1
            except:
                break
    print('lastn',n)

    #check if score in underflow loop, free go if it happens 
    
    if n == 1:
        if player.player == currentplayer.player:
            print('scored')
            score(board,player,1)
            nextplayer = currentplayer
            n -=1
            print(board)
        
        else:
            nextplayer = currentplayer
    else:
        nextplayer = currentplayer.switch()
    
        

         
    print('newboard',board)
    turns -= 1

    return board,nextplayer,turns

def checkend(board):
    #goes through board and counts the total marbles in play
    n = 0
    for p in board:
        for i in p[0]:
            n += i
    print(board[0][1])
    if n == 0:
        if board[0][1]>board[1][1]:
            winner = plyer(0)
        elif board[0][1]<board[1][1]:
            winner = plyer(1)
        else:
            winner = None

        return True, winner

    else:            
        return False, None
#3 rules of congkak
def free(currentplayer):
    return currentplayer

def steal():
    return

def skip():
    return

# pstart = input('Player1 or Player2 start, player1 default (y for player1 start)')
pstart = 1

if pstart in ['y',1]:
    player = plyer(0)
else: 
    player = plyer(1)


test = 22
pit = 0

board = start(1)
# board[player.player][0][pit] = test
print('test start has {}'.format(test))
game = True
print('starting board')
print(board)
print('\n')




while game is True:
    turns = 1
    while turns > 0:
        print("Player {}'s go".format(player.player + 1))
        selectpit = int(input('select pit (0-6)'))
        board,player,turns = playermove(board,player,selectpit,turns)
        win,winner = checkend(board)
        print('here',win,winner)
        if win == True:
            game = False
            turns = 0
            print('game has ended')
            if win is None:
                print('Game Draw')
            else:
                print('Player {} wins'.format(player.player))
       