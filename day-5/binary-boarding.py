import utils.utils as utils


def get_number(chars, number_range, lower_half_id):
    if not chars:
        return number_range[0]

    char = chars.pop(0)
    middle = (number_range[0] + number_range[1]) // 2

    if char == lower_half_id:
        return get_number(chars, [number_range[0], middle], lower_half_id)

    return get_number(chars, [middle + 1, number_range[1]], lower_half_id)


# PART ONE #
boarding_passes = utils.open_file('boarding-passes.txt')

seat_ids = []

for boarding_pass in boarding_passes:
    row = get_number(list(boarding_pass[0:7:]), [0, 127], 'F')
    column = get_number(list(boarding_pass[7::]), [0, 7], 'L')
    seat_id = row * 8 + column
    seat_ids.append(seat_id)

seat_ids.sort()
print(seat_ids[len(seat_ids) - 1])

# PART TWO #
for i in range(1, len(seat_ids)):
    id_minus_1 = seat_ids[i - 1]
    id_plus_1 = seat_ids[i]

    if id_minus_1 + 1 == id_plus_1 - 1:
        print(id_minus_1 + 1)
