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
        
        if self.board[0][col-1] != " ":
            raise ValueError("Column Full")
        
        for row in range(len(self.board)):
            if self.board[self.height-1-row][col-1] == " ":
                self.board[self.height-1-row][col-1] = piece
                break
                
        
    def empty_board(self):
        self.board = [[" "]*self.width for i in range(self.height)]
        
    def check_win(self):
        if self.height < 4 or self.width < 4:
            return(False)
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
            for element in range(len(self.board[row])):
                r = row-3
                c = element-3
                d_neg_sequence = [self.board[r][c], self.board[r+1][c+1], self.board[r+2][c+2], self.board[r+3][c+3]]
                for i in range(4):
                    if d_neg_sequence[i] == d_neg_sequence[0]:
                        if d_neg_sequence[0] != " ":
                            identical = True
                    else:
                        identical = False
                        break
                if identical == True:
                    return(True)
            for element in range(len(self.board[row])):
                r = row-3
                d_pos_sequence = [self.board[r][c], self.board[r-1][0+1], self.board[r-2][0+2], self.board[r-3][0+3]]
                for i in range(4):
                    if d_pos_sequence[i] == d_pos_sequence[0]:
                        if d_pos_sequence[0] != " ":
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
        
        
            

        