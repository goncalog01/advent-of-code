def play_game(player1, player2):
    configurations = ()
    while len(player1) > 0 and len(player2) > 0:
        if (player1, player2) in configurations:
            return 1, player1
        else:
            configurations += ((player1.copy(), player2.copy()),)
            player1_card = player1[0]
            player2_card = player2[0]
            if player1_card < len(player1) and player2_card < len(player2):
                if play_game(player1[1:player1_card + 1], player2[1:player2_card + 1])[0] == 1:
                    player1 += [player1_card, player2_card]
                    player1.remove(player1_card)
                    player2.remove(player2_card)
                else:
                    player2 += [player2_card, player1_card]
                    player1.remove(player1_card)
                    player2.remove(player2_card)
            else:
                if player1_card > player2_card:
                    player1 += [player1_card, player2_card]
                    player1.remove(player1_card)
                    player2.remove(player2_card)
                else:
                    player2 += [player2_card, player1_card]
                    player1.remove(player1_card)
                    player2.remove(player2_card)
    if len(player1) > 0:
        return 1, player1
    else:
        return 2, player2

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

winner_deck = play_game(player1_deck, player2_deck)[1]

score = 0

for i in range(len(winner_deck), 0, -1):
    score += winner_deck[len(winner_deck) - i] * i

print(score)