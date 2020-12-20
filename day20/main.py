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


SQUARE_SIZE = 3
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
for key in tile_relations:
    print(key, tile_relations[key])

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


def rot(t, rels, times=1):
    for _ in range(times):
        new_t = []
        for r in list(zip(*t[::-1])):
            new_t.append(''.join(list(r)))
        t = new_t

    for _ in range(times):
        new_rels = {}
        for rell in rels:
            old_dir = rell[0]
            new_dir = rott[old_dir]
            new_key = new_dir + rell[1:]
            new_rels[new_key] = rels[rell]
        rels = new_rels

    return t, rels


def mir(t, rels, h=False):
    new_t = []
    if h:
        for r in t:
            new_t.append(r[::-1])
    else:
        new_t = reversed(t)

    new_rels = {}
    for rell in rels:
        old_or = rell[2]
        new_dir = '1' if old_or == '0' else '0'
        new_key = rell[:2] + new_dir
        new_rels[new_key] = rels[rell]
    return new_t


def print_t(t):
    for r in t:
        print(r)


v = traverse(first, 'l')

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

tiles[first], tile_relations[first] = rot(tiles[first], tile_relations[first], 3)

for key in tile_relations:
    print(key, tile_relations[key])

for i in range(SQUARE_SIZE):
    for j in range(TILE_SIZE):
        line = ''
        for k in range(SQUARE_SIZE):
            line += str(tiles[img_arr[i][k]][j]) + ' '
        print(line)
    print()
