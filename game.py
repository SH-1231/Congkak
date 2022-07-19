import time
import copy
from core_functions import plyer




class Game:

    def __init__(self):
        self.initialize_game()

    
    def start(self,n):
        p1 = {0:[n,n,n,n,n,n,n], 1:0}
        p2 = {0:[n,n,n,n,n,n,n], 1:0}

        b = [p1,p2]
        return b
    def initialize_game(self):
        self.board = self.start(7)
        self.turns = 0
        self.currentplayer = plyer(0)
        self.currentenemy = plyer(1)
        self.side = plyer(0)
        self.game_status = True
        self.options = {'verbose':0}


    def drawboard(self):
        p2 = self.board[1][0]
        p1 = [i for i in reversed(self.board[0][0])]
        p1home = self.board[0][1]
        p2home = self.board[1][1]

        print('\n')
        print('player2 score:',p2home)
        print(p2)
        print(p1)
        print('player1 score:',p1home)
        print('\n')

    def isvalid(self,selectpit): 
        if selectpit not in [i for i in range(len(self.board[0][0]))]:  
            return False
        if self.board[self.currentplayer.player][0][selectpit] == 0:
            return False
        else:
            return True
    
    def checkend(self):
    #goes through board and counts the total marbles in play
        n = 0
        for p in self.board:
            for i in p[0]:
                n += i
        if n == 0:
            if self.board[0][1]>self.board[1][1]:
                winner = plyer(0)
            elif self.board[0][1]<self.board[1][1]:
                winner = plyer(1)
            else:
                winner = None

            return True, winner

        else:            
            return False, None

    def score(self,points):
        self.board[self.currentplayer.player][1] += points
        return self.board

    def playermove(self,pit,options):
        try: 
            verbose = options['verbose']
        except:
            verbose = 0

        currentplayer = self.currentplayer.player
        player = self.side.player


        # note that pit for the first overflow loop/ only underflow will have
        # to be +1 as the player adds marbles starting in pit+1

        #find how many marbles, n in selected pit

        
        n = self.board[self.currentplayer.player][0][pit]
        spaces = 7 - pit
        
        # removes marbles in selected pit
        self.board[self.currentplayer.player][0][pit] = 0
        
        
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
                    self.board[self.side.player][0][pit+i] = self.board[self.side.player][0][pit+i] + 1
                    n -= 1
                except:
                    break
                if verbose == 1:
                    print(self.board)
        
            if self.side.player == self.currentplayer.player:
                self.score(1)
                n -=1
                if verbose == 1:
                    print('scored') 
                    print(self.board)

            
            #swap board sides on overflow loop iteration end
            self.side.switch()
            
            spaces = len(self.board[0][0])
            pit = 0
            j+=1
            

        

        #underflow
        print('start of underflow loop')
        # print('playerside',player,player)
        # print('starting pit',pit)
        # print('n',n)
        # print('spaces',spaces)

        for i in range(n):
                try:
                    self.board[self.side.player][0][pit+i] = self.board[self.side.player][0][pit+i] + 1
                    n -= 1
                    if verbose == 1:
                        print(self.board)
                except:
                    break
        lastpitn = pit+i
        lastpitside = self.side.player

        # print('lastpitn',lastpitn)
        # print('lastn',n)


        #check if score in underflow loop, free go if it happens 
        if n == 1:
            if self.side.player == self.currentplayer.player:
                
                self.score(1)
                n -=1
                if verbose == 1:
                    print('scored')
                    print(self.board)
            
            
        else:
            pass
        

        lastpit = [lastpitn, lastpitside]
        return self.board,lastpit

    def checkfree(self,lastpit):
        print('####\ncheck free')
        # currentplayer = playerinfo['currentplayer']
        # currentenemy = playerinfo['currentenemy']
        # player = playerinfo['player']
        # enemy = playerinfo['enemy']

        
        lastpitn = lastpit[0]
        if lastpitn == len(self.board[0][0]):
            print('free occured')
            return True

        else:
            return False

    def checksteal(self, lastpit):
        #checking current board
        print('####\ncheck steal')

        lastpitn = lastpit[0]
        #sets enemy board to 0 and transfers amt to player score
        if lastpitn == len(self.board[0][0]):
            return False

        if self.board[self.currentplayer.player][0][lastpitn] == 1:
            print('steal occured')
            return True

        else:
            return False

    def checkskip(self, lastpit):
        #checking current board
        print('####\ncheck skip')

        lastpitn = lastpit[0]
        lastpitside = lastpit[1]

        if lastpitn == len(self.board[0][0]):
            return False

        if self.board[lastpitside][0][lastpitn] == 1:
            print('skip occured')
            return True
        else:
            return False

        
    def stealfunc(self,lastpit):
        lastpitn = lastpit[0]
        

        print('stealing now')
        amt = self.board[self.currentenemy.player][0][len(self.board[0][0])-lastpitn-1] 
        #clearing pit
        print('amount stolen',amt)
        self.board[self.currentenemy.player][0][len(self.board[0][0])-lastpitn-1] = 0
        print('before steal',self.board[self.currentplayer.player][1])
        self.board[self.currentplayer.player][1] += amt
        print('after steal',self.board[self.currentplayer.player][1])

        return self.board
            
    def play(self):
        # selectpit = int(input("Player {}'s go. {} turns remaining. \n Please select a pit to play".format(self.currentplayer,self.turns)))

        self.initialize_game()
        skip = False
        skipturns  = 0
        self.currentplayer.switch()
        self.currentenemy.switch() 

        #number of turns for a player
        while self.game_status is True:
            self.turns += 1
            self.turns = skipturns + self.turns #adds turns from skip
            print("Start of a new player's turn",self.turns)
            self.currentplayer.switch()
            self.currentenemy.switch() 
        
            while self.turns > 0:
                #resetting the status
                skip = False
                skipturns = 0
                steal = False
                free = False
                
                    
                oldboard = copy.deepcopy(self.board)              

                #player go
                print('\n\n#############################')
                # print('board\n',board)
                self.drawboard()
                print('start of round playerinfo')
                print('currentplayer',self.currentplayer.player)
                print('currentenemy',self.currentenemy.player)
                print('\n')
                print("Player {}'s go".format(self.currentplayer.player + 1))
                print('Number of moves remaining',self.turns)
                #pit selection
                selectpit = int(input('select pit (0-6)'))
                legal = self.isvalid(selectpit)
                print(legal)

                while legal is False:
                    self.drawboard()
                    selectpit = int(input('invalid pit, please select pit (0-6)'))
                    legal = self.isvalid(selectpit)

                
                
                #making a move
                self.board,lastpit = self.playermove(selectpit,options=self.options)

                #checks
                print('#############\nchecks initiated')
                
                ##checking if lastpit has n == 1

                #checking for free go. 
                free = self.checkfree(lastpit)
                if free is True:
                    self.turns += 1
                
                #checking for steal or skip, this only occurs when lastpitn ==1
                
                elif self.board[lastpit[1]][0][lastpit[0]] == 1:
                    print('lastpit has 1 marble, checking for steal and skip')
                    #checking for steal
                    steal = self.checksteal(lastpit)
                    if steal is True:
                        self.board = self.stealfunc(lastpit)

                    # checking for skip
                    skip = self.checkskip(lastpit)
                    if skip is True:
                        skipturns = 1

                else:
                    pass
                print('#############\n')

                print('end of round playerinfo')
                print('currentplayer',self.currentplayer.player)
                print('currentenemy',self.currentenemy.player)
                
                

                #check if game has ended
                win,winner = self.checkend()
                if win == True:
                    self.game = False
                    
                    print('game has ended')
                    if win is None:
                        print('Game Draw')
                    else:
                        print('Player {} wins'.format(winner))
                



                # print('newboard\n',board)
                self.drawboard()
                
                self.turns -= 1
    def max(self):
        return

    def min(self):
        return
                


def main():
    g = Game()
    g.play()

if __name__ == "__main__":
    main()
            

            
