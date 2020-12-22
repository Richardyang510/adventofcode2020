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


def game(decks):
    prev_hands = [set(), set()]
    while len(decks[0]) > 0 and len(decks[1]) > 0:

        d1s = ','.join(map(str, decks[0]))
        d2s = ','.join(map(str, decks[1]))

        if d1s in prev_hands[0] or d2s in prev_hands[1]:
            return 0, None
        else:
            prev_hands[0].add(','.join(map(str, decks[0])))
            prev_hands[1].add(','.join(map(str, decks[1])))

            top_1 = decks[0].pop(0)
            top_2 = decks[1].pop(0)

            if len(decks[0]) >= top_1 and len(decks[1]) >= top_2:
                winner, wd = game([decks[0][:top_1], decks[1][:top_2]])
            else:
                if top_1 > top_2:
                    winner = 0
                else:
                    winner = 1

            if winner == 0:
                decks[0].append(top_1)
                decks[0].append(top_2)
            else:
                decks[1].append(top_2)
                decks[1].append(top_1)

    if len(decks[0]) == 0:
        return 1, decks[1]
    else:
        return 0, decks[0]


ww, wwd = game(deck)

tot = 0
num_cards = len(wwd)
for i in range(1, num_cards + 1):
    tot += i * wwd[num_cards - i]
print(tot)
