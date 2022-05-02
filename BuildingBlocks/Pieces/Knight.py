class Knight:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color
        self.name = "Knight"
        self.abbreviation = "N"

    def __str__(self) -> str:
        return ''.join([self.color, ' ', self.name])

    def possible_moves(self, board):
        possible_new_squares = []
        if 7 >= self.x - 1 >= 0:
            # left 2 down
            if 7 >= self.y - 2 >= 0 and board[self.x - 1][self.y - 2].piece is None:
                possible_new_squares.append((self.x - 1, self.y - 2))
            # left 2 up
            if 7 >= self.y + 2 >= 0 and board[self.x - 1][self.y + 2].piece is None:
                possible_new_squares.append((self.x - 1, self.y + 2))

        if 0 <= self.x + 2 <= 7:
            # 2 right down
            if 0 <= self.y - 1 <= 7 and board[self.x + 2][self.y - 1].piece is None:
                possible_new_squares.append((self.x + 2, self.y - 1))
            # 2 right up
            if 0 <= self.y + 1 <= 7 and board[self.x + 2][self.y + 1].piece is None:
                possible_new_squares.append((self.x + 2, self.y + 1))

        if 7 >= self.x + 1 >= 0:
            # right 2 down
            if 7 >= self.y - 2 >= 0 and board[self.x + 1][self.y - 2].piece is None:
                possible_new_squares.append((self.x + 1, self.y - 2))
            # right 2 up
            if 7 >= self.y + 2 >= 0 and board[self.x + 1][self.y + 2].piece is None:
                possible_new_squares.append((self.x + 1, self.y + 2))

        if 0 <= self.x - 2 <= 7:
            # 2 left up
            if 0 <= self.y + 1 <= 7 and board[self.x - 2][self.y + 1].piece is None:
                possible_new_squares.append((self.x - 2, self.y + 1))
            # 2 left down
            if 0 <= self.y - 1 <= 7 and board[self.x - 2][self.y - 1].piece is None:
                possible_new_squares.append((self.x - 2, self.y - 1))

        return possible_new_squares

    def possible_captures(self, board):
        possible_captures = []

        if 7 >= self.x - 1 >= 0:
            # left 2 down
            if 7 >= self.y - 2 >= 0 and board[self.x - 1][self.y - 2].piece and \
                    board[self.x - 1][self.y - 2].piece.color != self.color:
                possible_captures.append((self.x - 1, self.y - 2))
            # left 2 up
            if 7 >= self.y + 2 >= 0 and board[self.x - 1][self.y + 2].piece and \
                    board[self.x - 1][self.y + 2].piece.color != self.color:
                possible_captures.append((self.x - 1, self.y + 2))

        if 0 <= self.x + 2 <= 7:
            # 2 right down
            if 0 <= self.y - 1 <= 7 and board[self.x + 2][self.y - 1].piece and \
                    board[self.x + 2][self.y - 1].piece.color != self.color:
                possible_captures.append((self.x + 2, self.y - 1))
            # 2 right up
            if 0 <= self.y + 1 <= 7 and board[self.x + 2][self.y + 1].piece and \
                    board[self.x + 2][self.y + 1].piece.color != self.color:
                possible_captures.append((self.x + 2, self.y + 1))

        if 7 >= self.x + 1 >= 0:
            # right 2 down
            if 7 >= self.y - 2 >= 0 and board[self.x + 1][self.y - 2].piece and \
                    board[self.x + 1][self.y - 2].piece.color != self.color:
                possible_captures.append((self.x + 1, self.y - 2))
            # right 2 up
            if 7 >= self.y + 2 >= 0 and board[self.x + 1][self.y + 2].piece and \
                    board[self.x + 1][self.y + 2].piece.color != self.color:
                possible_captures.append((self.x + 1, self.y + 2))

        if 0 <= self.x - 2 <= 7:
            # 2 left up
            if 0 <= self.y + 1 <= 7 and board[self.x - 2][self.y + 1].piece and \
                    board[self.x - 2][self.y + 1].piece.color != self.color:
                possible_captures.append((self.x - 2, self.y + 1))
            # 2 left down
            if 0 <= self.y - 1 <= 7 and board[self.x - 2][self.y - 1].piece and \
                    board[self.x - 2][self.y - 1].piece.color != self.color:
                possible_captures.append((self.x - 2, self.y - 1))

        return possible_captures
