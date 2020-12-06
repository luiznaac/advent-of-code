import functools


def open_file():
    with open('passwords-with-rules.txt') as passwords_file:
        passwords_with_rule = [password_line.rstrip() for password_line in passwords_file]

    return passwords_with_rule


def extract_info(password_with_rule):
    parts = password_with_rule.split(' ')
    [boundary_1, boundary_2] = [int(boundary) for boundary in parts[0].split('-')]
    letter = parts[1].replace(':', '')
    password = parts[2]

    return [boundary_1, boundary_2, letter, password]


def is_valid_times(password_with_rule):
    [minimum, maximum, letter, password] = extract_info(password_with_rule)

    times = functools.reduce(lambda times_appeared, current_letter: times_appeared+1 if current_letter == letter else times_appeared, password, 0)

    return minimum <= times <= maximum


# PART ONE #
valid_passwords = 0

for password_with_rule in open_file():
    if is_valid_times(password_with_rule):
        valid_passwords += 1

print(valid_passwords)


# PART TWO #
def is_valid_position(password_with_rule):
    [position_1, position_2, letter, password] = extract_info(password_with_rule)

    times = 0

    times = times+1 if password[position_1-1] == letter else times
    times = times+1 if password[position_2-1] == letter else times

    return times == 1


valid_passwords = 0

for password_with_rule in open_file():
    if is_valid_position(password_with_rule):
        valid_passwords += 1

print(valid_passwords)

