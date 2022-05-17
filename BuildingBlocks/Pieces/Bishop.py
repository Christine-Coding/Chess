class Bishop:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color
        self.name = "Bishop"
        self.abbreviation = "B"

    def __str__(self) -> str:
        return ''.join([self.color, ' ', self.name])

    def possible_moves(self, board):
        # movement to the left diagonally down
        possible_new_squares = []
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

        return possible_captures
