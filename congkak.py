import copy
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
        print('player {}'.format(self.player))

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

#this function makes a move on the board
def playermove(board,playerinfo,pit):
    currentplayer = playerinfo['currentplayer']
    currentenemy = playerinfo['currentenemy']
    player = playerinfo['player']
    enemy = playerinfo['enemy']


    # note that pit for the first overflow loop/ only underflow will have
    # to be +1 as the player adds marbles starting in pit+1

    #find how many marbles, n in selected pit
    n = board[player.player][0][pit]
    spaces = 7 - pit
    
    # removes marbles in selected pit
    board[player.player][0][pit] = 0
    
    
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
            print('scored')
            score(board,player,1)
            n -=1
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
    currentplayer = playerinfo['currentplayer']
    currentenemy = playerinfo['currentenemy']
    player = playerinfo['player']
    enemy = playerinfo['enemy']

    
    lastpitn = lastpit[0]
    if lastpitn == len(board[0][0]):
        print('free occured')
        return True

    else:
        return False

def checksteal(board, playerinfo, lastpit):
    print('####\ncheck steal')
    currentplayer = playerinfo['currentplayer']
    currentenemy = playerinfo['currentenemy']
    player = playerinfo['player']
    enemy = playerinfo['enemy']
    lastpitn = lastpit[0]
    #sets enemy board to 0 and transfers amt to player score
    if lastpitn == len(board[0][0]):
        return False

    if board[currentplayer.player][0][lastpitn] == 0:
        print('steal occured')
        return True
    else:
        return False

def checkskip(board, playerinfo, lastpit):
    print('####\ncheck skip')
    currentplayer = playerinfo['currentplayer']
    currentenemy = playerinfo['currentenemy']
    player = playerinfo['player']
    enemy = playerinfo['enemy']
    
    #sets enemy board to 0 and transfers amt to player score
    lastpitn = lastpit[0]
    lastpitside = lastpit[1]

    if lastpitn == len(board[0][0]):
        return False

    if board[lastpitside][0][lastpitn] == 0:
        print('skip occured')
        return True
    else:
        return False

# def freefunc(turns):
#     turns += 1
#     return turns 



def stealfunc(board,playerinfo,lastpit):
    lastpitn = lastpit[0]
    print('steal occured!')
    enemy = plyer(player.player).switch()
    amt = board[enemy.player][0][7-lastpitn] 
    #clearing pit
    board[enemy.player][0][len(board[0][0])-lastpitn-1] = 0
    board[player.player][1] =+ amt

    return board









# pstart = input('Player1 or Player2 start, player1 default (y for player1 start)')
pstart = 1

if pstart in ['y',1]:
    player = plyer(0)
    enemy = plyer(1)
else: 
    player = plyer(1)
    enemy = plyer(0)



test = 8
pit = 0
location1 = [1,0]

board = start(7)
board[0][0][0] = 8
board[1][0][0] = 0
board[1][0][2] = 5
board[1][0][3] = 10





print('test start has {}'.format(test))
game = True
print('starting board')
print(board)
print('\n')

skip = False
turns = 0
skipturns  = 0
game = True

#number of turns for a player
while game is True:
    turns += 1
    turns = skipturns + turns #adds turns from skip
    print('debug!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',turns)

   
    while turns > 0:
         #resetting the status
        skip = False
        skipturns = 0
        steal = False
        free = False
            
            
        oldboard = copy.deepcopy(board)
        currentplayer = plyer(player.player)
        currentenemy = plyer(enemy.player)

        #player go
        print('\n\n#############################')
        print('board\n',board)
        print("Player {}'s go".format(currentplayer.player + 1))
        print('Number of moves remaining',turns)
        #pit selection
        selectpit = int(input('select pit (0-6)'))


        #making a move, extra turn on landing at home is implemented within
        playerinfo = {'currentplayer':currentplayer, 'currentenemy':currentenemy,
                       'player':player, 'enemy':enemy}
        board,lastpit = playermove(board,playerinfo,selectpit)
        

        #checks
        print('checks initiated')
        print('currentplayer',currentplayer.player)
        print('currentenemy',currentenemy.player)
        print('player',player.player)
        print('enemy',enemy.player)

        #checking for free go
        free = checkfree(oldboard, playerinfo, lastpit)
        if free is True:
            turns += 1

        #checking for steal
        steal = checksteal(oldboard,playerinfo,lastpit)
        if steal is True:
            board = stealfunc(board,playerinfo,lastpit)

        # checking for skip
        skip = checkskip(oldboard,playerinfo,lastpit)
        if skip is True:
            skipturns = 1
        

        #check if game has ended
        win,winner = checkend(oldboard)
        if win == True:
            game = False
            
            print('game has ended')
            if win is None:
                print('Game Draw')
            else:
                print('Player {} wins'.format(player.player))
        



        print('newboard\n',board)
        
        turns -= 1
        