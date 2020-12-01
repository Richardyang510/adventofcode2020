# d1p1
# finds two values that sum to 2020, and print their product
def two_sum(data):
    left = 0
    right = len(data) - 1

    while left < right:
        tot = data[left] + data[right]
        if tot == 2020:
            return data[left] * data[right]
        elif tot < 2020:
            left += 1
        else:
            right -= 1

    return None


# d1p2
# finds three values that sum to 2020, and print their product
def three_sum(data):
    for i in range(len(data)):
        left = i + 1
        right = len(data) - 1

        while left < right:
            tot = data[i] + data[left] + data[right]
            if tot == 2020:
                return data[i] * data[left] * data[right]
            elif tot < 2020:
                left += 1
            else:
                right -= 1

    return None


input_file = open("input.txt", "r")
num_data = []

for line in input_file:
    num_data.append(int(line.strip('\n')))

num_data = sorted(num_data)

print(two_sum(num_data))
print(three_sum(num_data))