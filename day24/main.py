import copy

input_file = open("input.txt", "r")


class HexGrid:
    grid = {}
    r = None
    neighbors = [(0, -1), (-1, -1), (-1, 0), (0, 1), (1, 1), (1, 0)]

    def __init__(self, radius):
        self.r = radius
        for i in range(-radius, radius + 1):
            self.grid[i] = {}
            for j in range(-radius, radius + 1):
                self.grid[i][j] = 0

    def flip(self, x, y):
        if self.grid[x][y] == 0:
            self.grid[x][y] = 1
        else:
            self.grid[x][y] = 0

    def count_black(self):
        tot = 0
        for i in range(-self.r, self.r + 1):
            for j in range(-self.r, self.r + 1):
                if self.grid[i][j] == 1:
                    tot += 1
        return tot

    def iterate(self):
        new_grid = copy.deepcopy(self.grid)
        for x in range(-self.r, self.r + 1):
            for y in range(-self.r, self.r + 1):
                num_black_neighbors = 0
                for dx, dy in self.neighbors:
                    if -self.r <= x + dx <= self.r and -self.r <= y + dy <= self.r:
                        if self.grid[x + dx][y + dy] == 1:
                            num_black_neighbors += 1

                if self.grid[x][y] == 1 and (num_black_neighbors == 0 or num_black_neighbors > 2):
                    new_grid[x][y] = 0

                if self.grid[x][y] == 0 and num_black_neighbors == 2:
                    new_grid[x][y] = 1

        self.grid = new_grid


def go_dir(x, y, d):
    if d == "ne":
        return x, y - 1
    elif d == "nw":
        return x - 1, y - 1
    elif d == "w":
        return x - 1, y
    elif d == "sw":
        return x, y + 1
    elif d == "se":
        return x + 1, y + 1
    elif d == "e":
        return x + 1, y


def traverse(path):
    x, y = 0, 0
    while len(path) > 0:
        if path.startswith("s") or path.startswith("n"):
            d = path[:2]
            path = path[2:]
        else:
            d = path[:1]
            path = path[1:]
        x, y = go_dir(x, y, d)
    return x, y


hg = HexGrid(70)  # magic number

for line in input_file:
    fx, fy = traverse(line.strip())
    hg.flip(fx, fy)

print(hg.count_black())

for i in range(100):
    hg.iterate()

print(hg.count_black())
