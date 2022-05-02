def show_possible_moves(board, move_piece, possible_moves_color):
    # color the possible moves (squares)
    possible_moves = move_piece.possible_moves(board)
    if possible_moves:
        color = possible_moves_color
        for el in possible_moves:
            board[el[0]][el[1]].marked = color


def show_possible_captures(board, move_piece, possible_captures_color):
    # color the possible captures
    possible_captures = move_piece.possible_captures(board)
    if possible_captures:
        color = possible_captures_color
        for el in possible_captures:
            board[el[0]][el[1]].marked = color


def show_possible_castling(board, move_piece, possible_castling_color):
    # color the possible castling
    possible_castling = move_piece.possible_castling(board)
    if possible_castling:
        for el in possible_castling:
            board[el[0][0]][el[0][1]].marked = possible_castling_color


def show_possible_promotion(board, move_piece, possible_promotions_color):
    # color the possible castling
    possible_promotions = move_piece.possible_promotions(board)
    if possible_promotions:
        for el in possible_promotions:
            board[el[0]][el[1]].marked = possible_promotions_color


def show_possible_en_passant(board, move_piece, possible_en_passant_color, last_moved_piece, previous_board_state):
    # color the possible en passant
    possible_en_passant = move_piece.possible_en_passant(last_moved_piece, previous_board_state)
    if possible_en_passant:
        board[possible_en_passant[0]][possible_en_passant[1]].marked = possible_en_passant_color
