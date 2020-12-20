from time import time

with open('input', 'r') as f:
    numbers = [int(number) for number in f.read().split(',')]

start = time()
turn = len(numbers)
spoken = { number: i+1 for i,number in enumerate(numbers[:-1])}

while True:

    if(turn == 30000000):
        print(numbers[-1])
        print(time() - start)
        break

    last_number = numbers[-1]

    if last_number in spoken:
        numbers.append(len(numbers) - spoken[last_number])
    else:
        numbers.append(0)
    spoken[last_number] = turn

    turn += 1

