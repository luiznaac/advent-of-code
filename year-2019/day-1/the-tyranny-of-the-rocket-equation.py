import utils.utils as utils


def calculate_required_fuel(mass):
    return (mass // 3) - 2


spacecraft_modules = utils.open_file('spacecraft-modules.txt')

# PART ONE #
total_fuel = 0

for module_mass in spacecraft_modules:
    total_fuel += calculate_required_fuel(int(module_mass))

print(total_fuel)


# PART TWO #
def calculate_required_fuel_for_fuel(fuel_mass):
    required_fuel = calculate_required_fuel(fuel_mass)

    if required_fuel < 0:
        return 0

    return required_fuel + calculate_required_fuel_for_fuel(required_fuel)


total_fuel = 0

for module_mass in spacecraft_modules:
    fuel_for_module = calculate_required_fuel(int(module_mass))
    total_fuel += (calculate_required_fuel_for_fuel(fuel_for_module) + fuel_for_module)

print(total_fuel)
