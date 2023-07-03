import numpy as np 

name_ex = input("Please write what you wish your player name to be: ")

from classplayer import Player #this allows players to create a username that can't be changed 
# i moved this class to seperate file so the progam wouldn't be so slow in running

print(Player(name_ex))

#begins generation of board 

class Board:
    def __init__(self, level):
        self._level = level 
        self.board1 = None
        self.board2 = None 
    
    '''level is an attribute that determines which version of the 
      board that ends up being returned'''
    @property 
    def level(self):
         return self._level 
    
    @level.setter 
    def level(self, ins): 
        ins = str(ins).upper()
        if isinstance(ins, str): 
            if ins == 'EASY':
                self._level = 'easy'
            if ins == 'MEDIUM':
                self._level = 'medium'
            elif ins == 'HARD':
                self._level = 'hard'
            else: 
                raise TypeError(f"please enter either 'easy', 'medium' or 'hard' as the level")
        else: 
            raise ValueError(f'please enter string value (either "easy" or "medium" or "hard") for your input')   

    def grid(self): #generate an initial grid that follows the parameters of Sudoku
        base  = 3
        side  = base*base

        def pattern(r, c):
            return (base * (r % base) + r // base + c) % side + 1

        # makes the soduku board using the pattern and random numbers
        board = [[pattern(r, c) for c in range(side)] for r in range(side)]
        self.board1 = np.array(board)
        return self.board1


    
    def chosenlevel(self): # choosing and setting a difficulting level as inputted by user 
        '''the parameters for possible replacement increase by 
        increasing the divisible factors chosen at each level''' 
        if self._level == 'easy': 
            gone = np.random.randint(2,4) 
            for row in self.board1:
                for x in row: 
                    if int(x)%gone == 0: 
                        self.board1[self.board1 == int(x)] = 0
        if self._level == 'medium': 
            gone = np.random.randint(2,8)
            for row in self.board1:
                for x in row: 
                    if int(x)%gone == 0: 
                        self.board1[self.board1 == int(x)] = 0
        if self._level == 'hard': 
            gone = np.random.randint(2,8)
            for row in self.board1:
                for x in row: 
                    if int(x)%gone == 0: 
                        self.board1[self.board1 == int(x)] = 0
                    else: 
                        gone = np.random.randint(2,4)
                        for row in self.board1:
                            for x in row: 
                                if int(x)%gone == 0: 
                                    self.board1[self.board1 == int(x)] = 0
        return self.board1
    
    def ux(self): #how the user can input values 
        print('instructions: the locations where there are 0s are where you can fill in with a digit. play soduku as you normally would, by identifuing the index of where you would like to replace a 0 with the number you would like to input. you can not replace non-zero numbers, they are your hints. good luck!')
        if np.any(self.board1==0): 
            all_done = False #all_done, or the game will only be done (all_done = True) when no zeros are present 
        else: 
            all_done = True 
            self.board1 = self.board2

        while all_done == False:  
            row = int(input("enter the row of the index location you wish to modify (0-8):  "))
            if row > 8 or row <0 : 
                raise ValueError('invalid index')
            col = int(input("enter the column of the index location you wish to modify (0-8):  "))
            if col > 8 or col <0 : 
                raise ValueError('invalid index')
            dig = int(input("enter the digit you would like to replace the zero with (1-9):  "))
            if dig >9 or dig <0:
                raise ValueError('invalid digit')
            
            if self.board1[row][col] != 0:
                raise IndexError("The cell is already filled. Try again") 
            else: 
                self.board1[row][col] = dig
                
            print(self.board1)
            '''my current issue is that the game ends if an error is raised.
             currently reworking the loops to try and fix this issue'''
    def checker(self): #verifies at the end to see if the user inputted correct values
    #if all_done = True: 
        check = False 
        while check == False:
            #checking rows
            for row in self.board2: 
                if len(set(row)) != len(row):
                    check = False 
            #checking columns 
            matrix = self.board2 
            for col in matrix.T:
                if len(set(col)) != len(col): 
                    check = False 
            #checking 3x3 squares
            for p in range(0,9,3):
                for o in range(0,9,3):
                    square = self.board2[p:p+3, o:o+3].flatten()
                    if len(set(square)) == len(square):
                        check = True 
                    else: 
                        print("something's not right... try again")
        if check == True: 
            print("YOU GOT IT!! you're a genius!! congrats :)")

board = Board('easy')
board.grid()
print(board.chosenlevel())
board.ux()    
board.checker()
    
   


