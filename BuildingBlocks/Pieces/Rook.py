class Rook:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color
        self.name = "Rook"
        self.abbreviation = "R"
        self.has_not_moved = True

    def __str__(self) -> str:
        return ''.join([self.color, ' ', self.name])

    def possible_moves(self, board):
        possible_new_squares = []
        # example: 3, 4 - (3 -> 0/2, 4, 3 -> 4/7, 4 // 3, 4 -> 0/3, 4 -> 5/7)
        # movement to the left
        if self.x != 0:
            for i in range(self.x - 1, -1, -1):
                if board[i][self.y].piece is not None:
                    break
                possible_new_squares.append((i, self.y))
        # movement to the right
        if self.x != 7:
            for i in range(self.x + 1, 8):
                if board[i][self.y].piece is not None:
                    break
                possible_new_squares.append((i, self.y))
        # movement downwards
        if self.y != 0:
            for j in range(self.y - 1, -1, -1):
                if board[self.x][j].piece is not None:
                    break
                possible_new_squares.append((self.x, j))
        # movement upwards
        if self.y != 7:
            for j in range(self.y + 1, 8):
                if board[self.x][j].piece is not None:
                    break
                possible_new_squares.append((self.x, j))

        return possible_new_squares

    def possible_captures(self, board):
        possible_captures = []

        # movement to the left
        if self.x != 0:
            for i in range(self.x - 1, -1, -1):
                if board[i][self.y].piece is not None:
                    if board[i][self.y].piece.color != self.color:
                        possible_captures.append((i, self.y))
                    break
        # movement to the right
        if self.x != 7:
            for i in range(self.x + 1, 8):
                if board[i][self.y].piece is not None:
                    if board[i][self.y].piece.color != self.color:
                        possible_captures.append((i, self.y))
                    break
        # movement downwards
        if self.y != 0:
            for j in range(self.y - 1, -1, -1):
                if board[self.x][j].piece is not None:
                    if board[self.x][j].piece.color != self.color:
                        possible_captures.append((self.x, j))
                    break
        # movement upwards
        if self.y != 7:
            for j in range(self.y + 1, 8):
                if board[self.x][j].piece is not None:
                    if board[self.x][j].piece.color != self.color:
                        possible_captures.append((self.x, j))
                    break

        return possible_captures
