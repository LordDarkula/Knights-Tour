import chess_py
from copy import deepcopy as cp

class Node(object):
    def __init__(self, head):
        self.head = head
        self.visited = False
        self.tails = []

    def add_tails(self, tails):
        self.tails.extend(tails)

    def number_of_tails(self):
        connections = 0
        for tail in self.tails:
            if not tail.visited:
                connections += 1
        return connections


empty = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
]

my_board = chess_py.Board(empty)
empty_board = chess_py.Board(empty)

knight_loc = chess_py.Location(0, 0)

tour_knight = chess_py.Knight(chess_py.Color.init_white(), knight_loc)
my_board.place_piece_at_square(tour_knight, knight_loc)

def next_squares(location):
    return chess_py.Knight(chess_py.Color.init_white(), location).possible_moves(empty_board)

node_graph = cp(empty)

for i in range(len(node_graph)):
    for j in range(len(node_graph[i])):
        node_graph[i][j] = Node(chess_py.Location(i, j))

for i in range(len(node_graph)):
    for j in range(len(node_graph[i])):
        node_graph[i][j].add_tails(next_squares(chess_py.Location(i, j)))

