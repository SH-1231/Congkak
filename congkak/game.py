import os

from core_functions import plyer




class Game:

    # Initialization of the class
    def __init__(self,n):
        self.n = n
    
    #This function contructs the board used to play
    def start(self):
        n = self.n
        p1 = {0:[n,n,n,n,n,n,n], 1:0}
        p2 = {0:[n,n,n,n,n,n,n], 1:0}

        b = [p1,p2]
        return b

    #Initializes the game
    def initialize_game(self):
        #initialize the board
        self.board = self.start()
        self.gameturns = 0
        self.lastmove = 0
        self.lastpit = 0

        #3 rules of congkak checks
        self.free = False
        self.skip = False
        self.skip = False

        #initialize player data
        self.turns = 0
        self.currentplayer = plyer(0)
        self.currentenemy = plyer(1)
        self.side = plyer(0)
        self.game_status = True
        self.options = {'verbose':0}


        #reversing player 2's orientation for the user to see
        p2 = self.board[1][0]
        p1 = [i for i in reversed(self.board[0][0])]
        p1home = self.board[0][1]
        p2home = self.board[1][1]

        #saving the gamestate (this is broken)
        if 'movelist.txt' in os.getcwd():
            os.remove('movelist.txt') 
        movelist = open('movelist.txt','w')
        movelist.write('gameturns:' + str(self.gameturns) + '\n')
        movelist.write('Current player:{}\n'.format(self.currentplayer.player))
        movelist.write(str(p2home)+ '\n')
        movelist.write(str(p2)+ '\n')
        movelist.write(str(p1)+ '\n')
        movelist.write(str(p1home)+ '\n')
        movelist.write('\n')
        movelist.close()


   
    #This function draws the board on the terminal
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

    #This function determines if the move made by the current player is legal
    def isvalid(self,selectpit): 
        if selectpit not in [i for i in range(len(self.board[0][0]))]:  
            return False
        if self.board[self.currentplayer.player][0][selectpit] == 0:
            return False
        else:
            return True
    
    #This function checks if the current player's side of the board is empty
    def checkemptyside(self):
        playern = 0
        for i in range(len(self.board[0][0])):
            playern += self.board[self.currentplayer.player][0][i]
        if playern == 0 :
            return True
        else:
            return False

    #This function checks if the game is still live
    def check_game_status(self):
        #goes through board and counts the total marbles in play
        #returns True if it is still live
        n = 0
        p1 = self.board[0][0]
        p2 = self.board[1][0]
        for i in range(len(p1)):
            n+= p1[i]
            n+= p2[i]
            print(n,i)

        if n == 0:
            if self.board[0][1]>self.board[1][1]:
                winner = plyer(0)
            elif self.board[0][1]<self.board[1][1]:
                winner = plyer(1)
            else:
                winner = None

            return False, winner

        else:            
            return True, None

    #This function scores points
    def score(self,points):
        self.board[self.currentplayer.player][1] += points
        return self.board

    #This function allows for a player to make a move
    def playermove(self,pit,options):
        try: 
            verbose = options['verbose']
        except:
            verbose = 0

        #setting the side of the board to the current player
        self.side.player = self.currentplayer.player
        


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
        self.lastpit = pit+i
        

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
        
        self.lastpitside = self.side.player
        print('lastpitinfo:{},{}'.format(self.lastpit,self.lastpitside))
        # lastpit = [lastpitn, lastpitside]
        return self.board

    #1st Rule of congkak
    def checkfree(self):
        print('####\ncheck free')
        # currentplayer = playerinfo['currentplayer']
        # currentenemy = playerinfo['currentenemy']
        # player = playerinfo['player']
        # enemy = playerinfo['enemy']

        
        # lastpitn = lastpit[0]
        if self.lastpit == len(self.board[0][0]):
            print('free occured')
            return True

        else:
            return False

    #2nd Rule of congkak
    def checksteal(self):
        #checking current board
        print('####\ncheck steal')

        # lastpitn = lastpit[0]
        #sets enemy board to 0 and transfers amt to player score
        if self.lastpit == len(self.board[0][0]):
            return False

        if self.board[self.currentplayer.player][0][self.lastpit] == 1:
            print('steal occured')
            return True

        else:
            return False

    #3rd Rule of congkak
    def checkskip(self):
        #checking current board
        print('####\ncheck skip')

        # lastpitn = lastpit[0]
        # lastpitside = lastpit[1]

        if self.lastpit == len(self.board[0][0]):
            return False

        
        if self.board[self.currentenemy.player][0][len(self.board[0][0]) - self.lastpit - 1] == 1:
            print('skip occured')
            return True
        else:
            return False

    #This function steals the opposing player's marbles    
    def stealfunc(self):
        # lastpitn = lastpit[0]
        print('stealing now')
        amt = self.board[self.currentenemy.player][0][len(self.board[0][0])-self.lastpit-1] 
        #clearing pit
        print('amount stolen',amt)
        self.board[self.currentenemy.player][0][len(self.board[0][0])-self.lastpit-1] = 0
        print('before steal',self.board[self.currentplayer.player][1])
        self.board[self.currentplayer.player][1] += amt
        print('after steal',self.board[self.currentplayer.player][1])

        return self.board
    
    #This function saves the move made (Broken)
    def save(self):
        p2 = self.board[1][0]
        p1 = [i for i in reversed(self.board[0][0])]
        p1home = self.board[0][1]
        p2home = self.board[1][1]
        

        movelist = open('movelist.txt','a')
        movelist.write('\n\n')
        movelist.write('gameturns:' + str(self.gameturns) + '\n')
        movelist.write('move:' + str(self.lastmove) + '\n')
        movelist.write('Current player:{}\n'.format(self.currentplayer.player))
        movelist.write(str(p2home)+ '\n')
        movelist.write(str(p2)+ '\n')
        movelist.write(str(p1)+ '\n')
        movelist.write(str(p1home)+ '\n')
        movelist.write('\n')

        movelist.write('checks')
        movelist.write('free: {}'.format(self.free))
        movelist.write('steal: {}'.format(self.steal))
        movelist.write('skip: {}'.format(self.skip))
        


        
        movelist.close()

    #Initializes play
    def play(self):
        # selectpit = int(input("Player {}'s go. {} turns remaining. \n Please select a pit to play".format(self.currentplayer,self.turns)))

        self.initialize_game()
        skipturns  = 0
        self.currentplayer.switch()
        self.currentenemy.switch() 

        #number of turns for a player
        while self.game_status is True:
            self.gameturns += 1
            
            self.turns += 1
            self.turns = skipturns + self.turns #adds turns from skip
            print("Start of a new player's turn",self.turns)
            self.currentplayer.switch()
            self.currentenemy.switch() 
        
            while self.turns > 0:
                #resetting the status
                self.skip = False
                skipturns = 0
                self.steal = False
                self.free = False
                
                    
                # oldboard = copy.deepcopy(self.board)              

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
                self.lastmove = selectpit
                print(legal)

                while legal is False:
                    self.drawboard()
                    selectpit = int(input('invalid pit, please select pit (0-6)'))
                    self.lastmove = selectpit
                    legal = self.isvalid(selectpit)

                
                
                #making a move
                self.board = self.playermove(selectpit,options=self.options)

                #checks
                print('#############\nchecks initiated')
                
                ##checking if lastpit has n == 1

                #checking for free go. 
                self.free = self.checkfree()
                print('lastpitside')
                print(self.board[self.lastpitside][0])

                if self.free is True:
                    self.turns += 1
                
                #checking for steal or skip, this only occurs when lastpitn ==1
                

                elif self.board[self.lastpitside][0][self.lastpit] == 1:
                    print('lastpit has 1 marble, checking for steal and skip')
                    #checking for steal
                    self.steal = self.checksteal()
                    if self.steal is True:
                        self.board = self.stealfunc()

                    # checking for skip
                    self.skip = self.checkskip()
                    if self.skip is True:
                        skipturns = 1

                else:
                    pass
                print('#############\n')

                print('end of round playerinfo')
                print('currentplayer',self.currentplayer.player)
                print('currentenemy',self.currentenemy.player)
                

                self.save()
        
                self.drawboard()
                
                #checking whether the current player side is empty
                emptyside = self.checkemptyside()
                if emptyside is True:
                    self.turns = 0
                else:    
                    self.turns -= 1
            self.game_status, self.winner = self.check_game_status()
            print(self.game_status)
        
        print('Game ended')
        if self.winner is None:
            print('tie!')
        else:
            print('Player {} Wins!'.format(self.winner.player))
        
    #AI Functions WIP
        
    def max(self):
        return

    def min(self):
        return
                


def main():
    g = Game(7)
    g.play()

if __name__ == "__main__":
    main()
            

            
