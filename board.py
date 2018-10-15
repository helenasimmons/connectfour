#Board by Egor Mikhaylov

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[" "]*self.width for i in range(self.height)]
    
    def disp_board(self):
        col_num = []
        for row in self.board:
            for element in row:
                print(element, end=' ')
            print()
        for i in range(1, self.width+1):
            col_num += [i]
        print(*col_num)
        
    def add_piece(self, col, piece):
        placed = False
        for row in range(len(self.board)):
            for element in range(len(self.board[row])):
                if element == col-1:
                    if self.board[self.height-1][element] == " " and placed == False:
                        if piece == "plus":
                            self.board[self.height-1][element] = "+"
                        else:
                            self.board[self.height-1][element] = "-"
                        placed = True
                    elif row != self.height-1 and placed == False:
                        if self.board[row+1][element] != " ":
                            if piece == "plus":
                                self.board[row][element] = "+"
                            else:
                                self.board[row][element] = "-"
                            placed = True
        
    def empty_board(self):
        self.board = [[" "]*self.width for i in range(self.height)]
        
    def check_win(self):
        for row in range(len(self.board)):
            for element in range(len(self.board[row])):
                h_sequence = [self.board[row][element], self.board[row][element+1], self.board[row][element+2], self.board[row][element+3]]
                value = h_sequence[0]
                identical = False
                for i in range(4):
                    if h_sequence[i] == value:
                        print(h_sequence)
                        if value != " ":
                            identical = True
                    else:
                        identical = False
                if identical == True:
                    return(True)
        if identical == False:
            return(False)
                
                    
    def is_full(self):
        for row in self.board:
            for element in row:
                if element == " ":
                    not_empty = True
        if not_empty == False:
            return(True)
        else:
            return(False)
        
        
    
            

        