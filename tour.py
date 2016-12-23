from chess_py import *

class Fill_square:
    color = color.white
    sym = 0

    def __init__(self):
        __class__.sym += 1
        self.symbol = str(__class__.sym)

    def __str__(self):
        return self.symbol


empty = [[None for _ in range(8)] for _ in range(8)]
my_board = Board(empty)

knight = Knight(color.white, Location(0, 0))
my_board.place_piece_at_square(knight, Location(0, 0)) # Change starting point here

moves = knight.possible_moves(my_board)
while len(moves) > 0:
    print(my_board)
    corner_move = None
    min_poss = None
    current_loc = knight.location

    for move in moves:
        my_board.update(move)
        my_board.place_piece_at_square(Pawn(color.white, current_loc), current_loc)
        poss_len = len(knight.possible_moves(my_board))

        if min_poss is None or min_poss > poss_len:
            corner_move = move
            min_poss = poss_len

        my_board.move_piece(move.end_loc, current_loc)

    my_board.update(corner_move)
    my_board.place_piece_at_square(Fill_square(), current_loc)
    moves = knight.possible_moves(my_board)

print(my_board)
