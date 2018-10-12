class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece #only one player should be able to have one certain color. Make that work. 
        #self.chosen = []
        self.current_choice = self.get_choice()
        self.turn = 1 #shouldn't the player set the turn. ALSO, for testing. Del if uncesessary. 
        
    def get_name(self):
        self.name = input('What is your name? ')
    def get_choice(self):
        pass
#        if self.turn == 1:
#            self.choice = int(input('{}, where would you like to place your piece? '.format(self.name))) #need to check whose turn it is.
#        if self.turn == 2:
#            self.choice = int(input('In what column would you like to place your piece? ')) #need to check whose turn it is.
##        self.chosen.append(self.choice)
##        if self.choice == True:
##            print(self.chosen)
        
if __name__ == "__main__":
    Player('red')
    pass