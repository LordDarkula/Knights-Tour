import chess_py

empty_board = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
]

my_board = chess_py.Board(empty_board)
node_graph = chess_py.Board(empty_board)

knight_loc = chess_py.Location(0, 0)

tour_knight = chess_py.Knight(chess_py.Color.init_white(), knight_loc)
my_board.place_piece_at_square(tour_knight, knight_loc)

def next_squares(location):
    return chess_py.Knight(chess_py.Color.init_white(), location).possible_moves(node_graph)

class Node:
    def __init__(self, head, *args):
        self.head = head
        self.tails = args
