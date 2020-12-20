import copy


def get_edge(tile, e):
    if e == 'u':
        return tile[0]
    elif e == 'd':
        return tile[-1]
    elif e == 'l':
        ed = ""
        for row in tile:
            ed += row[0]
        return ed
    elif e == 'r':
        ed = ""
        for row in tile:
            ed += row[-1]
        return ed
    return ""


SQUARE_SIZE = 12
TILE_SIZE = 10

input_file = open("input.txt", "r")

tiles = {}
tile_relations = {}

tile_id = 0
curr_tile = []

tile_or = ['u', 'd', 'l', 'r']
first = 0

for line in input_file:
    if len(line.strip()) == 0:
        tiles[tile_id] = curr_tile
        curr_tile = []
        continue

    if line.startswith("Tile"):
        tile_id = int(line[5:9])
    else:
        curr_tile.append(line.strip())
tiles[tile_id] = curr_tile

for t1_id in tiles:
    matches = 0
    t1 = tiles[t1_id]
    rel = {}
    for t2_id in tiles:
        if t1_id != t2_id:
            t2 = tiles[t2_id]
            for t1_or in tile_or:
                for t2_or in tile_or:
                    t1_ed = get_edge(t1, t1_or)
                    t2_ed = get_edge(t2, t2_or)
                    if t1_ed == t2_ed or t1_ed == t2_ed[::-1]:
                        is_flip = 1 if t1_ed == t2_ed[::-1] else 0
                        rel[t1_or + t2_or + str(is_flip)] = t2_id
    tile_relations[t1_id] = rel

# p1
prod = 1
for t_id in tile_relations:
    if len(tile_relations[t_id].keys()) == 2:
        print(t_id)
        first = t_id
        prod *= t_id

print(prod)

# p2
# for key in tile_relations:
#     print(key, tile_relations[key])

flip = {'r': 'l', 'l': 'r', 'u': 'd', 'd': 'u'}
flip_v = {'r': 'r', 'l': 'l', 'u': 'd', 'd': 'u'}
rott = {'l': 'u', 'u': 'r', 'r': 'd', 'd': 'l'}


def find_node_for(start, d):
    for key in tile_relations[start]:
        if key[0] == d:
            return tile_relations[start][key], key[1], key[0]


def traverse(start, d, nodes_only=False):
    curr = start
    came_from = ' '
    visited = []
    for i in range(SQUARE_SIZE):
        if i == SQUARE_SIZE - 1:
            # print(curr, '    ', came_from, ' ', tile_relations[curr])
            if nodes_only:
                visited.append(curr)
            else:
                visited.append((curr, came_from, ' '))
            break
        nex, ed_taken, ed_from = find_node_for(curr, d)
        ed_want = flip[ed_taken]
        # print(curr, nex, came_from, ed_from, tile_relations[curr])
        if nodes_only:
            visited.append(curr)
        else:
            visited.append((curr, came_from, ed_from))
        curr = nex
        came_from = ed_taken
        d = ed_want
    return visited


def rot(t, times=1):
    for _ in range(times):
        new_t = []
        for r in list(zip(*t[::-1])):
            new_t.append(''.join(list(r)))
        t = new_t

    return t


def mir(t, h=False):
    new_t = []
    if h:
        new_t = list(reversed(t))
    else:
        for r in t:
            new_t.append(r[::-1])

    return new_t


def print_t(t):
    for r in t:
        print(r)


def trim_tile(t):
    new_t = []
    for idx in range(TILE_SIZE):
        if 1 <= idx < TILE_SIZE - 1:
            new_t.append(t[idx][1:-1])
    return new_t


v = traverse(first, 'd')

img_arr = []
for k in v:
    s, d1, d2 = k
    n = ''
    for key in list(tile_relations[s].keys()):
        if key[0] != d1 and key[0] != d2:
            n = key[0]
            break
    img_arr.append(traverse(s, n, True))

for row in img_arr:
    print(row)

# print(tile_relations[first])
# tiles[first] = rot(tiles[first], 3)

for i in range(SQUARE_SIZE):
    for j in range(SQUARE_SIZE):
        if i == j == 0:
            continue
        # brute force all 8 orientations
        ors = [tiles[img_arr[i][j]]]
        ors.append(rot(ors[0]))
        ors.append(rot(ors[1]))
        ors.append(rot(ors[2]))
        ors.append(mir(ors[0]))
        ors.append(rot(ors[4]))
        ors.append(rot(ors[5]))
        ors.append(rot(ors[6]))

        found = False

        for or_tile in ors:
            # check prev neighbors (first left, then up)

            if 0 <= j - 1 < SQUARE_SIZE:
                neighbor_tile = tiles[img_arr[i][j - 1]]

                e1 = get_edge(or_tile, 'l')
                e2 = get_edge(neighbor_tile, 'r')

                if e1 == e2:
                    if i == 0:
                        tiles[img_arr[i][j]] = or_tile
                        found = True
                        break

            if 0 <= i - 1 < SQUARE_SIZE:
                neighbor_tile = tiles[img_arr[i - 1][j]]

                e1 = get_edge(or_tile, 'u')
                e2 = get_edge(neighbor_tile, 'd')

                if e1 == e2:
                    tiles[img_arr[i][j]] = or_tile
                    found = True
                    break

        if not found:
            print("NOT FOUND", img_arr[i][j])

# for i in range(SQUARE_SIZE):
#     for j in range(TILE_SIZE):
#         line = ''
#         for k in range(SQUARE_SIZE):
#             line += str(tiles[img_arr[i][k]][j]) + ' '
#         print(line)
#     print()

for t in tiles:
    tiles[t] = trim_tile(tiles[t])

img = []
for i in range(SQUARE_SIZE):
    for j in range(TILE_SIZE - 2):
        line = ''
        for k in range(SQUARE_SIZE):
            line += str(tiles[img_arr[i][k]][j])
        img.append(line)

num_hash = 0
for row in img:
    num_hash += row.count("#")

sea_monster = ["..................#.",
               "#....##....##....###",
               ".#..#..#..#..#..#..."]

mons_ors = [sea_monster]
mons_ors.append(rot(mons_ors[0]))
mons_ors.append(rot(mons_ors[1]))
mons_ors.append(rot(mons_ors[2]))
mons_ors.append(mir(mons_ors[0]))
mons_ors.append(rot(mons_ors[4]))
mons_ors.append(rot(mons_ors[5]))
mons_ors.append(rot(mons_ors[6]))

for mons_or in mons_ors:
    img_c = copy.deepcopy(img)
    num_found = 0
    mons_h = len(mons_or)
    mons_w = len(mons_or[0])
    # top left of mons
    for i in range(len(img_c) - mons_h):
        for j in range(len(img_c) - mons_w):
            # iterate over monster
            match = True
            for k in range(mons_h):
                for l in range(mons_w):
                    if mons_or[k][l] == "#" and img_c[i + k][j + l] != '#':
                        match = False
                        break
                if not match:
                    break
            if match:
                num_found += 1
    if num_found != 0:
        print(num_found, num_hash - 15 * num_found)
