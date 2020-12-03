def p1(trees, right_amt=3, down_amt=1):
    end = len(trees)
    wid = len(trees[0]) - 1

    x = 0
    y = 0

    num_trees = 0

    while y < end:
        num_trees += 1 if trees[y][x] == '#' else 0

        x = (x + right_amt) % wid
        y += down_amt

    return num_trees


input_file = open("input.txt", "r")
tree_map = []
for line in input_file:
    tree_map.append(line)

print(p1(tree_map))
print(p1(tree_map, 1) * p1(tree_map, 3) * p1(tree_map, 5) * p1(tree_map, 7) * p1(tree_map, 1, 2))
