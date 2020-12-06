input_file = open("input.txt", "r")
alphabet = set()
tot = 0
for line in input_file:
    for c in line:
        if c != '\n':
            alphabet.add(c)
    if line == "\n":
        tot += len(alphabet)
        alphabet = set()
tot += len(alphabet)
print(tot)

input_file = open("input.txt", "r")
tot = 0
group_sets = []
for line in input_file:
    if line == "\n":
        tot += len(set.intersection(*group_sets))
        group_sets = []
        continue

    new_group = set()
    for c in line:
        if c != '\n':
            new_group.add(c)
    group_sets.append(new_group)

tot += len(set.intersection(*group_sets))
print(tot)
