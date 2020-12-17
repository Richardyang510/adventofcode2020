import copy

NUM_IT = 12
input_file = open("input.txt", "r")
cube = {}


def count_neighbors(c, z, x, y, m, r):
    num = 0
    for dz in range(-1, 2):
        if not (-r <= z + dz <= r):
            continue
        for dx in range(-1, 2):
            if not (0 <= x + dx < m):
                continue
            for dy in range(-1, 2):
                if not (0 <= y + dy < m):
                    continue
                if dz == dx == dy == 0:
                    continue
                if c[dz + z][dx + x][dy + y] == '#':
                    num += 1
    return num


def empty_plane(n):
    ret = []
    for ii in range(n):
        ret.append(['.'] * n)
    return ret


def print_cube(c):
    keys = sorted(c.keys())
    for key in keys:
        if count_plane_active(c[key]) > 0:
            print("z =", key)
            for row in c[key]:
                print(row)


def do_iter(c):
    c_cpy = copy.deepcopy(c)
    for z in range(-NUM_IT, NUM_IT + 1):
        for x in range(input_len):
            for y in range(input_len):
                n = count_neighbors(c, z, x, y, input_len, NUM_IT)
                if c[z][x][y] == '#' and not (2 <= n <= 3):
                    c_cpy[z][x][y] = '.'
                elif n == 3:
                    c_cpy[z][x][y] = '#'
    return c_cpy


def count_plane_active(p):
    num = 0
    for x in range(input_len):
        for y in range(input_len):
            if p[x][y] == '#':
                num += 1
    return num


def count_cube_active(c):
    num = 0
    for z in range(-NUM_IT, NUM_IT + 1):
        num += count_plane_active(c[z])
    return num


plane = []
input_len = 0
for line in input_file:
    plane.append([','] * NUM_IT + list(line.strip()) + [','] * NUM_IT)

input_len = len(plane[0])

for i in range(NUM_IT + 1):
    plane.insert(0, ['.'] * input_len)
    plane.append(['.'] * input_len)

cube[0] = plane

for i in range(-NUM_IT, NUM_IT + 1):
    if i != 0:
        cube[i] = empty_plane(input_len)

print_cube(cube)
for it in range(6):
    print("ITERATION", it + 1)
    cube = do_iter(cube)
    # print_cube(cube)

print(count_cube_active(cube))
