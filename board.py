#Board by Egor Mikhaylov

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[" "]*self.width for i in range(self.height)]
    
    def disp_board(self):
        print("--"*self.width)
        col_num = []
        for row in self.board:
            for element in row:
                print(element, end=' ')
            print()
        for i in range(1, self.width+1):
            col_num += [i]
        print("--"*self.width)
        print(*col_num)
        
    def add_piece(self, col, piece):
        if col > self.height+1 or col < 1:
            raise ValueError("Invalid Column")
        placed = False
        for row in range(len(self.board)):
            for element in range(len(self.board[row])):
                if element == col-1:
#                    for element in self.board[0]:
#                        if element != " ":
#                            full = True
#                    if full == True:
#                        raise ValueError("Column Full")
                    if self.board[self.height-1][element] == " " and placed == False:
                        if piece == "x":
                            self.board[self.height-1][element] = "x"
                        else:
                            self.board[self.height-1][element] = "o"
                        placed = True
                    elif row != self.height-1 and placed == False:
                        if self.board[row+1][element] != " ":
                            if piece == "x":
                                self.board[row][element] = "x"
                            else:
                                self.board[row][element] = "o"
                            placed = True
        
    def empty_board(self):
        self.board = [[" "]*self.width for i in range(self.height)]
        
    def check_win(self):
        for row in range(len(self.board)):
            for element in range(len(self.board[row])):
                c = element-4
                h_sequence = [self.board[row][c], self.board[row][c+1], self.board[row][c+2], self.board[row][c+3]]
                value = h_sequence[0]
                identical = False
                for i in range(4):
                    if h_sequence[i] == value:
                        if value != " ":
                            identical = True
                    else:
                        identical = False
                        break
                if identical == True:
                    return(True)
            for element in range(len(self.board[row])):
                r = row-4
                v_sequence = [self.board[r][element], self.board[r+1][element], self.board[r+2][element], self.board[r+3][element]]
                value = v_sequence[0]
                for i in range(4):
                    if v_sequence[i] == value:
                        if value != " ":
                            identical = True
                    else:
                        identical = False
                        break
                if identical == True:
                    return(True)
        if identical == False:
            return(False)
                
                    
    def is_full(self):
        not_empty = False
        for row in self.board:
            for element in row:
                if element == " ":
                    not_empty = True
        if not_empty == False:
            return(True)
        else:
            return(False)
        
        
    
            

        