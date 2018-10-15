class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
        self.choice = self.get_choice()
        #self.current_choice = self.get_choice()
        #self.turn = 1 #shouldn't the player set the turn. ALSO, for testing. Del if uncesessary. 
        
    def get_name(self):
        self.name = input('What is your name? ')
    def get_choice(self):
        self.choice = int(input('In which column do you want to place your piece? '))
        

if __name__ == "__main__":
    Player('red')
    #pass