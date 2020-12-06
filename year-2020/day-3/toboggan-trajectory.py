def open_file():
    with open('map.txt') as map_file:
        partial_map = [map_line.rstrip() for map_line in map_file]

    return partial_map


def count_trees(right, down):
    position = 0
    number_of_trees = 0

    for map_line in partial_map[down::down]:
        position = (position + right) % len(map_line)
        number_of_trees = number_of_trees + 1 if map_line[position] == '#' else number_of_trees

    return number_of_trees


# PART ONE #
partial_map = open_file()

print(count_trees(3, 1))


# PART TWO #
answer = count_trees(1, 1)
answer *= count_trees(3, 1)
answer *= count_trees(5, 1)
answer *= count_trees(7, 1)
answer *= count_trees(1, 2)

print(answer)
