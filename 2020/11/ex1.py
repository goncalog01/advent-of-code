f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

prev = []
new = lines.copy()
num_lines = len(lines)
num_cols = len(lines[0])

while prev != new:
    prev = new.copy()
    new = []
    for line in range(num_lines):
        new_line = []
        for col in range(num_cols):
            seat = prev[line][col]
            if seat != ".":
                adj = ((col-1, line-1), (col, line-1), (col+1, line-1), (col-1, line), (col+1, line), (col-1, line+1), (col, line+1), (col+1, line+1))
                adj_occ = 0
                for (x, y) in adj:
                    if 0 <= x < num_cols and 0 <= y < num_lines and prev[y][x] == "#":
                        adj_occ += 1
                if seat == "L" and adj_occ == 0:
                    seat = "#"
                elif seat == "#" and adj_occ >= 4:
                    seat = "L"
            new_line += [seat]
        new += [new_line]

print(sum(line.count('#') for line in new))