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

part_nums = {}
potential_gears = []
for i in range(len(lines)):
    current_num = ""
    current_positions = []
    for j in range(len(lines[0])):
        if lines[i][j].isdigit():
            current_num += lines[i][j]
            current_positions.append((i, j))
        else:
            if lines[i][j] == "*":
                potential_gears.append((i, j))
            if current_num != "" and number_symbol_adjacent(current_positions, lines):
                if int(current_num) in part_nums:
                    part_nums[int(current_num)].append(current_positions)
                else:
                    part_nums[int(current_num)] = [current_positions]
            current_num = ""
            current_positions = []
    if current_num != "" and number_symbol_adjacent(current_positions, lines):
        if int(current_num) in part_nums:
            part_nums[int(current_num)].append(current_positions)
        else:
            part_nums[int(current_num)] = [current_positions]

total = 0
for gear in potential_gears:
    adjacent_pos = get_adjacent_positions(gear, lines)
    adjacent = 0
    ratio = 1
    for part_num in part_nums:
        for num in part_nums[part_num]:
            for pos in num:
                if pos in adjacent_pos:
                    adjacent += 1
                    ratio *= part_num
                    break
    if adjacent == 2:
        total += ratio

print(total)