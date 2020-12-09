import utils.utils as utils
import functools


numbers = utils.open_file_integers('output.txt')

length = 25


# PART ONE #
def get_first_not_matching_number(numbers):
    for n in range(length, len(numbers)):
        sums = []
        for i in range(n - length, n + length):
            for j in range(i + 1, n):
                if i != j:
                    sums.append(numbers[i] + numbers[j])

        if not numbers[n] in sums:
            return numbers[n]


number = get_first_not_matching_number(numbers)
print(number)


# PART TWO #
def get_sum_range(numbers, number):
    for range_size in range(2, len(numbers)):
        for i in range(0, len(numbers) - (range_size - 1)):
            sum = functools.reduce(lambda a,b: a+b, numbers[i:i + range_size:])
            if sum == number:
                return [i, i + range_size]


sum_range = get_sum_range(numbers, number)

smallest = functools.reduce(lambda a,b : a if a > b else b, numbers[sum_range[0]:sum_range[1]:])
greatest = functools.reduce(lambda a,b : a if a < b else b, numbers[sum_range[0]:sum_range[1]:])

print(smallest + greatest)
