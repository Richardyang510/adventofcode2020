input_file = open("input.txt", "r")

reading_input = False

ranges = {}
my_ticket = None
nearby = []
valid_tickets = []
all_ranges = []
err_rate = 0
poss_cols = {}

for line in input_file:
    if len(line.strip()) == 0:
        continue
    if line.startswith("your"):
        my_ticket = list(map(int, input_file.readline().strip().split(',')))
        reading_input = True
    elif reading_input and not line.startswith("nearby"):
        t = list(map(int, line.strip().split(',')))
        nearby.append(t)
    elif not reading_input:
        loc = line.split(':')[0]
        range_1 = line.split(':')[1].split("or")[0].strip().split("-")
        range_2 = line.split(':')[1].split("or")[1].strip().split("-")

        r_t1 = (int(range_1[0]), int(range_1[1]))
        r_t2 = (int(range_2[0]), int(range_2[1]))

        all_ranges.append(r_t1)
        all_ranges.append(r_t2)

        ranges[loc] = [r_t1, r_t2]

for n in nearby:
    valid = True
    for val in n:
        found = False
        for lo, hi in all_ranges:
            if lo <= val <= hi:
                found = True
                break
        if not found:
            err_rate += val
            valid = False
    if valid:
        valid_tickets.append(n)

print(err_rate)

valid_tickets.insert(0, my_ticket)

for i in range(len(valid_tickets[0])):
    for loc in ranges:
        r1_l, r1_h = ranges[loc][0]
        r2_l, r2_h = ranges[loc][1]
        valid = True
        for ticket in valid_tickets:
            val = ticket[i]
            if not (r1_l <= val <= r1_h or r2_l <= val <= r2_h):
                valid = False
                break

        if valid:
            if i not in poss_cols:
                poss_cols[i] = []
            if loc not in poss_cols[i]:
                poss_cols[i].append(loc)

# for key in poss_cols:
#     print(key, poss_cols[key])

visited = {}
num_left = len(poss_cols)

while num_left > 0:
    for col in poss_cols:
        if len(poss_cols[col]) == 1 and col not in visited:
            loc = poss_cols[col][0]
            visited[col] = loc
            num_left -= 1

            for other_col in poss_cols:
                if loc in poss_cols[other_col]:
                    poss_cols[other_col].remove(loc)

prod = 1
for col in visited:
    if visited[col].startswith("departure"):
        prod *= my_ticket[col]

print(prod)
