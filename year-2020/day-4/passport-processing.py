import re

def open_file():
    with open('passports.txt') as passport_file:
        unparsed_passports = [passport_line.rstrip() for passport_line in passport_file]

    return unparsed_passports


def byr(value):
    return len(value) == 4 and 1920 <= int(value) <= 2002


def iyr(value):
    return len(value) == 4 and 2010 <= int(value) <= 2020


def eyr(value):
    return len(value) == 4 and 2020 <= int(value) <= 2030


def hgt(value):
    if len(value.split('cm')) == 2:
        return 150 <= int(value.split('cm')[0]) <= 193

    if len(value.split('in')) == 2:
        return 59 <= int(value.split('in')[0]) <= 76

    return False


def hcl(value):
    if len(value.split('#')) == 2:
        return re.match('^[a-f0-9]{6}$', value.split('#')[1])

    return False


def ecl(value):
    valid_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    return not {value} - set(valid_values)


def pid(value):
    return re.match('^[0-9]{9}$', value)


def validate_values(passport):
    passport_fields = passport[0]
    passport_values = passport[1]

    for index, field in enumerate(passport_fields):
        if field == 'byr':
            if not byr(passport_values[index]): return False
        if field == 'iyr':
            if not iyr(passport_values[index]): return False
        if field == 'eyr':
            if not eyr(passport_values[index]): return False
        if field == 'hgt':
            if not hgt(passport_values[index]): return False
        if field == 'hcl':
            if not hcl(passport_values[index]): return False
        if field == 'ecl':
            if not ecl(passport_values[index]): return False
        if field == 'pid':
            if not pid(passport_values[index]): return False

    return True


def is_valid_passport(passport):
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    if set(mandatory_fields) - set(passport[0]):
        return False

    return validate_values(passport)


unparsed_passports = open_file()

passports = []
passport_fields = []
passport_values = []

for unparsed_passport_line in unparsed_passports:
    if not unparsed_passport_line:
        passports.append([passport_fields, passport_values])
        passport_fields = []
        passport_values = []
        continue

    passport_fields += [field.split(':')[0] for field in unparsed_passport_line.split(' ')]
    passport_values += [field.split(':')[1] for field in unparsed_passport_line.split(' ')]

passports.append([passport_fields, passport_values])

print(passports)

valid_passports = 0

for passport in passports:
    valid_passports = valid_passports + 1 if is_valid_passport(passport) else valid_passports

print(valid_passports)
