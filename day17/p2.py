import copy

NUM_IT = 8
input_file = open("input.txt", "r")


def count_neighbors(c, z, w, x, y, m, r):
    num = 0
    for dz in range(-1, 2):
        if not (-r <= z + dz <= r):
            continue
        for dw in range(-1, 2):
            if not (-r <= w + dw <= r):
                continue
            for dx in range(-1, 2):
                if not (0 <= x + dx < m):
                    continue
                for dy in range(-1, 2):
                    if not (0 <= y + dy < m):
                        continue
                    if dz == dx == dy == dw == 0:
                        continue
                    if c[dz + z][dw + w][dx + x][dy + y] == '#':
                        num += 1
    return num


def empty_plane(n):
    ret = []
    for ii in range(n):
        ret.append(['.'] * n)
    return ret


def empty_cube(n):
    ret = {}
    for i in range(-NUM_IT, NUM_IT + 1):
        ret[i] = empty_plane(n)
    return ret


def print_cube(h):
    keys = sorted(h.keys())
    for key in keys:
        if count_cube_active(h[key]) > 0:
            print("w =", key)
            k2s = h[key].keys()
            k2s = sorted(k2s)
            for k2 in k2s:
                if count_plane_active(h[key][k2]) > 0:
                    print("z =", k2)
                    for row in h[key][k2]:
                        print(row)


def do_iter(c):
    c_cpy = copy.deepcopy(c)
    for z in range(-NUM_IT, NUM_IT + 1):
        print("l", z)
        for w in range(-NUM_IT, NUM_IT + 1):
            for x in range(input_len):
                for y in range(input_len):
                    n = count_neighbors(c, z, w, x, y, input_len, NUM_IT)
                    if c[z][w][x][y] == '#' and not (2 <= n <= 3):
                        c_cpy[z][w][x][y] = '.'
                    elif n == 3:
                        c_cpy[z][w][x][y] = '#'
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
    for w in range(-NUM_IT, NUM_IT + 1):
        num += count_plane_active(c[w])
    return num


def count_hcube_active(h):
    num = 0
    for z in range(-NUM_IT, NUM_IT + 1):
        num += count_cube_active(h[z])
    return num


plane = []
input_len = 0
for line in input_file:
    plane.append([','] * NUM_IT + list(line.strip()) + [','] * NUM_IT)

input_len = len(plane[0])

for i in range(NUM_IT + 1):
    plane.insert(0, ['.'] * input_len)
    plane.append(['.'] * input_len)

cube = {0: plane}

for i in range(-NUM_IT, NUM_IT + 1):
    if i != 0:
        cube[i] = empty_plane(input_len)

hcube = {0: cube}

for i in range(-NUM_IT, NUM_IT + 1):
    if i != 0:
        hcube[i] = empty_cube(input_len)

for it in range(6):
    print("ITERATION", it + 1)
    hcube = do_iter(hcube)
    # print_cube(hcube)

print(count_hcube_active(hcube))
