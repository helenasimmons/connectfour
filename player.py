class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
    def get_name(self):
        self.name = input('What is your name? ')
    def get_choice(self):
        pass
#    def get_choice(self):
        
if __name__ == "__main__":
    Player('red')
    pass