import numpy as np


def add_matrix(board):
    # 8x8 matrix with (color, piece)
    state = np.empty((8, 8), dtype=(int, 2))
    # piece/color name to int
    dict_colors = {"white": 1, "black": 2}
    dict_pieces = {"Pawn": 1, "Rook": 2, "Knight": 3, "Bishop": 4, "Queen": 5, "King": 6}
    for i in range(8):
        for j in range(8):
            if board[i][j].piece:
                state[i][j] = (dict_colors[board[i][j].piece.color], dict_pieces[board[i][j].piece.name])
            else:
                state[i][j] = (0, 0)
    return state
