PREAMBLE = 25

input_file = open("input.txt", "r")

numbers = []

for line in input_file:
    numbers.append(int(line.strip()))


def two_sum(data, sum_to):
    left = 0
    right = len(data) - 1

    while left < right:
        tot = data[left] + data[right]
        if tot == sum_to:
            return data[left] + data[right]
        elif tot < sum_to:
            left += 1
        else:
            right -= 1

    return None


def p1(nums):
    for i in range(len(nums) - PREAMBLE):
        sorted_nums = sorted(list(nums[i: i + PREAMBLE]))

        if two_sum(sorted_nums, nums[i + PREAMBLE]) is None:
            return nums[i + PREAMBLE]


part_1 = p1(numbers)
print(part_1)


def p2(nums, sum_to):
    for i in range(len(nums)):
        tot = 0
        j = i
        smallest = nums[j]
        largest = nums[j]
        while tot < sum_to:
            tot += nums[j]
            smallest = min(smallest, nums[j])
            largest = max(largest, nums[j])
            j += 1
        if tot == sum_to:
            return smallest + largest


print(p2(numbers, part_1))
