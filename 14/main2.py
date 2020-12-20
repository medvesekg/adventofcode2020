from itertools import product

def parse_instructions(lines):
    instructions = []
    for line in lines:
        instruction = {}
        tokens = line.split()
        if tokens[0] == 'mask':
            instruction['type'] = 'mask'
            instruction['value'] = tokens[-1]
        else:
            address = tokens[0].split('[')[1].split(']')[0]
            instruction['type'] = 'mem'
            instruction['address'] = int(address)
            instruction['value'] = int(tokens[-1])
        instructions.append(instruction)

    return instructions


def apply_mask(mask_string, number):

    binary = list(bin(number)[2:].rjust(36, '0'))

    x_indices = []
    for (i, char) in enumerate(mask_string):
        if char == '1':
            binary[i] = '1'
        if char == 'X':
            x_indices.append(i)

    numbers = []
    if not len(x_indices):
        numbers.append(binary)

    combinations = [[0,1] for index in x_indices]
    combinations = product(*combinations)

    for combination in combinations:
        new_binary = binary.copy()
        for (i,value) in enumerate(combination):
            new_binary[x_indices[i]] = str(value)
        numbers.append(new_binary)

    return list(map(lambda x: int(x, 2), map(lambda x: "".join(x), numbers)))


def run(instructions, memory):
    current_mask = None
    for instruction in instructions:
        if instruction['type'] == 'mask':
            current_mask = instruction['value']
        else:
            addresses = apply_mask(current_mask, int(instruction['address']))
            for address in addresses:
                memory[address] = instruction['value']


with open('input', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

instructions = parse_instructions(lines)

memory = {}

run(instructions, memory)

print(sum(memory.values()))
