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

def occupied_adjacent(seat, seats):
    adjacent = adjacent_positions(seat)
    return len([a for a in adjacent if seats[a[0]][a[1]] == OCCUPIED_SEAT])


def next_round(seats):
    seats_copy = deepcopy(seats)
    changes = 0
    for (rowIndex, row) in enumerate(seats):
        for (colIndex, seat) in enumerate(row):
            if seat == EMPTY_SEAT and occupied_adjacent((rowIndex, colIndex), seats) == 0:
                seats_copy[rowIndex][colIndex] = OCCUPIED_SEAT
                changes += 1
            elif seat == OCCUPIED_SEAT and occupied_adjacent((rowIndex, colIndex), seats) > 3:
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

def run(seats, rounds=0):

    result = next_round(seats)
    if result["changes"]:
        return run(result["seats"], rounds + 1)
    else:
        return {
            "seats": result["seats"],
            "rounds": rounds
        }

def show_state(seats):
    for row in seats:
        for seat in row:
            print(seat, end="")
        print('\n')

result = run(seats)

print(count_occupied(result["seats"]))

