import copy

with open('input', 'r') as f:
    lines = f.readlines()

instructions = list(map(lambda line: line.split(), lines))


def run_without_repeat(instructions):
    executed = {}
    accumulator = 0
    pointer = 0
    while pointer < len(instructions):

        if str(pointer) in executed:
            return accumulator
            break

        instruction = instructions[pointer]
        operation = instruction[0]
        argument = instruction[1]

        executed[str(pointer)] = True

        if operation == 'acc':
            accumulator += int(argument)
            pointer += 1
        elif operation == 'nop':
            pointer += 1
        elif operation == 'jmp':
            pointer += int(argument)


def run(instructions):
    LIMIT = 10000
    executed = 0
    accumulator = 0
    pointer = 0

    while pointer < len(instructions):
        if executed > LIMIT :
            raise Exception('Max execution limit reached')
            break

        instruction = instructions[pointer]
        operation = instruction[0]
        argument = instruction[1]

        executed += 1

        if operation == 'acc':
            accumulator += int(argument)
            pointer += 1
        elif operation == 'nop':
            pointer += 1
        elif operation == 'jmp':
            pointer += int(argument)

    return accumulator




def try_change(original_instructions, pointer):
    instructions = copy.deepcopy(original_instructions)
    for i in range(pointer, len(instructions)):
        instruction = instructions[i]
        operation = instruction[0]
        if operation == 'nop':
            instructions[i][0] = 'jmp'
            return {
                'instructions': instructions,
                'pointer': i + 1
            }
        elif operation == 'jmp':
            instructions[i][0] = 'nop'
            return {
                'instructions': instructions,
                'pointer': i + 1
            }
    raise Exception('Nothing to change')


print(run_without_repeat(instructions))


pointer = 0
current_instructions = copy.deepcopy(instructions)
while True:
    try:
        acc = run(current_instructions)
        print(acc)
        break
    except Exception as e:
        result = try_change(instructions, pointer)
        current_instructions = result['instructions']
        pointer = result['pointer']



