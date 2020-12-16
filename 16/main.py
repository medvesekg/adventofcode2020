def split_list(list, delim):
    result = []
    remain = list
    while True:
        try:
            index = remain.index(delim)
            part = remain[:index]
            result.append(part)
            remain = remain[index+1:]
        except ValueError:
            result.append(remain)
            break
    return result

def parse_rules(data):
    parsed_rules = {}
    for row in data:
        tokens = row.split(':')
        name = tokens[0]
        rules = tokens[1].split('or')

        parsed_rules[name] = [range(int(string_range.split('-')[0]), int(string_range.split('-')[1]) + 1) for string_range in rules]

    return parsed_rules

def parse_your_ticket(data):
    return list(map(int, data[1].split(',')))

def parse_other_tickets(data):
    return [list(map(int, ticket.split(','))) for ticket in data[1:]]




with open('input', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

data = split_list(lines, '')
rules = parse_rules(data[0])
your_ticket = parse_your_ticket(data[1])
other_tickets = parse_other_tickets(data[2])


invalid = []
for ticket in other_tickets:
    for value in ticket:
        valid = False
        for field_rules in rules.values():
            for range in field_rules:
                if value in range:
                    valid = True
        if not valid:
            invalid.append(value)

print(sum(invalid))