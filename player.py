class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
        
    def get_name(self):
        self.name = input('What is your name? ')
        return self.name
    
    def get_choice(self):
        print()
        print(f'{self.name} In which column do you want to place your piece? ')
        print()
        choice = int(input('> '))
        return int(choice)

if __name__ == "__main__":
    pass