from core_functions import *
import os



options = {}
options['verbose'] = 0

# pstart = input('Player1 or Player2 start, player1 default (y for player1 start)')
pstart = 1

if pstart in ['y',1]:
    player = plyer(0)
    currentplayer = plyer(0)
    enemy = plyer(1)
    currentenemy = plyer(1)
else: 
    currentplayer = plyer(1)
    player = plyer(1)
    enemy = plyer(0)
    currentenemy = plyer(0)



test = 8
pit = 0
location1 = [1,0]

board = start(7)
#board[0][0][0] = 8
#board[1][0][0] = 0
#board[1][0][2] = 5
#board[1][0][3] = 10





print('test start has {}'.format(test))
game = True
print('starting board')
print(board)
print('\n')

skip = False
turns = 0
skipturns  = 0
game = True

currentplayer = currentplayer.switch()
currentenemy = currentenemy.switch() 

#number of turns for a player
while game is True:
    turns += 1
    turns = skipturns + turns #adds turns from skip
    print("Start of a new player's turn",turns)
    currentplayer = currentplayer.switch()
    currentenemy = currentenemy.switch() 
   
    while turns > 0:
        #resetting the status
        skip = False
        skipturns = 0
        steal = False
        free = False
        
            
        oldboard = copy.deepcopy(board)
        # currentplayer = plyer(player.player)
        # currentenemy = plyer(enemy.player)
        player = plyer(currentplayer.player)
        enemy = plyer(currentenemy.player)

        #making a move, extra turn on landing at home is implemented within
        playerinfo = {'currentplayer':currentplayer, 'currentenemy':currentenemy,
                       'player':player, 'enemy':enemy}

        


        #player go
        print('\n\n#############################')
        # print('board\n',board)
        drawboard(board)
        print('start of round playerinfo')
        print('currentplayer',currentplayer.player)
        print('currentenemy',currentenemy.player)
        print('player',player.player)
        print('enemy',enemy.player)
        print('\n')
        print("Player {}'s go".format(currentplayer.player + 1))
        print('Number of moves remaining',turns)
        #pit selection
        selectpit = int(input('select pit (0-6)'))
        legal = checklegal(board,playerinfo,selectpit)
        print(legal)

        while legal is False:
            drawboard(board)
            selectpit = int(input('invalid pit, please select pit (0-6)'))
            legal = checklegal(board,playerinfo,selectpit)

        
        
        #making a move
        board,lastpit = playermove(board,playerinfo,selectpit,options)


        if board is None:
            print('please select nonzero pit')
            board = oldboard
            break

        #checks
        print('#############\nchecks initiated')
        
        ##checking if lastpit has n == 1

        #checking for free go. 
        free = checkfree(board, playerinfo, lastpit)
        if free is True:
            turns += 1
        
        #checking for steal or skip, this only occurs when lastpitn ==1
        
        elif board[lastpit[1]][0][lastpit[0]] == 1:
            print('lastpit has 1 marble, checking for steal and skip')
            #checking for steal
            steal = checksteal(board,playerinfo,lastpit)
            if steal is True:
                board = stealfunc(board,playerinfo,lastpit)

            # checking for skip
            skip = checkskip(board,playerinfo,lastpit)
            if skip is True:
                skipturns = 1

        else:
            pass
        print('#############\n')

        print('end of round playerinfo')
        print('currentplayer',currentplayer.player)
        print('currentenemy',currentenemy.player)
        print('player',player.player)
        print('enemy',enemy.player)
        

        #check if game has ended
        win,winner = checkend(oldboard)
        if win == True:
            game = False
            
            print('game has ended')
            if win is None:
                print('Game Draw')
            else:
                print('Player {} wins'.format(player.player))
        



        # print('newboard\n',board)
        drawboard(board)
        
        turns -= 1
        