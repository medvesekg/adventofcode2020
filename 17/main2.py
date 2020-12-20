from itertools import product
from copy import deepcopy

EMPTY = '.'
ACTIVE = '#'

class PocketDimension:

    def __init__(self):
        self.offset = {
            "x": 0,
            "y": 0,
            "z": 0,
            "w": 0
        }
        self.size = {
            "x": 1,
            "y": 1,
            "z": 1,
            "w": 1
        }

        self.coordinate_system = [[[[EMPTY]]]]

    def access(self, coordinates):
        x,y,z,w = coordinates
        x = self.array_index("x", x)
        y = self.array_index("y", y)
        z = self.array_index("z", z)
        w = self.array_index("w", w)
        return self.coordinate_system[x][y][z][w]

    def set(self, coordinates, value):

        x, y, z, w = coordinates
        x = self.array_index("x", x)
        y = self.array_index("y", y)
        z = self.array_index("z", z)
        w = self.array_index("w", w)

        self.coordinate_system[x][y][z][w] = value

    def array_index(self, direction, value):
        max = self.size[direction]- self.offset[direction] - 1
        min = -self.offset[direction]
        if value > max:
            getattr(self, "extend_" + direction)(value - max)
        elif value < min:
            getattr(self, "extend_" + direction)(value - min)
        return value + self.offset[direction]







    def extend_x(self, size):
        for i in range(abs(size)):
            if size > 0:
                self.coordinate_system.append(self.create_y())
            else:
                self.coordinate_system.insert(0, self.create_y())
        self.size["x"] += abs(size)
        if size < 0:
            self.offset["x"] += abs(size)

    def extend_y(self, size):
        for cube in self.coordinate_system:
            for i in range(abs(size)):
                if size > 0:
                    cube.append(self.create_z())
                else:
                    cube.insert(0, self.create_z())
        self.size["y"] += abs(size)
        if size < 0:
            self.offset["y"] += abs(size)

    def extend_z(self, size):
        for cube in self.coordinate_system:
            for plane in cube:
                for i in range(abs(size)):
                    if size > 0:
                        plane.append(self.create_w())
                    else:
                        plane.insert(0, self.create_w())

        self.size["z"] += abs(size)
        if size < 0:
            self.offset["z"] += abs(size)

    def extend_w(self, size):
        for cube in self.coordinate_system:
            for plane in cube:
                for row in plane:
                    for i in range(abs(size)):
                        if size > 0:
                            row.append(EMPTY)
                        else:
                            row.insert(0, EMPTY)

        self.size["w"] += abs(size)
        if size < 0:
            self.offset["w"] += abs(size)


    def create_y(self):
        return [self.create_z() for i in range(self.size["y"])]

    def create_z(self):
        return [self.create_w() for i in range(self.size["z"])]

    def create_w(self):
        return [EMPTY for i in range(self.size["w"])]


    def all_coordinates(self):
        coordinates = []
        for (x, cube) in enumerate(self.coordinate_system):
            for (y, plane) in enumerate(cube):
                for (z, row) in enumerate(plane):
                    for(w, value) in enumerate(row):
                        coordinates.append((
                            x - self.offset["x"],
                            y - self.offset["y"],
                            z - self.offset["z"],
                            w - self.offset["w"]
                        ))
        return coordinates

    def active_count(self):
        num_of_active = 0
        for coordinate in self.all_coordinates():
            if(self.access(coordinate) == ACTIVE):
                num_of_active += 1
        return num_of_active





def neighbours(coordinates):
    neighbour_coordinates = [coordinates for coordinates in product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]) if coordinates != (0, 0, 0, 0)]
    x,y,z,w = coordinates
    return [(x + diff[0], y + diff[1], z + diff[2], w + diff[3]) for diff in neighbour_coordinates]


def active_neighbours(coordinates, pocket_dimension):
    active_neighbour_count = 0
    for neigbour in neighbours(coordinates):
        if pocket_dimension.access(neigbour) == ACTIVE:
            active_neighbour_count += 1
    return active_neighbour_count

def run(pocket_dimension, max_cycles, current_cycle=0):
    print(current_cycle)
    if current_cycle < max_cycles:
        pocket_dimension.extend_x(1)
        pocket_dimension.extend_y(1)
        pocket_dimension.extend_z(1)
        pocket_dimension.extend_w(1)
        pocket_dimension.extend_x(-1)
        pocket_dimension.extend_y(-1)
        pocket_dimension.extend_z(-1)
        pocket_dimension.extend_w(-1)
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
        pocket_dimension.set((x,y,0,0), value)

end_state = run(pocket_dimension, 6)


print(end_state.active_count())







