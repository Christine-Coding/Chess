class Queen:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color
        self.name = "Queen"
        self.abbreviation = "Q"

    def __str__(self) -> str:
        return ''.join([self.color, ' ', self.name])

    def possible_moves(self, board):
        possible_new_squares = []

        # movement to the left diagonally down
        temp_1 = self.x - 1
        temp_2 = self.y - 1
        while not (temp_1 < 0 or temp_2 < 0) and board[temp_1][temp_2].piece is None:
            possible_new_squares.append((temp_1, temp_2))
            temp_1 -= 1
            temp_2 -= 1

        # movement to the right diagonally down
        temp_3 = self.x + 1
        temp_4 = self.y - 1
        while not (temp_3 > 7 or temp_4 < 0) and board[temp_3][temp_4].piece is None:
            possible_new_squares.append((temp_3, temp_4))
            temp_3 += 1
            temp_4 -= 1

        # movement to the right diagonally up
        temp_5 = self.x + 1
        temp_6 = self.y + 1
        while not (temp_5 > 7 or temp_6 > 7) and board[temp_5][temp_6].piece is None:
            possible_new_squares.append((temp_5, temp_6))
            temp_5 += 1
            temp_6 += 1

        # movement to the left diagonally up
        temp_7 = self.x - 1
        temp_8 = self.y + 1
        while not (temp_7 < 0 or temp_8 > 7) and board[temp_7][temp_8].piece is None:
            possible_new_squares.append((temp_7, temp_8))
            temp_7 -= 1
            temp_8 += 1

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

        # movement to the left diagonally down
        temp_1 = self.x - 1
        temp_2 = self.y - 1
        while not (temp_1 < 0 or temp_2 < 0):
            if board[temp_1][temp_2].piece and board[temp_1][temp_2].piece.color == self.color:
                break
            if board[temp_1][temp_2].piece and board[temp_1][temp_2].piece.color != self.color:
                possible_captures.append((temp_1, temp_2))
                break
            temp_1 -= 1
            temp_2 -= 1

        # movement to the right diagonally down
        temp_3 = self.x + 1
        temp_4 = self.y - 1
        while not (temp_3 > 7 or temp_4 < 0):
            if board[temp_3][temp_4].piece and board[temp_3][temp_4].piece.color == self.color:
                break
            if board[temp_3][temp_4].piece and board[temp_3][temp_4].piece.color != self.color:
                possible_captures.append((temp_3, temp_4))
                break
            temp_3 += 1
            temp_4 -= 1

        # movement to the right diagonally up
        temp_5 = self.x + 1
        temp_6 = self.y + 1
        while not (temp_5 > 7 or temp_6 > 7):
            if board[temp_5][temp_6].piece and board[temp_5][temp_6].piece.color == self.color:
                break
            if board[temp_5][temp_6].piece and board[temp_5][temp_6].piece.color != self.color:
                possible_captures.append((temp_5, temp_6))
                break
            temp_5 += 1
            temp_6 += 1

        # movement to the left diagonally up
        temp_7 = self.x - 1
        temp_8 = self.y + 1
        while not (temp_7 < 0 or temp_8 > 7):
            if board[temp_7][temp_8].piece and board[temp_7][temp_8].piece.color == self.color:
                break
            if board[temp_7][temp_8].piece and board[temp_7][temp_8].piece.color != self.color:
                possible_captures.append((temp_7, temp_8))
                break
            temp_7 -= 1
            temp_8 += 1

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
