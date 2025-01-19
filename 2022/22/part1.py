def pad_board(board):
    max_len = 0
    for line in board:
        max_len = max(max_len, len(line))
    for i in range(len(board)):
        board[i] += " " * (max_len - len(board[i]))

def parse_path(path):
    path_lst = []
    steps = ""
    for char in path:
        if char.isdigit():
            steps += char
        else:
            path_lst.append(int(steps))
            path_lst.append(char)
            steps = ""
    if steps == "":
        path_lst.append(path[-1])
    else:
        path_lst.append(int(steps))
    return path_lst

def wrap_around(board, x, y, dir):
    new_x = x
    new_y = y
    match dir:
        case "R":
            v = (-1, 0)
        case "D":
            v = (0, -1)
        case "L":
            v = (1, 0)
        case "U":
            v = (0, 1)

    while 0 <= new_x < len(board[0]) and 0 <= new_y < len(board) and board[new_y][new_x] != " ":
        new_x += v[0]
        new_y += v[1]

    new_x -= v[0]
    new_y -= v[1]
    if board[new_y][new_x] == ".":
        return (new_x, new_y)
    else:
        return (x, y)

def move(board, x, y, dir):
    match dir:
        case "R":
            new_x = x + 1
            new_y = y
        case "D":
            new_x = x
            new_y = y + 1
        case "L":
            new_x = x - 1
            new_y = y
        case "U":
            new_x = x
            new_y = y - 1
    if 0 <= new_x < len(board[0]) and 0 <= new_y < len(board):
        if board[new_y][new_x] == ".":
            return (new_x, new_y)
        elif board[new_y][new_x] == "#":
            return (x, y)
        else:
            return wrap_around(board, x, y, dir)
    else:
        return wrap_around(board, x, y, dir)

with open("input.txt", "r") as f:
    data = f.read().splitlines()

board = data[:-2]
pad_board(board)
path = parse_path(data[-1])

dirs = { "R" : 0, "D" : 1, "L" : 2, "U" : 3 }
turn = {
    "R" : {
        "R" : "D",
        "L" : "U"
    },
    "D" : {
        "R" : "L",
        "L" : "R"
    },
    "L" : {
        "R" : "U",
        "L" : "D"
    },
    "U" : {
        "R" : "R",
        "L" : "L"
    }
}
facing = "R"
x = board[0].index(".")
y = 0

for instr in path:
    if isinstance(instr, int):
        for _ in range(instr):
            x, y = move(board, x, y, facing)
    else:
        facing = turn[facing][instr]

print(1000 * (y + 1) + 4 * (x + 1) + dirs[facing])