SUM_TO = 2020


# d1p1
# finds two values that sum to 2020, and print their product
def two_sum(data, other=0):
    left = 0
    right = len(data) - 1

    while left < right:
        tot = other + data[left] + data[right]
        if tot == SUM_TO:
            return data[left] * data[right] * (other if other != 0 else 1)
        elif tot < SUM_TO:
            left += 1
        else:
            right -= 1

    return None


# d1p2
# finds three values that sum to 2020, and print their product
def three_sum(data):
    for i in range(len(data)):
        t_sum = two_sum(data[i+1:], data[i])
        if t_sum is None:
            continue
        else:
            return t_sum

    return None


input_file = open("input.txt", "r")
num_data = []

for line in input_file:
    num_data.append(int(line.strip('\n')))

num_data = sorted(num_data)

print(two_sum(num_data))
print(three_sum(num_data))
