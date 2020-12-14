import math

with open('input', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

earliest = int(lines[0])
buses = map(int, [id for id in lines[1].split(',') if id != 'x'])

earliest_bus = min(buses, key= lambda bus: (math.ceil(earliest / bus) * bus) - earliest)

departure = math.ceil(earliest / earliest_bus) * earliest_bus
wait = departure - earliest

result = wait * earliest_bus

print(result)