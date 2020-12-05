def p1(seat):
    lo = 0
    hi = 127
    for i in range(7):
        if seat[i] == "F":
            hi = hi - int((hi-lo)/2) - 1
        elif seat[i] == "B":
            lo = int((hi-lo)/2 + 1) + lo

    lo2 = 0
    hi2 = 7
    for i in range(3):
        if seat[i+7] == "L":
            hi2 = hi2 - int((hi2-lo2)/2) - 1
        elif seat[i+7] == "R":
            lo2 = int((hi2-lo2)/2 + 1) + lo2

    return 8 * hi + hi2


input_file = open("input.txt", "r")
max_p1 = 0
all_seats = []
for line in input_file:
    max_p1 = max(max_p1, p1(line))
    all_seats.append(p1(line))

print(max_p1)

all_seats = sorted(all_seats)
prev_seat = None

for a_seat in all_seats:
    if prev_seat is None:
        prev_seat = a_seat
        continue
    if a_seat - prev_seat > 1:
        print(a_seat - 1)
        break
    prev_seat = a_seat
