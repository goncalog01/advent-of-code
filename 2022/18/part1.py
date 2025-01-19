def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))

with open("input.txt", "r") as f:
    data = f.read().splitlines()

cubes = [[int(x) for x in data[i].split(",")] for i in range(len(data))]
exposed = [6 for _ in cubes]
for i in range(len(cubes)):
    for j in range(i + 1, len(cubes)):
        if manhattan(cubes[i], cubes[j]) == 1:
            exposed[i] -= 1
            exposed[j] -= 1
print(sum(exposed))