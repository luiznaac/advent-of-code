import utils.utils as utils


# PART ONE #
def process_instruction(instructions, orientation, north, east):
    if not instructions:
        return [north, east]

    instruction_pair = instructions.pop(0)
    instruction = instruction_pair[0]
    value = int(instruction_pair[1:len(instruction_pair):])

    if instruction == 'N' or (instruction == 'F' and orientation == 0):
        north += value
    if instruction == 'E' or (instruction == 'F' and orientation == 1):
        east += value
    if instruction == 'S' or (instruction == 'F' and orientation == 2):
        north -= value
    if instruction == 'W' or (instruction == 'F' and orientation == 3):
        east -= value
    if instruction == 'R':
        orientation = int(((orientation * 90 + value) % 360) / 90)
    if instruction == 'L':
        orientation = int(((orientation * 90 - value) % 360) / 90)

    return process_instruction(instructions, orientation, north, east)


# PART TWO #
def process_instruction_with_waypoint(instructions, north, east, waypoint_north, waypoint_east):
    if not instructions:
        return [north, east]

    instruction_pair = instructions.pop(0)
    instruction = instruction_pair[0]
    value = int(instruction_pair[1:len(instruction_pair):])

    if instruction == 'N':
        waypoint_north += value
    if instruction == 'E':
        waypoint_east += value
    if instruction == 'S':
        waypoint_north -= value
    if instruction == 'W':
        waypoint_east -= value
    if instruction == 'F':
        north += waypoint_north * value
        east += waypoint_east * value
    if instruction == 'R':
        rotations = 4 - (value % 360) / 90
        [waypoint_north, waypoint_east] = resolve_waypoint_rotation(rotations, waypoint_north, waypoint_east)
    if instruction == 'L':
        rotations = (value % 360) / 90
        [waypoint_north, waypoint_east] = resolve_waypoint_rotation(rotations, waypoint_north, waypoint_east)

    return process_instruction_with_waypoint(instructions, north, east, waypoint_north, waypoint_east)


def resolve_waypoint_rotation(rotations, waypoint_north, waypoint_east):
    rotations_made = 0
    while rotations_made < rotations:
        waypoint_east_aux = waypoint_east
        waypoint_east = -waypoint_north
        waypoint_north = waypoint_east_aux
        rotations_made += 1

    return [waypoint_north, waypoint_east]


instructions = utils.open_file('instructions.txt')

[north, east] = process_instruction_with_waypoint(instructions, 0, 0, 1, 10)

print('north ', north)
print('east ', east)

print(abs(north) + abs(east))
