class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
        self.turn = 0 
        
    def get_name(self):
        self.name = input('What is your name? ')
        return self.name
    def get_choice(self):
        self.choice = int(input('In which column do you want to place your piece? '))
        return int(self.choice)

if __name__ == "__main__":
    pass