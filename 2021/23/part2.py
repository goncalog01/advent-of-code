def extend(lines):
    return (*lines[:3], (*"  #D#C#B#A#",), (*"  #D#B#A#C#",), *lines[3:],)

def room_size(lines):
    return len(lines) - 3

def char(lines, x, y):
    return lines[y][x]

def stoppable(lines):
    return tuple(i for i in range(1, len(lines[0]) - 1) if i not in rooms.values())

def in_right_room(lines, x, y):
    if not is_amphipod(lines, x, y):
        return False
    if x == rooms[char(lines, x, y)]:
        return True
    return False

def in_room(lines, x, y):
    return y > 1

def room_complete(lines, x):
    for y in range(2, 2 + room_size(lines)):
        if not in_right_room(lines, x, y):
            return False
    return True

def rooms_complete(lines):
    return room_complete(lines, 3) and room_complete(lines, 5) and room_complete(lines, 7) and room_complete(lines, 9)

def is_amphipod(lines, x, y):
    val = char(lines, x, y)
    return val if val in rooms.keys() else False

def is_empty(lines, x, y):
    return char(lines, x, y) == "."

def is_room_empty(lines, x):
    for y in range(2, 2 + room_size(lines)):
        if not is_empty(lines, x, y):
            return False
    return True

def is_blocking_room(lines, x, y):
    for j in range(y + 1, 2 + room_size(lines)):
        if is_amphipod(lines, x, j) and not in_right_room(lines, x, j):
            return True
    return False

def has_room_available(lines, x, y):
    amphipod = char(lines, x, y)
    room = rooms[amphipod]
    if is_room_empty(lines, room):
        return True
    for y in range(2, 2 + room_size(lines)):
        if not is_empty(lines, room, y) and not in_right_room(lines, room, y):
            return False
    return True

def is_path_empty(lines, x, target):
    while x != target:
        if x > target:
            x -= 1
        if x < target:
            x += 1
        if not is_empty(lines, x, 1):
            return False
    return True

def blocked_in_room(lines, x, y):
    if y < 3:
        return False
    return not is_empty(lines, x, y - 1)

def move_in_pos(lines, room):
    for y in range(1 + room_size(lines), 1, -1):
        if is_empty(lines, room, y):
            return y

def can_move(lines, x, y):
    return (not in_right_room(lines, x, y) or is_blocking_room(lines, x, y)) and not blocked_in_room(lines, x, y)

def move_cost(lines, x, y, i, j):
    return ((y - 1) + abs(x - i) + (j - 1)) * type_cost[char(lines, x, y)]

def move(l, x, y, i, j):
    new_lines = (*((*(((char(l, a, b), char(l, x, y))[a==i and b==j], char(l, i, j))[a==x and b==y] for a in range(len(l[b]))),) for b in range(len(l))),)
    return (new_lines, move_cost(l, x, y, i, j))

def check_state(lines):
    cached = cache.get(lines)
    if cached is not None:
        return cached
    if rooms_complete(lines):
        return 0
    costs = []
    for y in range(1, len(lines)):
        for x in range(1, len(lines[y])):
            amphipod = is_amphipod(lines, x, y)
            if not amphipod:
                continue
            if can_move(lines, x, y):
                room = rooms[amphipod]
                if has_room_available(lines, x, y) and is_path_empty(lines, x, room):
                    l, c = move(lines, x, y, room, move_in_pos(lines, room))
                    cost = check_state(l)
                    if cost >= 0:
                        costs.append(c + cost)
                elif in_room(lines, x, y):
                    for i in stoppable(lines):
                        if not is_path_empty(lines, x, i):
                            continue
                        l, c = move(lines, x, y, i, 1)
                        cost = check_state(l)
                        if cost >= 0:
                            costs.append(c + cost)
    res = -1
    if costs:
        res = min(costs)
    cache[lines] = res
    return res

with open("input.txt", "r") as f:
    lines = (*((*line,) for line in f),)

type_cost = { "A": 1, "B": 10, "C": 100, "D": 1000 }
rooms = { "A": 3, "B": 5, "C": 7, "D": 9 }
cache = {}

print(check_state(extend(lines)))