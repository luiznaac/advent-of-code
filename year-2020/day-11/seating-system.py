import utils.utils as utils
import functools
from copy import deepcopy


# PART ONE #
def process_seat(i, j):
    seat = seats[i][j]
    new_seat = seat

    if seat == 'L':
        new_seat = process_empty_seat(i, j)

    if seat == '#':
        new_seat = process_occupied_seat(i, j)

    return new_seat


def process_empty_seat(seat_i, seat_j):
    occupied_adjacent_seats = get_occupied_adjacent_seats(seat_i, seat_j)

    if occupied_adjacent_seats == 0:
        return '#'

    return seats[seat_i][seat_j]


def process_occupied_seat(seat_i, seat_j):
    occupied_adjacent_seats = get_occupied_adjacent_seats(seat_i, seat_j)

    if occupied_adjacent_seats >= 4:
        return 'L'

    return seats[seat_i][seat_j]


def get_occupied_adjacent_seats(seat_i, seat_j):
    adjacent_i_min = seat_i if seat_i == 0 else seat_i - 1
    adjacent_i_max = seat_i + 1 if seat_i == len(seats) - 1 else seat_i + 2
    adjacent_j_min = seat_j if seat_j == 0 else seat_j - 1
    adjacent_j_max = seat_j + 1 if seat_j == len(seats[0]) - 1 else seat_j + 2

    occupied_adjacent_seats = functools.reduce(
        lambda occupied_seats, rows: occupied_seats + functools.reduce(
            lambda occupied_seats_in_row, seat: occupied_seats_in_row + (1 if seat == '#' else 0)
            , rows[adjacent_j_min:adjacent_j_max:], 0)
        , seats[adjacent_i_min:adjacent_i_max:], 0)

    occupied_adjacent_seats -= 1 if seats[seat_i][seat_j] == '#' else 0

    return occupied_adjacent_seats


def print_seats(seats_to_print):
    print()
    for seat_row in seats_to_print:
        for seat in seat_row:
            print(seat, end='')
        print()


def count_final_occupied_seats(seats):
    return functools.reduce(
            lambda occupied_seats, seat: occupied_seats + (1 if seat == '#' else 0)
        , [seat for seat_row in seats for seat in seat_row], 0)


# PART TWO #
def process_seat_in_directions(i, j):
    seat = seats[i][j]
    new_seat = seat

    if seat == 'L':
        new_seat = process_empty_seat_in_direction(i, j)

    if seat == '#':
        new_seat = process_occupied_seat_in_direction(i, j)

    return new_seat


def process_empty_seat_in_direction(seat_i, seat_j):
    occupied_adjacent_seats = get_occupied_adjacent_seats_in_directions(seat_i, seat_j)

    if occupied_adjacent_seats == 0:
        return '#'

    return seats[seat_i][seat_j]


def process_occupied_seat_in_direction(seat_i, seat_j):
    occupied_adjacent_seats = get_occupied_adjacent_seats_in_directions(seat_i, seat_j)

    if occupied_adjacent_seats >= 5:
        return 'L'

    return seats[seat_i][seat_j]


def get_occupied_adjacent_seats_in_directions(seat_i, seat_j):
    directions = [
        [-1, -1],  # UP LEFT
        [-1, 0],   # UP
        [-1, 1],   # UP RIGHT
        [0, 1],    # RIGHT
        [1, 1],    # DOWN RIGHT
        [1, 0],    # DOWN
        [1, -1],   # DOWN LEFT
        [0, -1],   # LEFT
    ]

    occupied_adjacent_seats = functools.reduce(
        lambda occupied_adjacent_seats, direction: occupied_adjacent_seats + (1 if first_seat_in_direction(seat_i, seat_j, direction) == '#' else 0)
        , directions, 0)

    return occupied_adjacent_seats


def first_seat_in_direction(i, j, direction):
    sum_i = direction[0]
    sum_j = direction[1]
    i += sum_i
    j += sum_j

    while not boundary_reached(i, j):
        if seats[i][j] != '.':
            return seats[i][j]

        i += sum_i
        j += sum_j

    return 'L'


def boundary_reached(i, j):
    max_i = len(seats)
    max_j = len(seats[0])

    return i < 0 or j < 0 or i == max_i or j == max_j


seats = utils.open_file_array_of_chars('seats.txt')
new_seats = deepcopy(seats)

changed = True

while changed:
    for i in range(0, len(seats)):
        for j in range(0, len(seats[0])):
            new_seats[i][j] = process_seat_in_directions(i, j)

    if seats == new_seats:
        changed = False

    seats = deepcopy(new_seats)

print(count_final_occupied_seats(seats))
