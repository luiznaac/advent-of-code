def open_file(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    return lines
