with open("input.txt", "r") as f:
    lines = f.read().splitlines()

player1_deck = []
player2_deck = []

for i in range(1, len(lines)):
    if lines[i] == "":
        break
    else:
        player1_deck += [int(lines[i])]

i += 2

for i in range(i, len(lines)):
    player2_deck += [int(lines[i])]

while len(player1_deck) > 0 and len(player2_deck) > 0:
    if player1_deck[0] > player2_deck[0]:
        player1_deck += [player1_deck[0], player2_deck[0]]
        player1_deck.remove(player1_deck[0])
        player2_deck.remove(player2_deck[0])
    else:
        player2_deck += [player2_deck[0], player1_deck[0]]
        player1_deck.remove(player1_deck[0])
        player2_deck.remove(player2_deck[0])

if len(player1_deck) > 0:
    winner = player1_deck
else:
    winner = player2_deck

score = 0

for i in range(len(winner), 0, -1):
    score += winner[len(winner) - i] * i

print(score)