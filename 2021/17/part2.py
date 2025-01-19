def step(x, y, vel_x, vel_y):
    x += vel_x
    y += vel_y
    if vel_x > 0:
        vel_x -= 1
    elif vel_x < 0:
        vel_x += 1
    vel_y -= 1
    return x, y, vel_x, vel_y

def run_steps(vel_x, vel_y):
    x, y = 0, 0
    while y >= target["y"][0]:
        x, y, vel_x, vel_y = step(x, y, vel_x, vel_y)
        if target["x"][0] <= x <= target["x"][1] and target["y"][0] <= y <= target["y"][1]:
            return True
    return False

with open("input.txt", "r") as f:
    input = f.read()

_, a, b = input.split("=")
target = {}
target["x"] = [int(a.split("..")[0]), int(a.split("..")[1].split(",")[0])]
target["y"] = [int(x) for x in b.split("..")]

hits = 0
for i in range(target["x"][1] + 1):
    for j in range(target["y"][0], -target["y"][0]):
        if run_steps(i, j):
            hits += 1
print(hits)