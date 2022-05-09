import numpy as np


class Game:
    def __init__(self, player_color: bool, opening: int):
        # track board states, moves, captures and matrices
        self.board_states = np.empty(5899, dtype=np)
        self.matrices = np.empty(5899, dtype=np)
        self.white_moves = []
        self.black_moves = []
        self.move_number = 0
        # track player color and whose move it is
        self.player_color = player_color  # True: white, False: black
        self.whose_turn = True  # True: white's turn, False: black's turn
        # track pawn promotions in progress, moves in progress and co-ordinates of the last move
        self.pawn_promotion = None  # Square
        self.move_piece = None  # Piece
        self.last_move = np.empty(0)   # Array of co-ordinates
        # lists of squares that are currently under attack by the enemy pieces
        self.fire_by_white_pieces = set()
        self.fire_by_black_pieces = set()
        self.under_fire = set()
        # set if or which openings learner is being used
        # 0 - none, 1 - one line, 2 - multiple lines
        self.opening = opening
