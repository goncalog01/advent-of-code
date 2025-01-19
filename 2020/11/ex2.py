def occupied(seats, current_line, current_col, line_offset, col_offset):
    num_lines = len(seats)
    num_cols = len(seats[0])
    current_line += line_offset
    current_col += col_offset
    while 0 <= current_line < num_lines and 0 <= current_col < num_cols and seats[current_line][current_col] == ".":
        current_line += line_offset
        current_col += col_offset
    if not (0 <= current_line < num_lines and 0 <= current_col < num_cols) or seats[current_line][current_col] == "L":
        return False
    elif seats[current_line][current_col] == "#":
        return True

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
                adj = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
                adj_occ = 0
                for (x, y) in adj:
                    if occupied(prev, line, col, x, y):
                        adj_occ += 1
                if seat == "L" and adj_occ == 0:
                    seat = "#"
                elif seat == "#" and adj_occ >= 5:
                    seat = "L"
            new_line += [seat]
        new += [new_line]

print(sum(line.count('#') for line in new))