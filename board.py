#Board by Egor Mikhaylov

class Board:
    def __init__(self):
        self.board_width = 7 #temp
        self.board_height = 8 #temp
        self.board = [["o"]*self.board_width for i in range(self.board_height)]
    
    def make_board(self):
        for row in self.board:
            for element in row:
                print(element, end=' ')
            print()
            

        