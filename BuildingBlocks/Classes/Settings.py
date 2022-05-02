from itertools import product

import pyglet


class Settings:
    def __init__(self, player_color: bool, show_tile_labels: bool, possible_moves_color: str, possible_captures_color: str,
                 possible_castling_color: str, possible_promotions_color: str, possible_en_passant_color: str,
                 last_move_color: str, tile_size: int, white_tile_color: str, black_tile_color: str):
        self.player_color = player_color  # True: white, False: black
        self.show_tile_labels = show_tile_labels

        # possible moves colors
        self.possible_moves_color = possible_moves_color
        self.possible_captures_color = possible_captures_color
        self.possible_castling_color = possible_castling_color
        self.possible_promotions_color = possible_promotions_color
        self.possible_en_passant_color = possible_en_passant_color
        self.last_move_color = last_move_color

        # window settings
        self.tile_size = tile_size
        self.width = 8 * tile_size
        self.height = 8 * tile_size

        # piece pictures and board colors
        self.dict_of_pictures = self.initialize_pictures()
        self.white_tile_color = white_tile_color
        self.black_tile_color = black_tile_color

    # Update the size of the screen
    def set_new_size(self, width, height):
        new_width_scale = width / self.width
        new_height_scale = height / self.height
        if new_width_scale < 1:
            if new_height_scale < 1:
                self.tile_size *= max(new_width_scale, new_height_scale)
            else:
                self.tile_size *= new_width_scale
        else:
            if new_height_scale < 1:
                self.tile_size *= new_height_scale
            else:
                self.tile_size *= min(new_width_scale, new_height_scale)
        self.width = self.tile_size * 8
        self.height = self.tile_size * 8

    # Load pictures of the pieces from a local folder
    @staticmethod
    def initialize_pictures():
        dictionary = {}
        pieces = ["Rook", "Knight", "Bishop", "King", "Queen", "Pawn"]
        colors = ["white", "black"]
        for piece, color in product(pieces, colors):
            picture = pyglet.image.load(''.join(['C:/Users/Christine/Documents/Programming/Chess/Pictures/', color, piece, '.png']))
            dictionary[''.join([color, piece])] = picture
        return dictionary
