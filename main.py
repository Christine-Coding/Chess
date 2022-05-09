from copy import deepcopy

import numpy as np
import pyglet

from BuildingBlocks.CheckOrMate import check_if_check
from BuildingBlocks.Classes.Game import Game
from BuildingBlocks.Initialize import initialize_board, initialize_pieces
from BuildingBlocks.OpeningsLearners.Helpers import add_matrix
from BuildingBlocks.OpeningsLearners.StringToLattice import lines_to_matrices
from BuildingBlocks.Screen import update_screen, click_square
from BuildingBlocks.Classes.Settings import Settings
from BuildingBlocks.MoveLogic import drag_piece, click_piece


# General settings
settings = Settings(player_color=True, show_tile_labels=False,
                    possible_moves_color="grey", possible_captures_color="red", possible_castling_color="black",
                    possible_promotions_color="green", possible_en_passant_color="gray", last_move_color="yellow",
                    tile_size=75, white_tile_color="white", black_tile_color="Sienna")

# Define Pyglet window
game_window = pyglet.window.Window(width=settings.width, height=settings.height, caption="Chess", resizable=True)
game_window.set_minimum_size(480, 480)

# Initialization of the board
board = initialize_board(settings)
initialize_pieces(board, "white")
initialize_pieces(board, "black")
start_pos_x, start_pos_y, stop_pos_x, stop_pos_y = 0, 0, 0, 0

# Initialize the game
game = Game(player_color=settings.player_color, opening=1)  # playing with white, learning one line
game.board_states[0] = deepcopy(board)
game.matrices[0] = add_matrix(board)
opening_lines = [item for sublist in lines_to_matrices() for item in sublist]


@game_window.event
def on_draw():
    game_window.clear()
    update_screen(board, game, settings)


@game_window.event
def on_mouse_press(x, y, button, modifiers):
    global start_pos_x, start_pos_y
    start_pos_x, start_pos_y = x, y


@game_window.event
def on_mouse_release(x, y, button, modifiers):
    global start_pos_x, start_pos_y, stop_pos_x, stop_pos_y, game
    print(game.white_moves, game.black_moves)
    this = 0
    for el in opening_lines:
        if (np.array_equal(game.matrices[game.move_number], el)):
            this += 1
            print("Jee!")
    stop_pos_x, stop_pos_y = x, y
    # right the button is clicked/dragged
    if button == 1:
        # dragged, not clicked
        if start_pos_x != stop_pos_x and start_pos_y != stop_pos_y:
            # check if valid movement
            start_piece = click_square(board, start_pos_x, start_pos_y, settings.tile_size)
            if start_piece:
                # check that the player clicked their own piece
                if game.whose_turn and start_piece.piece and start_piece.piece.color == "white" \
                        or not game.whose_turn and start_piece.piece and start_piece.piece.color == "black":
                    selected_square = click_square(board, stop_pos_x, stop_pos_y, settings.tile_size)  # False or Square
                    if selected_square:
                        drag_piece(game, board, settings, start_piece, selected_square, x, y)
        # clicked, not dragged
        else:
            selected_square = click_square(board, stop_pos_x, stop_pos_y, settings.tile_size)  # False or Square
            # check that the player clicked their own piece
            if game.move_piece and (game.whose_turn and game.move_piece.color == "white"
                                    or not game.whose_turn and game.move_piece.color == "black") \
                    or selected_square.piece and (game.whose_turn and selected_square.piece.color == "white"
                                                  or not game.whose_turn and selected_square.piece.color == "black"):
                # a piece or a square has been selected
                if selected_square:
                    click_piece(game, board, settings, selected_square, x, y)
    if game.whose_turn:     # white's turn
        game.fire_by_black_pieces = check_if_check(board, game)
    else:   # black's turn
        game.fire_by_white_pieces = check_if_check(board, game)

    # TODO - delete
    game.under_fire = check_if_check(board, game)


@game_window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    pass


@game_window.event
def on_resize(width, height):
    global settings
    settings.set_new_size(width, height)
    for i in range((board.shape[0])):
        for j in range((board.shape[1])):
            board[i][j].set_new_tile_size(settings.tile_size, settings.player_color)


if __name__ == '__main__':
    pyglet.app.run()
