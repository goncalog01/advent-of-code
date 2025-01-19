with open("input.txt", "r") as f:
    rounds = f.read().splitlines()

result = {
    "A" : {
        "X" : 4,
        "Y" : 8,
        "Z" : 3
    },
    "B" : {
        "X" : 1,
        "Y" : 5,
        "Z" : 9
    },
    "C" : {
        "X" : 7,
        "Y" : 2,
        "Z" : 6
    }
}

score = 0

for round in rounds:
    score += result[round[0]][round[2]]

print(score)