from itertools import product
from copy import deepcopy

EMPTY = '.'
ACTIVE = '#'

class PocketDimension:

    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0
        self.offset_z = 0
        self.size_x = 1
        self.size_y = 1
        self.size_z = 1
        self.coordinate_system = [[[EMPTY]]]

    def access(self, coordinates):
        x,y,z = coordinates
        x = self.actual_x(x)
        y = self.actual_y(y)
        z = self.actual_z(z)
        return self.coordinate_system[x][y][z]

    def access_x(self, x):
        actual_x = self.actual_x(x)
        return self.coordinate_system[actual_x]

    def access_y(self, y):
        actual_y = self.actual_y(y)
        return self.coordinate_system[actual_y]

    def access_z(self, z):
        actual_z = self.actual_z(z)
        return self.coordinate_system[actual_z]

    def set(self, coordinates, value):
        x, y, z = coordinates

        x = self.actual_x(x)
        y = self.actual_y(y)
        z = self.actual_z(z)

        self.coordinate_system[x][y][z] = value



    def actual_x(self, x):
        max = self.size_x - self.offset_x - 1
        min = -self.offset_x
        if x > max:
            self.extend_x(x - max)
        elif x < min:
            self.extend_x(x - min)
        return x + self.offset_x

    def actual_y(self, y):
        max = self.size_y - self.offset_y - 1
        min = -self.offset_y
        if y > max:
            self.extend_y(y - max)
        elif y < min:
            self.extend_y(y - min)
        return y + self.offset_y

    def actual_z(self, z):
        max = self.size_z - self.offset_z - 1
        min = -self.offset_z
        if z > max:
            self.extend_z(z - max)
        elif z < min:
            self.extend_z(z - min)
        return z + self.offset_z

    def extend_x(self, size):
        for i in range(abs(size)):
            if size > 0:
                self.coordinate_system.append(self.create_y())
            else:
                self.coordinate_system.insert(0, self.create_y())
        self.size_x += abs(size)
        if size < 0:
            self.offset_x += abs(size)

    def extend_y(self, size):
        for plane in self.coordinate_system:
            for i in range(abs(size)):
                if size > 0:
                    plane.append(self.create_z())
                else:
                    plane.insert(0, self.create_z())
        self.size_y += abs(size)
        if size < 0:
            self.offset_y += abs(size)

    def extend_z(self, size):
        for plane in self.coordinate_system:
            for row in plane:
                for i in range(abs(size)):
                    if size > 0:
                        row.append(EMPTY)
                    else:
                        row.insert(0, EMPTY)

        self.size_z += abs(size)
        if size < 0:
            self.offset_z += abs(size)

    def create_y(self):
        return [self.create_z() for i in range(self.size_y)]

    def create_z(self):
        return [EMPTY for i in range(self.size_z)]


    def all_coordinates(self):
        coordinates = []
        for (x, plane) in enumerate(self.coordinate_system):
            for (y, row) in enumerate(plane):
                for (z, value) in enumerate(row):
                    coordinates.append((
                        x - self.offset_x,
                        y - self.offset_y,
                        z - self.offset_z
                    ))
        return coordinates

    def active_count(self):
        num_of_active = 0
        for coordinate in self.all_coordinates():
            if(self.access(coordinate) == ACTIVE):
                num_of_active += 1
        return num_of_active





def neighbours(coordinates):
    neighbour_coordinates = [coordinates for coordinates in product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]) if coordinates != (0, 0, 0)]
    x,y,z = coordinates
    return [(x + diff[0], y + diff[1], z + diff[2]) for diff in neighbour_coordinates]


def active_neighbours(coordinates, pocket_dimension):
    active_neighbour_count = 0
    for neigbour in neighbours(coordinates):
        if pocket_dimension.access(neigbour) == ACTIVE:
            active_neighbour_count += 1
    return active_neighbour_count

def run(pocket_dimension, max_cycles, current_cycle=0):
    if current_cycle < max_cycles:
        pocket_dimension.extend_x(1)
        pocket_dimension.extend_y(1)
        pocket_dimension.extend_z(1)
        pocket_dimension.extend_x(-1)
        pocket_dimension.extend_y(-1)
        pocket_dimension.extend_z(-1)
        new_pocket_dimension = deepcopy(pocket_dimension)

        for coordinate in pocket_dimension.all_coordinates():
            value = pocket_dimension.access(coordinate)
            num_active_neighbours = active_neighbours(coordinate, pocket_dimension)
            if value == ACTIVE:
                if num_active_neighbours in [2,3]:
                    continue
                else:
                    new_pocket_dimension.set(coordinate, EMPTY)
            else:
                if num_active_neighbours == 3:
                    new_pocket_dimension.set(coordinate, ACTIVE)
                else:
                    continue
        return run(new_pocket_dimension, max_cycles, current_cycle + 1)
    else:
        return pocket_dimension




with open('input', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

pocket_dimension = PocketDimension()
for (y, line) in enumerate(lines):
    for (x, value) in enumerate(line):
        pocket_dimension.set((x,y,0), value)


end_state = run(pocket_dimension, 6)


print(end_state.active_count())







