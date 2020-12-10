from time import time

with open('input', 'r') as f:
    lines = f.readlines()

adapters = list(map(int, lines))
adapters.sort()
device_joltage = max(adapters) + 3
adapters.append(device_joltage)
adapters_dict = {a: True for a in adapters}

LENGTH = len(adapters) + 1


def get_path(path, adapters):
    if len(path) == LENGTH:
        return path
    current_joltage = path[-1]
    possible_joltags = [current_joltage + i for i in range(1, 4)]
    available_joltages = [a for a in possible_joltags if a in adapters]

    for joltage in available_joltages:
        new_path = path.copy()
        new_path.append(joltage)
        remaining_adapters = [adapter for adapter in adapters if adapter != joltage]
        return get_path(new_path, remaining_adapters)

start = [0]
path = get_path(start, adapters)

prev_joltage = None
diffs = []
for joltage in path:
    if prev_joltage is not None:
        diffs.append(joltage - prev_joltage)

    prev_joltage = joltage

one_jolt = len([a for a in diffs if a == 1])
three_jolt = len([a for a in diffs if a == 3])

print("Solution 1: ", one_jolt * three_jolt)

all_paths = {}

def get_paths(path, adapters):
    global all_paths

    paths = 0
    current_joltage = path[-1]

    key = current_joltage
    if key in all_paths:
        return all_paths[key]

    if current_joltage == device_joltage:
        paths += 1

    possible_joltags = [current_joltage + i for i in range(1, 4)]

    available_joltages = [a for a in possible_joltags if a in adapters]

    for joltage in available_joltages:
        new_path = path.copy()
        new_path.append(joltage)
        paths += get_paths(new_path, [a for a in adapters if a != joltage])

    if not key in all_paths:
        all_paths[key] = 0

    all_paths[key] = paths
    return paths


start = time()
print("Solution 2: ", get_paths([0], adapters), end="")
end = time()
print(" (Solved in ", end - start, " seconds)")