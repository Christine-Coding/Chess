# Refresh the screen
def update_screen(board, game, settings):
    last_move = game.last_move
    for i in range(8):
        for j in range(8):
            board[i][j].display_tile(settings.tile_size, settings.white_tile_color, settings.black_tile_color)
            if (i, j) in last_move:
                board[i][j].display_last_move(settings.tile_size, settings.last_move_color)

            # TODO - delete
            # if (i, j) in game.under_fire:
            #     ts = settings.tile_size
            #     rect = shapes.Rectangle(board[i][j].x_coordinate, board[i][j].y_coordinate,
            #                             width=ts, height=ts, color=webcolors.name_to_rgb("red"))
            #     rect.opacity = 200
            #     rect.draw()

            if board[i][j].piece:
                board[i][j].display_piece(settings.tile_size, settings.dict_of_pictures)
            if board[i][j].marked:
                board[i][j].display_move_dots(settings.tile_size, settings.player_color)
            if board[i][j].promotions:
                board[i][j].display_promotion_options(settings.tile_size, settings.dict_of_pictures)
            if (i == 0 and settings.player_color) or (i == 7 and not settings.player_color):
                board[i][j].display_tile_number(settings.tile_size, settings.white_tile_color, settings.black_tile_color)
            if (j == 0 and settings.player_color) or (j == 7 and not settings.player_color):
                board[i][j].display_tile_letter(settings.tile_size, settings.white_tile_color, settings.black_tile_color)


# Select a piece via a mouse click
def click_square(board, x, y, tile_size):
    for i in range((board.shape[0])):
        for j in range((board.shape[1])):
            # checking if the position of the mouse is inside the selected square
            if board[i][j].x_coordinate <= x <= (board[i][j].x_coordinate + tile_size) \
                    and board[i][j].y_coordinate <= y <= (board[i][j].y_coordinate + tile_size):
                return board[i][j]
