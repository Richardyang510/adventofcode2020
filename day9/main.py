PREAMBLE = 25

input_file = open("input.txt", "r")

numbers = []

for line in input_file:
    numbers.append(int(line.strip()))


def make_set(nums, lower, upper):
    num_set = set()
    for i in range(lower, upper):
        for j in range(lower, upper):
            if i != j:
                num_set.add(nums[i] + nums[j])

    return num_set


def p1(nums):
    for i in range(len(nums) - PREAMBLE):
        num_set = make_set(nums, i, i + PREAMBLE)
        # print(i, nums[i + PREAMBLE], num_set)
        if nums[i + PREAMBLE] not in num_set:
            return nums[i + PREAMBLE]


part_1 = p1(numbers)
print(part_1)


def p2(nums, sum_to):
    for i in range(len(nums)):
        tot = 0
        j = i
        while tot < sum_to:
            tot += nums[j]
            j += 1
        if tot == sum_to:
            smallest = nums[i]
            largest = nums[i]
            for a in range(i, j):
                smallest = min(smallest, nums[a])
                largest = max(largest, nums[a])
            return smallest + largest


print(p2(numbers, part_1))
