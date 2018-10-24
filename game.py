from board import Board
from player import Player

class Game:
    def __init__(self):
        self.players = []
        self.players.append(Player('x')) #player 1   should happen in play_game
        self.players.append(Player('o')) #player 2   so that the greeting comes first
        self.board = Board(7,6)
        self.turn = 0
               
    def play_game(self):
        '''allows for a game of Connect Four to be played.
            Two players will be allowed to face off against
            each other in a single game.
            
            One player will be able to win; however, it will
            allow for a draw to be called when appropriate. 
        '''
        print()
        print('Welcome to Connect Four!')
        while True:
            try:
                print()
                self.board.disp_board()
                self.choice = self.players[self.turn].get_choice()
                self.board.add_piece(self.choice, self.players[self.turn].piece)
                self.board.check_win()
                
                if self.board.check_win() == True: #don't need == True
                    self.board.disp_board()
                    print()
                    print(f"{self.players[self.turn].name} has won!")
                    print('Game Over')
                    self.board.empty_board()
                    return
                
                if self.board.check_win() == False: #unnecessary conditional
                    self.turn += 1
                    
                if self.board.is_full() == True:
                    self.board.disp_board()
                    print()
                    print('The board is full!')                    
                    print('It\'s a tie!')
                    self.board.empty_board()
                    print('Game Over')
                    return

                self.turn = self.turn % 2
                
            except Exception as e:
                print()
                print('That was not valid! {}'.format(str(e)))
                print()
    
if __name__ == "__main__":
    g = Game()
    g.play_game()
    