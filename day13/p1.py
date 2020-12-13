import math

input_file = open("input.txt", "r")

depart_time = int(input_file.readline().strip())

buses = input_file.readline().strip().split(',')
buses = list(filter(lambda a: a != 'x', buses))

min_delta = depart_time
bus_id = 0

for bus in buses:
    next_time = (math.floor(depart_time / int(bus)) + 1) * int(bus)
    delta = next_time - depart_time

    if delta < min_delta:
        min_delta = delta
        bus_id = int(bus)

print(bus_id * min_delta)
