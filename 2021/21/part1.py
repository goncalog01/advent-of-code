with open("input.txt", "r") as f:
    input = f.read().splitlines()

p1_pos = int(input[0].split(": ")[1])
p2_pos = int(input[1].split(": ")[1])

p1_score = 0
p2_score = 0

rolls = 0
next_roll = 1
p1_turn = True

while p1_score < 1000 and p2_score < 1000:
    if p1_turn:
        for _ in range(3):
            p1_pos = ((p1_pos + next_roll - 1) % 10) + 1
            next_roll = (next_roll % 100) + 1
            rolls += 1
        p1_score += p1_pos
        p1_turn = False
    else:
        for _ in range(3):
            p2_pos = ((p2_pos + next_roll - 1) % 10) + 1
            next_roll = (next_roll % 100) + 1
            rolls += 1
        p2_score += p2_pos
        p1_turn = True

print((min(p1_score, p2_score) * rolls))