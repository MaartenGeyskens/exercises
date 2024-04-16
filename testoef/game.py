from player import Player
from board import Board

class Game:

    def __init__(self):
        print("Start Spel")
        p1 = Player("Bart", "X")
        p2 = Player("Dries", "0")

        print(p1)
        print(p2)

        board= Board(7,6)
        print(board)
        board.print_board()

        row = board.empty_row_for_column(0)
        board.add_token(row,0,"X")
        board.print_board()
       
game = Game()
