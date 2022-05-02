import string

import pyglet
import webcolors

from pyglet import shapes

from BuildingBlocks.Classes.Settings import Settings


class Square:
    def __init__(self, x: int, y: int, tile_color: str, settings: Settings):
        self.x = x  # index
        self.y = y  # index

        self.x_coordinate = x * settings.tile_size if settings.player_color else (7 - x) * settings.tile_size
        self.y_coordinate = y * settings.tile_size if settings.player_color else (7 - y) * settings.tile_size

        self.letter = str(list(string.ascii_lowercase)[x])  # A-H tile letter
        self.number = str(y + 1)  # 1-8 tile number

        self.tile_color = tile_color

        self.piece = None  # None or piece
        self.marked = None  # None or color
        self.promotions = None  # None or color
        self.last_move = None   # None or color

    def __str__(self) -> str:
        if self.piece is not None:
            return ''.join([self.letter, self.number, ', ', self.tile_color, ' tile with ', self.piece.color, ' ',
                            self.piece.name])
        else:
            return ''.join([self.letter, self.number, ', ', self.tile_color, ' tile, empty'])

    # Update the tile size while resizing the screen
    def set_new_tile_size(self, tile_size, player_color):
        self.x_coordinate = self.x * tile_size if player_color else (7 - self.x) * tile_size
        self.y_coordinate = self.y * tile_size if player_color else (7 - self.y) * tile_size

    # Display or refresh the tile
    def display_tile(self, tile_size, white_tile_color, black_tile_color):
        if self.tile_color == "white":  # if the player is playing with white
            rect = shapes.Rectangle(self.x_coordinate, self.y_coordinate, width=tile_size,
                                    height=tile_size, color=webcolors.name_to_rgb(white_tile_color))
        else:
            rect = shapes.Rectangle(self.x_coordinate, self.y_coordinate, width=tile_size,
                                    height=tile_size, color=webcolors.name_to_rgb(black_tile_color))
        rect.draw()

    # Highlight the start and end square of the last move
    def display_last_move(self, tile_size, last_move_color):
        rect = shapes.Rectangle(self.x_coordinate, self.y_coordinate, width=tile_size,
                                height=tile_size, color=webcolors.name_to_rgb(last_move_color))
        rect.opacity = 100 if self.tile_color == "white" else 150
        rect.draw()

    # Display or refresh the pieces
    def display_piece(self, tile_size, dict_of_pictures):
        picture = dict_of_pictures[''.join([self.piece.color, self.piece.name])]  # get the loaded picture
        picture = pyglet.sprite.Sprite(img=picture, x=self.x_coordinate, y=self.y_coordinate)  # make it into Sprite
        picture.update(scale_x=tile_size / picture.width,
                       scale_y=tile_size / picture.height)  # scale to tile size
        picture.draw()

    # Display possible moves and captures via circles
    def display_move_dots(self, tile_size, player_color):
        tile_size = tile_size  # optimization
        if player_color:  # if the player is playing with white
            circle = shapes.Circle(x=tile_size * self.x + tile_size / 2,
                                   y=tile_size * self.y + tile_size / 2,
                                   radius=tile_size / 12, color=webcolors.name_to_rgb(self.marked))
            circle.draw()
        else:
            circle = shapes.Circle(x=tile_size * (7 - self.x) + tile_size / 2,
                                   y=tile_size * (7 - self.y) + tile_size / 2,
                                   radius=tile_size / 12, color=webcolors.name_to_rgb(self.marked))
            circle.draw()
        # unmark
        self.marked = None

    # Display the possible promotion options via pictures
    def display_promotion_options(self, tile_size, dict_of_pictures):
        options = ["Knight", "Rook", "Bishop", "Queen"]
        positions = [(0, 0), (0, 0.5 * tile_size), (0.5 * tile_size, 0),
                     (0.5 * tile_size, 0.5 * tile_size)]
        for piece, pos in zip(options, positions):
            picture = dict_of_pictures[''.join([self.promotions, piece])]  # get the loaded picture
            picture = pyglet.sprite.Sprite(img=picture, x=self.x_coordinate + pos[0],
                                           y=self.y_coordinate + pos[1])  # make it into Sprite
            picture.update(scale_x=(tile_size * 0.5 / picture.width),
                           scale_y=tile_size * 0.5 / picture.height)  # scale to tile size
            picture.draw()

    # Display the tile letter
    def display_tile_letter(self, tile_size, white_tile_color, black_tile_color):
        color = webcolors.name_to_rgb(black_tile_color) + (255,) if self.tile_color == "white" \
            else webcolors.name_to_rgb(white_tile_color) + (255,)
        label = pyglet.text.Label(self.letter, font_size=tile_size / 8,
                                  x=self.x_coordinate + tile_size * 0.88,
                                  y=self.y_coordinate + tile_size * 0.05,
                                  color=color)
        label.draw()

    # Display the tile number
    def display_tile_number(self, tile_size, white_tile_color, black_tile_color):
        color = webcolors.name_to_rgb(black_tile_color) + (255,) if self.tile_color == "white" \
            else webcolors.name_to_rgb(white_tile_color) + (255,)
        label = pyglet.text.Label(self.number, font_size=tile_size / 8,
                                  x=self.x_coordinate + tile_size * 0.05,
                                  y=self.y_coordinate + tile_size * 0.8,
                                  color=color)
        label.draw()
