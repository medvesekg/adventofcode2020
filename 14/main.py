with open('input', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


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


def construct_mask(mask_string):
    or_mask = int(mask_string.replace('X', '0'), 2)
    and_mask = int(mask_string.replace('X', '1'), 2)
    return or_mask, and_mask

def apply_mask(mask, item):
    return (item | mask[0]) & mask[1]

def run(instructions, memory):
    current_mask = None
    for instruction in instructions:
        if instruction['type'] == 'mask':
            current_mask = construct_mask(instruction['value'])
        else:
            memory[instruction['address']] = apply_mask(current_mask, instruction['value']) if current_mask else instruction['value']



instructions = parse_instructions(lines)

memory = {}

run(instructions, memory)

print(sum(memory.values()))

