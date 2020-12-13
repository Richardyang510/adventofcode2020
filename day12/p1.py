input_file = open("input.txt", "r")

d_e = 0
d_n = 0
d_c = 'E'

turn_right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
turn_left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}

for line in input_file:
    direction = line[0]
    val = int(line[1:].strip())

    if direction == 'F':
        direction = d_c
    if direction == 'R':
        while val > 0:
            direction = turn_right[d_c]
            d_c = direction
            val -= 90
    if direction == 'L':
        while val > 0:
            direction = turn_left[d_c]
            d_c = direction
            val -= 90

    if direction == 'E':
        d_e += val
    elif direction == 'W':
        d_e -= val
    elif direction == 'N':
        d_n += val
    elif direction == 'S':
        d_n -= val

    print(d_c, d_e, d_n)

print(abs(d_e) + abs(d_n))
