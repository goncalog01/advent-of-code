with open("input.txt", "r") as f:
    input = f.read().splitlines()

octopuses = []

for line in input:
    octopuses += [[int(x) for x in line]]

total_flashes = 0

for _ in range(100):
    flashes = []

    for i in range(10):
        for j in range(10):
            octopuses[i][j] += 1
            if octopuses[i][j] > 9:
                total_flashes += 1
                flashes += [(i, j)]

    k = 0

    while k < len(flashes):
        i = flashes[k][0]
        j = flashes[k][1]

        for pos in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
            if 0 <= pos[0] < 10 and 0 <= pos[1] < 10:
                octopuses[pos[0]][pos[1]] += 1
                if octopuses[pos[0]][pos[1]] > 9 and (pos[0], pos[1]) not in flashes:
                    total_flashes += 1
                    flashes += [(pos[0], pos[1])]

        k += 1

    for pos in flashes:
        octopuses[pos[0]][pos[1]] = 0

print(total_flashes)