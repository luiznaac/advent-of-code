import utils.utils as utils
import functools


adapters = utils.open_file_integers('adapters.txt')

# PART ONE #
adapters.sort()

one_difference = 1 if adapters[0] == 1 else 0
three_difference = 1 if adapters[0] == 3 else 0
three_difference += 1

for i in range(1, len(adapters)):
    if adapters[i] - adapters[i - 1] == 1:
        one_difference += 1
        continue

    if adapters[i] - adapters[i - 1] == 3:
        three_difference += 1

print(one_difference * three_difference)


# PART TWO #

# The first thought on solving this challenge was building a tree and validate every possible combination. It works for
# small sets, but with 110 numbers the number of combinations is human incomprehensible (110!). This would take
# centuries to calculate, so a new approach must be taken.

# The solution I found was to check which numbers couldn't in any case be removed from the list, that is, which ones
# already have a difference of three between them. With that, I can chunk the list into smaller lists of numbers that
# can be removed and apply a simple arrange calculation to find out how many different ways I can arrange them. Some
# rules must also be followed to make this calculation:
#
# - a set of just one number can have 2 arrangements (remove or not remove the number)
# - a set of two numbers can have 4 arrangements (remove just one of them (2 times), remove all or remove none = 4)
# - the trick is when there are three numbers or more in the set. I can't just remove them all, thus this would break
#   the difference of three rule. So the correct calculation arrangement for that is 2^set_size-(set_size-2)

adapters.insert(0, 0)
adapters.append(adapters[len(adapters) - 1] + 3)
not_available = []

for i in range(1, len(adapters)):
    if adapters[i] - adapters[i - 1] == 3:
        not_available.append(adapters[i])
        not_available.append(adapters[i - 1])

not_available = list(dict.fromkeys(not_available))
not_available.sort()
adapters.pop(0)
available_adapters = list(set(adapters) - set(not_available))
available_adapters.sort()

last_check = available_adapters[0]
size = 1
sizes = []

for available_adapter in available_adapters[1::]:
    if available_adapter - last_check == 1:
        last_check = available_adapter
        size += 1
        continue

    sizes.append(size)
    size = 1
    last_check = available_adapter

sizes.append(size)


def calculate_combinations(size):
    if size == 1:
        return 2
    if size == 2:
        return 4
    if size >= 3:
        return pow(2, size) - (size - 2)


combinations = list(map(calculate_combinations, sizes))
print(functools.reduce(lambda a, b: a*b, combinations))


# THE TREE THING THAT WOULD TAGE AGES #

# def check_requisites_and_iterate(adapters):
#     if adapters in arrangements:
#         return
#
#     arrangements.append(adapters)
#
#     for i in range(1, len(adapters) - 2):
#         if adapters[i + 1] - adapters[i - 1] > 3:
#             continue
#         new_adapters = list(adapters).copy()
#         new_adapters.pop(i)
#         check_requisites_and_iterate(new_adapters)
#
#
# arrangements = []
#
# adapters.insert(0, 0)
# adapters.append(adapters[len(adapters) - 1] + 3)
#
# start_time = time.time()
# check_requisites_and_iterate(adapters)
# end_time = time.time()
#
# print(len(arrangements))
# print(end_time - start_time)
