with open("input.txt", "r") as f:
    rounds = f.read().splitlines()

result = {
    "A" : {
        "X" : 3,
        "Y" : 4,
        "Z" : 8
    },
    "B" : {
        "X" : 1,
        "Y" : 5,
        "Z" : 9
    },
    "C" : {
        "X" : 2,
        "Y" : 6,
        "Z" : 7
    }
}

score = 0

for round in rounds:
    score += result[round[0]][round[2]]

print(score)