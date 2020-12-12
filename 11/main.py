from itertools import product
from copy import deepcopy

FLOOR = '.'
EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'

with open('input', 'r') as f:
    lines = f.readlines()

seats = list(map(lambda l: list(l.strip()), lines))

HEIGHT = len(seats)
WIDTH = len(seats[0])


def adjacent_positions(seat):
    adjacent = [
        position for position in product([-1,0,1],[-1,0,1])
        if position != (0,0)

    ]
    possible = map(lambda position: (seat[0] + position[0], seat[1] + position[1]), adjacent)

    return [
        adjacent_seat for adjacent_seat in possible
        if adjacent_seat[0] >= 0
        and adjacent_seat[1] >= 0
        and adjacent_seat[0] < HEIGHT
        and adjacent_seat[1] < WIDTH
    ]



def occupied_adjacent2(seat, seats):
    directions = [
        position for position in product([-1,0,1],[-1,0,1])
        if position != (0,0)
    ]

    occupied = 0
    for direction in directions:
        current = seat
        while True:
            new = (current[0] + direction[0], current[1] + direction[1])
            if new[0] < 0 or new[1] < 0 or new[0] > HEIGHT - 1 or new[1] > WIDTH - 1:
                break
            value = seats[new[0]][new[1]]

            if value == '#':
                occupied += 1
                break
            if value == 'L':
                break
            current = new

    return occupied


def occupied_adjacent1(seat, seats):
    adjacent = adjacent_positions(seat)
    return len([a for a in adjacent if seats[a[0]][a[1]] == OCCUPIED_SEAT])


def next_round(seats, occupied_adjacent, threshold):
    seats_copy = deepcopy(seats)
    changes = 0
    for (rowIndex, row) in enumerate(seats):
        for (colIndex, seat) in enumerate(row):
            if seat == EMPTY_SEAT and occupied_adjacent((rowIndex, colIndex), seats) == 0:
                seats_copy[rowIndex][colIndex] = OCCUPIED_SEAT
                changes += 1
            elif seat == OCCUPIED_SEAT and occupied_adjacent((rowIndex, colIndex), seats) >= threshold:
                seats_copy[rowIndex][colIndex] = EMPTY_SEAT
                changes += 1

    return {
        "changes": changes,
        "seats": seats_copy
    }

def count_occupied(seats):
    occupied = 0
    for row in seats:
        for seat in row:
            if seat == OCCUPIED_SEAT:
                occupied += 1
    return occupied

def run(seats, occupied_adjacent, threshold, rounds=0):

    result = next_round(seats, occupied_adjacent, threshold)
    if result["changes"]:
        return run(result["seats"], occupied_adjacent, threshold, rounds + 1)
    else:
        return {
            "seats": result["seats"],
            "rounds": rounds
        }

def show_state(seats):
    for row in seats:
        for seat in row:
            print(seat + '', end="")
        print('')
    print('')

result = run(seats, occupied_adjacent1, 4)

print(count_occupied(result["seats"]))

result2 = run(seats, occupied_adjacent2, 5)

print(count_occupied(result2["seats"]))

