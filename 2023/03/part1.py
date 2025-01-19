def get_adjacent_positions(position, map):
    adj = []
    
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, len(map))
            rangeY = range(0, len(map[0]))
            
            (newX, newY) = (position[0] + dx, position[1] + dy)
            
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))
    
    return adj

def digit_symbol_adjacent(position, map):
    for (i, j) in get_adjacent_positions(position, map):
        if map[i][j] != "." and not map[i][j].isdigit():
            return True
    return False

def number_symbol_adjacent(positions, map):
    for pos in positions:
        if digit_symbol_adjacent(pos, map):
            return True
    return False

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for i in range(len(lines)):
    current_num = ""
    current_positions = []
    for j in range(len(lines[0])):
        if lines[i][j].isdigit():
            current_num += lines[i][j]
            current_positions.append((i, j))
        else:
            if current_num != "" and number_symbol_adjacent(current_positions, lines):
                total += int(current_num)
            current_num = ""
            current_positions = []
    if current_num != "" and number_symbol_adjacent(current_positions, lines):
        total += int(current_num)

print(total)