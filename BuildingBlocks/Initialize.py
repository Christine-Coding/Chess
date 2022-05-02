import numpy as np

from BuildingBlocks.Pieces.Bishop import Bishop
from BuildingBlocks.Pieces.King import King
from BuildingBlocks.Pieces.Knight import Knight
from BuildingBlocks.Pieces.Pawn import Pawn
from BuildingBlocks.Pieces.Queen import Queen
from BuildingBlocks.Pieces.Rook import Rook
from BuildingBlocks.Classes.Square import Square


# create the board
def initialize_board(settings):
    board = np.empty((8, 8), dtype=Square)
    for i in range(8):
        for j in range(8):
            if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                board[i][j] = Square(i, j, "white", settings)
            else:
                board[i][j] = Square(i, j, "black", settings)
    return board


# initialize the pieces on the board
def initialize_pieces(board, color):
    i = [0, 1] if color == "white" else [7, 6]
    functions = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    # initializing the pieces
    for j, fun in zip(range(8), functions):
        # i[0] == 0 or 7
        board[j][i[0]].piece = fun(j, i[0], color)
    # initializing the pawns
    for k in range(8):
        # i[1] == 1 or 6
        board[k][i[1]].piece = Pawn(k, i[1], color)
