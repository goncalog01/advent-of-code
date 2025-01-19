from functools import cache

@cache
def play(p1_pos, p2_pos, p1_score = 0, p2_score = 0, rolls = 0, sum = 0, p1_turn = True):
    p1_wins = 0
    p2_wins = 0

    if p1_turn:
        if rolls < 3:
            for i in range(1, 4):
                next_sum = sum + i
                next_rolls = rolls + 1
                wins = play(p1_pos, p2_pos, p1_score, p2_score, next_rolls, next_sum, p1_turn)
                p1_wins += wins[0]
                p2_wins += wins[1]
        else:
            next_p1_pos = ((p1_pos + sum - 1) % 10) + 1
            next_p1_score = p1_score + next_p1_pos
            if next_p1_score >= 21:
                p1_wins += 1
            else:
                wins = play(next_p1_pos, p2_pos, next_p1_score, p2_score, 0, 0, False)
                p1_wins += wins[0]
                p2_wins += wins[1]
    else:
        if rolls < 3:
            for i in range(1, 4):
                next_sum = sum + i
                next_rolls = rolls + 1
                wins = play(p1_pos, p2_pos, p1_score, p2_score, next_rolls, next_sum, p1_turn)
                p1_wins += wins[0]
                p2_wins += wins[1]
        else:
            next_p2_pos = ((p2_pos + sum - 1) % 10) + 1
            next_p2_score = p2_score + next_p2_pos
            if next_p2_score >= 21:
                p2_wins += 1
            else:
                wins = play(p1_pos, next_p2_pos, p1_score, next_p2_score, 0, 0, True)
                p1_wins += wins[0]
                p2_wins += wins[1]
    return p1_wins, p2_wins

with open("input.txt", "r") as f:
    input = f.read().splitlines()

p1_pos = int(input[0].split(": ")[1])
p2_pos = int(input[1].split(": ")[1])

print(max(play(p1_pos, p2_pos)))