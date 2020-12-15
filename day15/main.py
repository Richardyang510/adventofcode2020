# GO_TO = 2020  # part 1
GO_TO = 30000000  # part 2
INPUT = '0,13,1,16,6,17'

input_nums = list(map(int, '0,13,1,16,6,17'.split(',')))
last_seen = {}

first_ignore = len(input_nums)
next_num = 0
num = 0

for i in range(0, GO_TO):
    if i % (GO_TO/10) == 0:
        print(i/GO_TO * 100, "%")

    if i < first_ignore:
        num = input_nums[i]
    else:
        num = next_num

    if num in last_seen:
        next_num = i - last_seen[num]
    elif i >= first_ignore - 1:
        next_num = 0

    last_seen[num] = i

print(num)
