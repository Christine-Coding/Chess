class King:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color
        self.name = "King"
        self.abbreviation = "K"
        self.has_not_moved = True

    def __str__(self) -> str:
        return ''.join([self.color, ' ', self.name])

    def possible_moves(self, board):
        possible_new_squares = []
        # movement to the left
        if self.x != 0 and board[self.x - 1][self.y].piece is None:
            possible_new_squares.append((self.x - 1, self.y))
        # movement to the right
        if self.x != 7 and board[self.x + 1][self.y].piece is None:
            possible_new_squares.append((self.x + 1, self.y))
        # movement downwards
        if self.y != 0 and board[self.x][self.y - 1].piece is None:
            possible_new_squares.append((self.x, self.y - 1))
        # movement upwards
        if self.y != 7 and board[self.x][self.y + 1].piece is None:
            possible_new_squares.append((self.x, self.y + 1))

        # movement to the left diagonally down
        if not (self.x - 1 < 0 or self.y - 1 < 0) and board[self.x - 1][self.y - 1].piece is None:
            possible_new_squares.append((self.x - 1, self.y - 1))
        # movement to the right diagonally down
        if not (self.x > 7 or self.y - 1 < 0) and board[self.x + 1][self.y - 1].piece is None:
            possible_new_squares.append((self.x + 1, self.y - 1))
        # movement to the right diagonally up
        if not (self.x + 1 > 7 or self.y + 1 > 7) and board[self.x + 1][self.y + 1].piece is None:
            possible_new_squares.append((self.x + 1, self.y + 1))
        # movement to the left diagonally up
        if not (self.x - 1 < 0 or self.y + 1 > 7) and board[self.x - 1][self.y + 1].piece is None:
            possible_new_squares.append((self.x - 1, self.y + 1))

        return possible_new_squares

    def possible_captures(self, board):
        possible_captures = []
        # movement to the left
        if self.x != 0 and board[self.x - 1][self.y].piece and board[self.x - 1][self.y].piece.color != self.color:
            possible_captures.append((self.x - 1, self.y))
        # movement to the right
        if self.x != 7 and board[self.x + 1][self.y].piece and board[self.x + 1][self.y].piece.color != self.color:
            possible_captures.append((self.x + 1, self.y))
        # movement downwards
        if self.y != 0 and board[self.x][self.y - 1].piece and board[self.x][self.y - 1].piece.color != self.color:
            possible_captures.append((self.x, self.y - 1))
        # movement upwards
        if self.y != 7 and board[self.x][self.y + 1].piece and board[self.x][self.y + 1].piece.color != self.color:
            possible_captures.append((self.x, self.y + 1))

        # movement to the left diagonally down
        if not (self.x - 1 < 0 or self.y - 1 < 0) and board[self.x - 1][self.y - 1].piece and \
                board[self.x - 1][self.y - 1].piece.color != self.color:
            possible_captures.append((self.x - 1, self.y - 1))
        # movement to the right diagonally down
        if not (self.x > 7 or self.y - 1 < 0) and board[self.x + 1][self.y - 1].piece and \
                board[self.x + 1][self.y - 1].piece.color != self.color:
            possible_captures.append((self.x + 1, self.y - 1))
        # movement to the right diagonally up
        if not (self.x + 1 > 7 or self.y + 1 > 7) and board[self.x + 1][self.y + 1].piece and \
                board[self.x + 1][self.y + 1].piece.color != self.color:
            possible_captures.append((self.x + 1, self.y + 1))
        # movement to the left diagonally up
        if not (self.x - 1 < 0 or self.y + 1 > 7) and board[self.x - 1][self.y + 1].piece and \
                board[self.x - 1][self.y + 1].piece.color != self.color:
            possible_captures.append((self.x - 1, self.y + 1))

        return possible_captures

    def possible_castling(self, board):
        possible_castling = []
        if self.color == "white":
            if self.has_not_moved:
                # long castles
                # king and rook have not moved
                if board[0][0].piece and board[0][0].piece.name == "Rook" and board[0][0].piece.has_not_moved:
                    # no pieces in between
                    if not board[1][0].piece and not board[2][0].piece and not board[3][0].piece:
                        possible_castling.append(
                            [(2, 0), (4, 0), (3, 0), (0, 0)])  # king new, king old, rook new, rook old
                # short castles
                # king and rook have not moved
                if board[7][0].piece and board[7][0].piece.name == "Rook" and board[7][0].piece.has_not_moved:
                    # no pieces in between
                    if not board[5][0].piece and not board[6][0].piece:
                        possible_castling.append(
                            [(6, 0), (4, 0), (5, 0), (7, 0)])  # king new, king old, rook new, rook old

        if self.color == "black":
            if self.has_not_moved:
                # long castles
                # king and rook have not moved
                if board[0][7].piece and board[0][7].piece.name == "Rook" and board[0][7].piece.has_not_moved:
                    # no pieces in between
                    if not board[1][7].piece and not board[2][7].piece and not board[3][7].piece:
                        possible_castling.append(
                            [(2, 7), (4, 7), (3, 7), (0, 7)])  # king new, king old, rook new, rook old
                # short castles
                # king and rook have not moved
                if board[7][7].piece and board[7][7].piece.name == "Rook" and board[7][7].piece.has_not_moved:
                    # no pieces in between
                    if not board[5][7].piece and not board[6][7].piece:
                        possible_castling.append(
                            [(6, 7), (4, 7), (5, 7), (7, 7)])  # king new, king old, rook new, rook old

        return possible_castling
