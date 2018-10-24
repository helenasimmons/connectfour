#player by Helena Simmons

class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
        
    def get_name(self):
        '''Asks and allows the player to input their name. 
        '''
        self.name = input('What is your name? ')
        return self.name # unnecessary
    
    def get_choice(self):
        '''Allows for the player to choose a column in which to place their piece.
'''
        print()
        print(f'{self.name}, in which column do you want to place your piece? ')
        print()
        choice = int(input('> '))
        return int(choice)

if __name__ == "__main__":
    pass