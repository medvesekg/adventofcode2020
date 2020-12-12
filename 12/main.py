with open('input', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


instructions = [{'code': line[0], 'value': int(line[1:])} for line in lines]

instruction_map = {
    'N': {
        'attribute': 'Y',
        'value': lambda v: v
    },
    'E': {
        'attribute': 'X',
        'value': lambda v: v
    },
    'S': {
        'attribute': 'Y',
        'value': lambda v: -v
    },
    'W': {
        'attribute': 'X',
        'value': lambda v: -v
    },
    'R': {
        'attribute': 'facing',
        'value': lambda v: v
    },
    'L': {
        'attribute': 'facing',
        'value': lambda v: -v
    }
}

facing_map = {
    -270:  'S',
    -180:  'W',
    -90:   'N',
    0:     'E',
    90:    'S',
    180:   'W',
    270:   'N',
}


def run(start_state, instructions):
    ship = start_state
    for instruction in instructions:
        code = instruction['code']
        if code == 'F':
            code = facing_map[ship['facing'] % 360]

        value_function = instruction_map[code]['value']
        attribute = instruction_map[code]['attribute']
        ship[attribute] += value_function(instruction['value'])

    return ship


def manhattan(ship):
    return abs(ship['X']) + abs(ship['Y'])


# def run2(start_state, start_waypoint, instructions):
#     ship = start_state
#     waypoint = start_waypoint
#
#     for instruction in instructions:
#         code = instruction['code']
#         value = instruction['value']
#         if code == 'F':
#             ship['X'] += (waypoint['X'] * value)
#             ship['Y'] += (waypoint['Y'] * value)
#         else:
#             instruction_map['code']



end_state1 = run({ 'facing': 0, 'Y': 0, 'X': 0,}, instructions)

print(manhattan(end_state1))

# end_state2 = run2({ 'facing': 0, 'Y': 0, 'X': 0,}, {'Y': 1, 'X': 10,}, instructions)
#print(manhattan(end_state2))



