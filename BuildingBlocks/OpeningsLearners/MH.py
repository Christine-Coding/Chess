def metropolis_hastings(input_parameters = [0, 0, 1, 1, 0]):
    for i in range(number_of_iterations):   # Number of opening lines sampled
        x[0] = first_board_state
        i = 1
        # Running through the database until we have reached the last board state
        # of the current opening line being sampled
        while True:
            current_x = x[i-1]
            for opening in openings_database:
                for board_state in opening:
                    # If the current state is in the openings database
                    # and it is not the last state in line, we select it
                    if current_x == board_state and board_state not last:
                        possible_moves.add(board_state)
            if possible_moves:
                proposed_x = possible_moves[randint(0, len(possible_moves))]
                A = probability_of_this_move / probability_of_the_last_move
                # Acceptance/rejection sampling
                # Add value where the input parameters are 1
                # and so is the corresponding parameter in the opening line
                added_value = [weights * input_parameters where True]
                A = A + sum(added_value)
                if random_value < A:
                    x[i] = proposed_x
                    i += 1
                else:
                    x[i] = current_x
            else:
                list_of_samples.add(x)
