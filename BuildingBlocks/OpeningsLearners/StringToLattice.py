# TODO - black vs white start (determine),
#  account for spaces after the move number
import re
import numpy as np
from copy import deepcopy

from BuildingBlocks.Classes.Settings import Settings
from BuildingBlocks.Initialize import initialize_board, initialize_pieces
from BuildingBlocks.OpeningsLearners.ReadLines import read_lines

lines = read_lines("Lines\Sicilian-Defence.txt")


def lines_to_matrices(lines):
    matrix_lists = []
    for (name, moves) in lines:
        # Initialize the board representation of the game
        settings = Settings(player_color=False, show_tile_labels=False,
                            possible_moves_color="grey", possible_captures_color="red", possible_castling_color="black",
                            possible_promotions_color="green", possible_en_passant_color="gray", last_move_color="yellow",
                            tile_size=75, white_tile_color="white", black_tile_color="Sienna")
        board = initialize_board(settings)
        initialize_pieces(board, "white")
        initialize_pieces(board, "black")

        # 8x8 matrix with (color, piece)
        initial_state = np.empty((8, 8), dtype=(int, 2))
        # piece/color name to int
        dict_colors = {"white": 1, "black": 2}
        dict_pieces = {"Pawn": 1, "Rook": 2, "Knight": 3, "Bishop": 4, "Queen": 5, "King": 6}
        for i in range(8):
            for j in range(8):
                if board[i][j].piece:
                    initial_state[i][j] = (dict_colors[board[i][j].piece.color], dict_pieces[board[i][j].piece.name])
                else:
                    initial_state[i][j] = (0, 0)

        # Opening line to a list of matrices
        matrices = [initial_state]
        counter = True  # white starts
        for move in moves:
            move = move.strip("+").strip("#")
            if re.match(r"^(R).*$", move):
                board = move_a_piece(board, move, "Rook", "white" if counter else "black")
            elif re.match(r"^(N).*$", move):
                board = move_a_piece(board, move, "Knight", "white" if counter else "black")
            elif re.match(r"^(B).*$", move):
                board = move_a_piece(board, move, "Bishop", "white" if counter else "black")
            elif re.match(r"^(Q).*$", move):
                board = move_a_piece(board, move, "Queen", "white" if counter else "black")
            elif re.match(r"^(K).*$", move):
                board = move_a_piece(board, move, "King", "white" if counter else "black")
            elif re.match(r"(O-O-O).*$", move):
                print("Long castles", move)
                None
            elif re.match(r"(O-O).*$", move):
                print("Short castles", move)
                None
            elif "=" in move:
                board = promote(board, move, "white" if counter else "black")
            else:
                # TODO - en passant, promotion
                board = move_a_piece(board, move, "Pawn", "white" if counter else "black")
            counter = not counter
        matrix_lists.append(matrices)
    return matrix_lists


# board, move == Nxd4, move_piece = "Knight", move_piece_color == "white"
def move_a_piece(board, move, move_piece, move_piece_color):
    dict_let = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    dict_num = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8'}
    # capture
    if "x" in move:
        with_piece, capture = move.split("x")
        for i in range(8):
            for j in range(8):
                if board[i][j].piece and board[i][j].piece.name == move_piece and board[i][j].piece.color == move_piece_color:
                    for (x, y) in board[i][j].piece.possible_captures(board):
                        if capture == (dict_let[x] + dict_num[y]):
                            print("CAPTURE", capture, board[i][j].piece.abbreviation + "x" + dict_let[x] + dict_num[y])
                            board[x][y].piece = board[i][j].piece
                            board[x][y].piece.x = x
                            board[x][y].piece.y = y
                            board[i][j].piece = None
                            return board
    # move
    else:
        for i in range(8):
            for j in range(8):
                if board[i][j].piece and board[i][j].piece.name == move_piece and board[i][j].piece.color == move_piece_color:
                    for (x, y) in board[i][j].piece.possible_moves(board):
                        if move == (board[i][j].piece.abbreviation + dict_let[x] + dict_num[y]):
                            print("move", move, board[i][j].piece.abbreviation + dict_let[x] + dict_num[y])
                            board[x][y].piece = deepcopy(board[i][j].piece)
                            board[x][y].piece.x = x
                            board[x][y].piece.y = y
                            board[i][j].piece = None
                            return board
    print("FINISH")
    return board


# board, move == e8=Q, move_piece_color == "white"
def promote(board, move, move_piece_color):
    dict_let = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    dict_num = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8'}
    j = 6 if move_piece_color == "white" else 1
    promotion, to_piece = move.split("=")
    for i in range(8):
        if board[i][j].piece and board[i][j].piece.name == "Pawn" and board[i][j].piece.color == move_piece_color:
            for (x, y) in board[i][j].piece.possible_promotions(board):
                if promotion == (dict_let[x] + dict_num[y]):
                    print("move", move, board[i][j].piece.abbreviation + dict_let[x] + dict_num[y])
                    board[x][y].piece = deepcopy(board[i][j].piece)
                    board[x][y].piece.x = x
                    board[x][y].piece.y = y
                    board[i][j].piece = None
                    return board


lines_to_matrices(lines)
