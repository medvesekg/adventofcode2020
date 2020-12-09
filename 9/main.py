import itertools

PREAMBLE_LENGTH = 25

with open('input', 'r') as f:
    lines = f.readlines()

numbers = list(map(int, lines))
preamble = numbers[:PREAMBLE_LENGTH]
iteration = 1
invalid = None

for i in range(PREAMBLE_LENGTH, len(numbers)):
    number = numbers[i]
    combinations = itertools.combinations(preamble, 2)
    sums = list(map(sum, combinations))

    if number not in sums:
        invalid = number
        break

    preamble = numbers[iteration:iteration+PREAMBLE_LENGTH]
    iteration += 1

print(invalid)

block = []
for left in range(len(numbers)):
    for right in range(left+2, len(numbers)):
        range_sum = sum(numbers[left:right])
        if range_sum == invalid and len(numbers[left:right]) > len(block):
            block = numbers[left:right]

weakness = max(block) + min(block)

print(weakness)