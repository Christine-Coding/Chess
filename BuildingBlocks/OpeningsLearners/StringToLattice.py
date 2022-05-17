import re
from copy import deepcopy

from BuildingBlocks.Classes.Settings import Settings
from BuildingBlocks.Initialize import initialize_board, initialize_pieces
from BuildingBlocks.OpeningsLearners.Helpers import add_matrix
from BuildingBlocks.OpeningsLearners.ReadLines import read_lines
from BuildingBlocks.Pieces.Bishop import Bishop
from BuildingBlocks.Pieces.King import King
from BuildingBlocks.Pieces.Knight import Knight
from BuildingBlocks.Pieces.Queen import Queen
from BuildingBlocks.Pieces.Rook import Rook


def lines_to_matrices(lines=read_lines(r"C:\Users\Christine\Documents\Programming\Chess\BuildingBlocks\OpeningsLearners\Lines\clean_lines.txt")):
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

        # Opening line to a list of matrices
        matrices = [add_matrix(board)]
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
            elif re.match(r"(O-O).*$", move):
                board = castle(board, move, "white" if counter else "black")
            elif "=" in move:
                board = promote(board, move, "white" if counter else "black")
            else:
                # TODO - en passant
                board = move_a_piece(board, move, "Pawn", "white" if counter else "black")
            counter = not counter
            matrices.append(add_matrix(board))
        print("FINISH")
        print()
        matrix_lists.append(matrices)
    return matrix_lists


# board, move == Nxd4, move_piece = "Knight", move_piece_color == "white"
def move_a_piece(board, move, move_piece, move_piece_color):
    dict_let = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    dict_num = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8'}
    # capture
    if "x" in move:
        capture = move.split("x")[-1]
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
    return board


# board, move == e8=Q, move_piece_color == "white"
def promote(board, move, move_piece_color):
    dict_let = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    dict_num = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8'}
    j = 6 if move_piece_color == "white" else 1
    promotion, to_piece = move.split("=")
    promotion = promotion.split("x")[-1] if "x" in promotion else promotion
    for i in range(8):
        if board[i][j].piece and board[i][j].piece.name == "Pawn" and board[i][j].piece.color == move_piece_color:
            for (x, y) in board[i][j].piece.possible_promotions(board):
                if promotion == (dict_let[x] + dict_num[y]):
                    print("promote", move, dict_let[x] + dict_num[y] + "=" + to_piece)
                    if to_piece == "Q":
                        board[x][y].piece = Queen(x, y, move_piece_color)
                    elif to_piece == "R":
                        board[x][y].piece = Rook(x, y, move_piece_color)
                    elif to_piece == "N":
                        board[x][y].piece = Knight(x, y, move_piece_color)
                    else:
                        board[x][y].piece = Bishop(x, y, move_piece_color)
                    board[i][j].piece = None
                    return board


# board, move == 0-0-0, move_piece_color == "white"
def castle(board, move, move_piece_color):
    dict_let = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    dict_num = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8'}
    y = 0 if move_piece_color == "white" else 7
    if re.match(r"(O-O-O).*$", move):
        print("LONG castles", move)
        board[2][y].piece = King(2, y, move_piece_color)
        board[3][y].piece = Rook(3, y, move_piece_color)
        board[4][y].piece = None
        board[1][y].piece = None
    else:
        print("SHORT castles", move)
        board[6][y].piece = King(2, y, move_piece_color)
        board[5][y].piece = Rook(3, y, move_piece_color)
        board[7][y].piece = None
        board[4][y].piece = None
    return board

# lines_to_matrices()
