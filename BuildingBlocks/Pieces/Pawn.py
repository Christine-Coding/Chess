import re


class Pawn:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color
        self.name = "Pawn"
        self.abbreviation = ""

    def __str__(self) -> str:
        return ''.join([self.color, ' ', self.name])

    def possible_moves(self, board):
        possible_new_squares = []
        if self.color == "white":
            if board[self.x][self.y + 1].piece is None:
                # starting with 2 steps
                if self.y == 1 and board[self.x][self.y + 2].piece is None:
                    possible_new_squares.append((self.x, self.y + 2))
                # 1 step forward
                if self.y < 6:
                    possible_new_squares.append((self.x, self.y + 1))
        else:
            if board[self.x][self.y - 1].piece is None:
                # black starting with 2 steps
                if self.y == 6 and board[self.x][self.y - 2].piece is None:
                    possible_new_squares.append((self.x, self.y - 2))
                # 1 step forward
                if self.y > 1:
                    possible_new_squares.append((self.x, self.y - 1))
        return possible_new_squares

    def possible_captures(self, board):
        possible_captures = []
        # regular capturing
        if self.color == "white":
            if self.y < 6:
                if self.x < 7:
                    if board[self.x + 1][self.y + 1].piece and board[self.x + 1][self.y + 1].piece.color != self.color:
                        possible_captures.append((self.x + 1, self.y + 1))
                if self.x > 0:
                    if board[self.x - 1][self.y + 1].piece and board[self.x - 1][self.y + 1].piece.color != self.color:
                        possible_captures.append((self.x - 1, self.y + 1))
        else:  # black
            if self.y > 1:
                if self.x < 7:
                    if board[self.x + 1][self.y - 1].piece and board[self.x + 1][self.y - 1].piece.color != self.color:
                        possible_captures.append((self.x + 1, self.y - 1))
                if self.x > 0:
                    if board[self.x - 1][self.y - 1].piece and board[self.x - 1][self.y - 1].piece.color != self.color:
                        possible_captures.append((self.x - 1, self.y - 1))
        return possible_captures

    def possible_promotions(self, board):
        possible_promotions = []
        if self.color == "white":
            if self.y == 6:
                # promote
                if board[self.x][self.y + 1].piece is None:
                    possible_promotions.append((self.x, self.y + 1))
                # capture right and promote
                if self.x < 7:
                    if board[self.x + 1][self.y + 1].piece and board[self.x + 1][self.y + 1].piece.color != self.color:
                        possible_promotions.append((self.x + 1, self.y + 1))
                # capture left and promote
                if self.x > 0:
                    if board[self.x - 1][self.y + 1].piece and board[self.x - 1][self.y + 1].piece.color != self.color:
                        possible_promotions.append((self.x - 1, self.y + 1))
        else:  # black
            if self.y == 1:
                # promote
                if board[self.x][self.y - 1].piece is None:
                    possible_promotions.append((self.x, self.y - 1))
                # capture right and promote
                if self.x < 7:
                    if board[self.x + 1][self.y - 1].piece and board[self.x + 1][self.y - 1].piece.color != self.color:
                        possible_promotions.append((self.x + 1, self.y - 1))
                # capture left and promote
                if self.x > 0:
                    if board[self.x - 1][self.y - 1].piece and board[self.x - 1][self.y - 1].piece.color != self.color:
                        possible_promotions.append((self.x - 1, self.y - 1))

        return possible_promotions

    def possible_en_passant(self, last_moved_piece, previous_board_state):
        dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        possible_en_passant = ()
        if self.color == "white":
            if self.y == 4:
                matcher = re.compile('[a-h]5')
                if matcher.match(last_moved_piece) and previous_board_state[dict[last_moved_piece[0]]][6].piece.name == "Pawn"\
                        and previous_board_state[dict[last_moved_piece[0]]][6].piece.color == "black":
                    possible_en_passant = (dict[last_moved_piece[0]], self.y + 1)
        else:  # black
            if self.y == 3:
                matcher = re.compile('[a-h]4')
                if matcher.match(last_moved_piece) and previous_board_state[dict[last_moved_piece[0]]][1].piece.name == "Pawn"\
                        and previous_board_state[dict[last_moved_piece[0]]][1].piece.color == "white":
                    possible_en_passant = (dict[last_moved_piece[0]], self.y - 1)
        return possible_en_passant
