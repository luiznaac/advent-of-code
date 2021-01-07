def open_file(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    return lines


def open_file_integers(filename):
    lines = open_file(filename)

    return list(map(lambda num: int(num), lines))


def open_file_array_of_chars(filename):
    lines = open_file(filename)

    return list(map(lambda chars: [*chars], lines))
