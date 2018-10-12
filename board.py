#Board by Egor Mikhaylov

class Board:
    def __init__(self, width, height):
        self.board_width = width
        self.board_height = height
        self.board = [["o"]*self.board_width for i in range(self.board_height)]
    
    def disp_board(self):
        for row in self.board:
            for element in row:
                print(element, end=' ')
            print()
        
    def add_piece(self, col, piece):
        placed = False
        for row in range(len(self.board)):
            for element in range(len(self.board[row])):
                if element == col-1:
                    if self.board[self.board_height-1][element] == "o" and placed == False:
                        if piece == "plus":
                            self.board[self.board_height-1][element] = "+"
                        else:
                            self.board[self.board_height-1][element] = "-"
                        placed = True
                    elif row != self.board_height-1 and placed == False:
                        if self.board[row+1][element] != "o":
                            if piece == "plus":
                                self.board[row][element] = "+"
                            else:
                                self.board[row][element] = "-"
                            placed = True
            

        