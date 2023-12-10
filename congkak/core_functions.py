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
        # print('player {}'.format(self.player))

    def switch(self):
        
        if self.player == 0:
            self.player = 1

        elif self.player == 1:
            self.player = 0

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

def checklegal(board,playerinfo,pit):
    currentplayer = playerinfo['currentplayer']
    if pit not in [i for i in range(len(board[0][0]))]:
        return False
    
    elif board[currentplayer.player][0][pit] == 0:
        return False

    else: 
        return True

#this function makes a move on the board
def playermove(board,playerinfo,pit,options):
    try: 
        verbose = options['verbose']
    except:
        verbose = 0

    


    currentplayer = playerinfo['currentplayer']
    currentenemy = playerinfo['currentenemy']
    player = playerinfo['player']
    enemy = playerinfo['enemy']


    # note that pit for the first overflow loop/ only underflow will have
    # to be +1 as the player adds marbles starting in pit+1

    #find how many marbles, n in selected pit

    


    n = board[currentplayer.player][0][pit]
    spaces = 7 - pit
    
    # removes marbles in selected pit
    board[currentplayer.player][0][pit] = 0
    
    
    #putting marbles in next pit
    pit += 1

    #treating overflows
    j = 0
    

    # This is the overflow loop (there are marbles to be placed on the other side of the current board)
    while n > spaces:
        #debug statements
        print('start of overflow loop',j)
        # print('playerside',player.player)
        # print('starting pit',pit)
        # print('n',n)
        # print('spaces',spaces)
        
        
        for i in range(spaces):
            try:
                board[player.player][0][pit+i] = board[player.player][0][pit+i] + 1
                n -= 1
            except:
                break
            if verbose == 1:
                print(board)
    
        if player.player == currentplayer.player:
            score(board,player,1)
            n -=1
            if verbose == 1:
                print('scored') 
                print(board)

        
        #swap board sides on overflow loop iteration end
        player.switch()
        
        spaces = 7
        pit = 0
        mod = 0
        j+=1
        

    

    #underflow
    print('start of underflow loop')
    # print('playerside',player,player)
    # print('starting pit',pit)
    # print('n',n)
    # print('spaces',spaces)

    for i in range(n):
            try:
                board[player.player][0][pit+i] = board[player.player][0][pit+i] + 1
                n -= 1
                if verbose == 1:
                    print(board)
            except:
                break
    lastpitn = pit+i
    lastpitside = player.player

    # print('lastpitn',lastpitn)
    # print('lastn',n)


    #check if score in underflow loop, free go if it happens 
    if n == 1:
        if player.player == currentplayer.player:
            
            score(board,player,1)
            n -=1
            if verbose == 1:
                print('scored')
                print(board)
        
        
    else:
        pass
    

    lastpit = [lastpitn, lastpitside]
    return board,lastpit

def checkend(board):
    #goes through board and counts the total marbles in play
    n = 0
    for p in board:
        for i in p[0]:
            n += i
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

def checkfree(board,playerinfo,lastpit):
    print('####\ncheck free')
    # currentplayer = playerinfo['currentplayer']
    # currentenemy = playerinfo['currentenemy']
    # player = playerinfo['player']
    # enemy = playerinfo['enemy']

    
    lastpitn = lastpit[0]
    if lastpitn == len(board[0][0]):
        print('free occured')
        return True

    else:
        return False

def checksteal(board, playerinfo, lastpit):
    #checking current board
    print('####\ncheck steal')
    currentplayer = playerinfo['currentplayer']
    # currentenemy = playerinfo['currentenemy']
    # player = playerinfo['player']
    # enemy = playerinfo['enemy']

    lastpitn = lastpit[0]
    lastpitside = lastpit[1]
    #sets enemy board to 0 and transfers amt to player score
    if lastpitn == len(board[0][0]):
        return False

    if board[currentplayer.player][0][lastpitn] == 1:
        print('steal occured')
        return True

    else:
        return False

def checkskip(board, playerinfo, lastpit):
    #checking current board
    print('####\ncheck skip')
    # currentplayer = playerinfo['currentplayer']
    # currentenemy = playerinfo['currentenemy']
    # player = playerinfo['player']
    # enemy = playerinfo['enemy']
    

    lastpitn = lastpit[0]
    lastpitside = lastpit[1]

    if lastpitn == len(board[0][0]):
        return False

    if board[lastpitside][0][lastpitn] == 1:
        print('skip occured')
        return True
    else:
        return False

# def freefunc(turns):
#     turns += 1
#     return turns 



def stealfunc(board,playerinfo,lastpit):
    lastpitn = lastpit[0]
    currentplayer = playerinfo['currentplayer']
    currentenemy = playerinfo['currentenemy']

    print('steal occured!')
    amt = board[currentenemy.player][0][len(board[0][0])-lastpitn-1] 
    #clearing pit
    print('amount stolen',amt)
    board[currentenemy.player][0][len(board[0][0])-lastpitn-1] = 0
    print('before steal',board[currentplayer.player][1])
    board[currentplayer.player][1] += amt
    print('after steal',board[currentplayer.player][1])

    return board

def drawboard(board):
    p2 = board[1][0]
    p1 = [i for i in reversed(board[0][0])]
    p1home = board[0][1]
    p2home = board[1][1]

    print('\n')
    print('player2 score:',p2home)
    print(p2)
    print(p1)
    print('player1 score:',p1home)
    print('\n')



#this function plays the best play of the turn
def AIturn(board):
    play = 0
    return play





