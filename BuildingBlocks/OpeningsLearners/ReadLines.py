import re


def read_lines(location):
    names, moves = [], []

    with open(location, "r", encoding="utf-8") as f:
        for line in f:
            # Get the name of the line
            if re.match(r"^(?!\n|1.).*$", line):
                names.append([line.strip().strip("/")])
            # Get white's moves and black's moves (clean the input)
            if re.match(r"^(1.).*$", line):
                lst = [re.sub("\d+[.]|[,]", "", move.strip()) for move in line.split(" ")]
                lst = list(filter(None, lst))
                # white_moves.append(lst[0:][::2])
                # black_moves.append((lst[1:][::2]))
                moves.append(lst)

    return zip(names, moves)


def pgn_to_txt(old_location, new_location):
    with open(old_location, "r", encoding="utf-8") as old_file, open(new_location, 'r+', encoding="utf-8") as new_file:
        for line in old_file:
            if "[Site" not in line.strip():
                if "[White" in line.strip():
                    new_file.write(re.search('"([^"]*)"', line)[1].strip()+"/")
                elif "[Black" in line.strip():
                    new_file.write(re.search('"([^"]*)"', line)[1])
                elif line != "\n":
                    new_file.write(line.strip())
                else:
                    new_file.write(line)





pgn_to_txt("Lines\\all_lines.txt", "Lines\\clean_lines.txt")
lines = read_lines(r"C:\Users\Christine\Documents\Programming\Chess\BuildingBlocks\OpeningsLearners\Lines\clean_lines.txt")
for e1, e2 in lines:
    print(e1)

