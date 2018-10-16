from board import Board
from player import Player

class Game:
    def __init__(self):
        self.players = []
        self.players.append(Player('x')) #player 1
        self.players.append(Player('o')) #player 2
        self.board = Board(7,7)
        self.turn = 0
        self.game = self.play_game()
        
    def play_game(self):
        print()
        while True:
            try:
                self.board.disp_board()
                self.choice = self.players[self.turn].get_choice()
                self.board.add_piece(self.choice, self.players[self.turn].piece)
                
                
                
                self.board.check_win()
                if self.board.check_win() == True:
                    print('Game Over')
                    break
                if self.board.check_win() == False:
                    self.turn += 1
                if self.board.is_full() == True:
                    pass
                    
                if self.board.is_full() == False:
                    print('Game Over')
                    
                    
                self.turn = self.turn % 2
                break
                
            except Exception as e:
                print()
                print('That was not valid! {}'.format(str(e)))
                print()
                break
    
if __name__ == "__main__":
    Game()
    