from BuildingBlocks.Classes.Settings import Settings
from BuildingBlocks.Initialize import initialize_board, initialize_pieces
from BuildingBlocks.OpeningsLearners.StringToMatrix import lines_to_matrices, add_matrix


def get_first_board_state():
    settings = Settings(player_color=False, show_tile_labels=False,
                        possible_moves_color="grey", possible_captures_color="red", possible_castling_color="black",
                        possible_promotions_color="green", possible_en_passant_color="gray", last_move_color="yellow",
                        tile_size=75, white_tile_color="white", black_tile_color="Sienna")
    board = initialize_board(settings)
    initialize_pieces(board, "white")
    initialize_pieces(board, "black")
    matrix = add_matrix(board)
    return matrix


# Enumerate all of the occurring states
def get_board_state_dictionary():
    openings = [item for sublist in lines_to_matrices() for item in sublist[1]]
    board_states_enumerated = [(0, get_first_board_state())]
    counter = 1
    for i in range(len(openings)):
        found = False
        for element in board_states_enumerated:
            if (openings[i] == element[1]).all():
                found = True
                break
        if not found:
            board_states_enumerated.append((counter, openings[i]))
            counter += 1
    return board_states_enumerated
