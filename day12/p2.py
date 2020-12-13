input_file = open("input.txt", "r")

d_e = 0
d_n = 0
w_e = 10
w_n = 1


def turn_right(n, e):
    return -e, n


def turn_left(n, e):
    return e, -n


for line in input_file:
    direction = line[0]
    val = int(line[1:].strip())

    if direction == 'F':
        for i in range(val):
            d_e += w_e
            d_n += w_n
    if direction == 'R':
        while val > 0:
            w_n, w_e = turn_right(w_n, w_e)
            val -= 90
    if direction == 'L':
        while val > 0:
            w_n, w_e = turn_left(w_n, w_e)
            val -= 90

    if direction == 'E':
        w_e += val
    elif direction == 'W':
        w_e -= val
    elif direction == 'N':
        w_n += val
    elif direction == 'S':
        w_n -= val

    print(d_e, d_n)

print(abs(d_e) + abs(d_n))
