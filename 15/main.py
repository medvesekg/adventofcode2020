from time import time

with open('testinput', 'r') as f:
    numbers = [int(number) for number in f.read().split(',')]

start = time()
turn = len(numbers)
while True:

    if(turn == 10000):
        print(numbers[-1])
        print(time() - start)
        break


    last_number = numbers[-1]

    try:
        previously_spoken = len(numbers) - numbers[::-1][1:].index(last_number) - 1
        last_spoken = len(numbers)

        numbers.append(last_spoken - previously_spoken)
    except ValueError:
        numbers.append(0)


    turn += 1

