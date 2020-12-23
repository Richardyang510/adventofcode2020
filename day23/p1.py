num_it = 100

cups_num = 123487596
cups = list(map(int, str(cups_num)))
num_cups = len(cups)

i = 0

for it in range(num_it):
    cur_cup = cups[i]

    pickup_1 = cups[(i + 1) % num_cups]
    pickup_2 = cups[(i + 2) % num_cups]
    pickup_3 = cups[(i + 3) % num_cups]

    cups.remove(pickup_1)
    cups.remove(pickup_2)
    cups.remove(pickup_3)

    dest_cup_val = cur_cup - 1
    while dest_cup_val in [pickup_1, pickup_2, pickup_3]:
        dest_cup_val -= 1

    if dest_cup_val < min(cups):
        dest_cup_val = max(cups)

    cups.insert(cups.index(dest_cup_val) + 1, pickup_3)
    cups.insert(cups.index(dest_cup_val) + 1, pickup_2)
    cups.insert(cups.index(dest_cup_val) + 1, pickup_1)

    i = (cups.index(cur_cup) + 1) % num_cups

print(cups)
