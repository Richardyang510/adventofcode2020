input_file = open("input.txt", "r")

deck = [[], []]
input_player = 0

for line in input_file:
    if len(line.strip()) == 0:
        continue
    elif line.startswith("Player 1"):
        input_player = 0
    elif line.startswith("Player 2"):
        input_player = 1
    else:
        deck[input_player].append(int(line.strip()))

print(deck)

while len(deck[0]) > 0 and len(deck[1]) > 0:
    top_1 = deck[0].pop(0)
    top_2 = deck[1].pop(0)
    if top_1 > top_2:
        deck[0].append(top_1)
        deck[0].append(top_2)
    else:
        deck[1].append(top_2)
        deck[1].append(top_1)

print(deck)

num_cards = len(deck[0])
tot = 0
for i in range(1, num_cards+1):
    tot += i * deck[0][num_cards - i]
print(tot)

num_cards = len(deck[1])
tot = 0
for i in range(1, num_cards+1):
    tot += i * deck[1][num_cards - i]
print(tot)