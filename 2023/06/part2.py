with open("input.txt", "r") as f:
    lines = f.read().splitlines()

n = ""
for char in lines[0]:
    if char.isdigit():
        n += char
time = int(n)
n = ""
for char in lines[1]:
    if char.isdigit():
        n += char
distance = int(n)

wins = 0
for n in range(time // 2, -1, -1):
    if n * (time - n) > distance:
        wins += 1
    else:
        break
if time % 2 == 0:
    wins = (wins - 1) * 2 + 1
else:
    wins *= 2

print(wins)
