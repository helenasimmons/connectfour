from board import Board
from player import Player

class Game:
    def __init__(self):
        #self.players = []
        self.player1 = Player('red') #TEST STUFF. Del later. 
        self.player2 = Player('yellow') #TEST STUFF. Del later. 
        self.board = Board()
        self.turn = 1 #Sets player1. Could be set to 2 if Player2's turn is up. 
        
    def play_game(self):
        pass
    
if __name__ == "__main__":
    Game()
    pass