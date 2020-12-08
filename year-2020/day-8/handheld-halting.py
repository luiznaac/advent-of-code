import utils.utils as utils


instructions = utils.open_file('instructions.txt')


# PART ONE #
def execute_instructions(instructions):
    accumulator = 0
    already_executed = []
    i = 0

    while i < len(instructions):
        instruction = instructions[i].split(' ')

        if i in already_executed:
            return ['err', accumulator]

        already_executed.append(i)

        if instruction[0] == 'jmp':
            i += int(instruction[1])
            continue

        if instruction[0] == 'acc':
            accumulator += int(instruction[1])

        i += 1

    return ['ok', accumulator]


print(execute_instructions(instructions)[1])


# PAR TWO #
def replace_nth_jmp_or_nop(instructions, n):
    count = 0

    for i in range(len(instructions)):
        instruction = instructions[i].split(' ')
        count = count + 1 if instruction[0] == 'jmp' or instruction[0] == 'nop' else count

        if count == n:
            instruction[0] = 'nop' if instruction[0] == 'jmp' else 'jmp'
            instructions[i] = ' '.join(instruction)
            return instructions


n = 1
result = ['err']

while result[0] == 'err':
    new_instructions = replace_nth_jmp_or_nop(instructions.copy(), n)
    result = execute_instructions(new_instructions)
    n += 1

print(result[1])
