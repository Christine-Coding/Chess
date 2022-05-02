import re


def read_lines(location):
    names, moves = [], []

    with open(location, "r", encoding="utf-8") as f:
        for line in f:
            # Get the name of the line
            if re.match(r"^(?!\n|1.).*$", line):
                names.append([line.strip()])
            # Get white's moves and black's moves (clean the input)
            if re.match(r"^(1.).*$", line):
                lst = [re.sub("\d+[.]|[,]", "", move) for move in line.strip().split(" ")]
                # white_moves.append(lst[0:][::2])
                # black_moves.append((lst[1:][::2]))
                moves.append(lst)

    return zip(names, moves)
