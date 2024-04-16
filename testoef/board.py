class Board():

    def __init__(self, columns, rows):
        self.__columns = columns
        self.__rows = rows
        self.__initialize_board()

    def initialize_board(self):
        self.__board = []
        for r in range(0,self.__rows):
            row = []
            for c in range(0, self.__columns):
                row.append(" ")
            self.__board.append(row)

    
    def print_board(self):
        print("Board is printing")
        self.__print_number
        self.___print_line()
        for row in self.__board:
            self.__print_row()

    def __print_line(self):
        line = " "
        line += "_" * (self.__columns * 4 -1)
        line += " "
        print(line)

    def __print_row(self, row):
        row = "|"
        for c in range(0, self.__columns):
            line += f" {row[c]} |"
        print(line)

    def __print_number(self):
        line = " "
        for c in range (0,self.__columns):
            header = c + 1
            if header < 10:
                line += f" {header} "

            else:
                line += f" {header} "
        print(line)
    
    def add_token(self,row, column, token):
        self.__board[row][column] = token

    def empty_row_for_column(self, column):
        for c in range(self.__rows -1, -1, -1):
            if self.__board[c][column] == " ":
                return c
        return -1
