input_file = open("input.txt", "r")

adapters_list = []

for line in input_file:
    adapters_list.append(int(line.strip()))

adapters_list = sorted(adapters_list)


# greedy approach, pick next smallest adapter
# time: O(N)
# space: O(1)
def p1(adapters):
    diffs = [0, 0, 0]

    jolt = 0
    for adapter in adapters:
        diffs[adapter - jolt - 1] += 1
        jolt = adapter

    diffs[2] += 1  # account from last adapter to device
    print(diffs[0] * diffs[2], diffs)


# find all paths from 0 to max(adapters)
# don't need to worry about visited since DAG
# dp array holds number of paths from index i to max(adapters)
# time: O(N)
# space: O(N)
def p2(adapters):
    adapters.insert(0, 0)
    # dp = [0] * (max(adapters) + 1)
    dp = dict.fromkeys(adapters, 0)

    dp[adapters[-1]] = 1

    # work backwards
    for adapter in reversed(adapters[0:-1]):
        for i in range(1, 4):
            dest = adapter + i
            if dest in adapters:
                dp[adapter] += dp[dest]

    print(dp[0])


p1(adapters_list)
p2(adapters_list)
