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
    faces = {
        1 : {
            "x_range" : (100, 149),
            "y_range" : (0, 49)
        },
        2 : {
            "x_range" : (50, 99),
            "y_range" : (0, 49)
        },
        3 : {
            "x_range" : (50, 99),
            "y_range" : (50, 99)
        },
        4 : {
            "x_range" : (50, 99),
            "y_range" : (100, 149)
        },
        5 : {
            "x_range" : (0, 49),
            "y_range" : (100, 149)
        },
        6 : {
            "x_range" : (0, 49),
            "y_range" : (150, 199)
        }
    }
    wrap_to = {
        1 : {
            "U" : (6, "D"),
            "R" : (4, "R"),
            "D" : (3, "R")
        },
        2 : {
            "U" : (6, "L"),
            "L" : (5, "L")
        },
        3 : {
            "L" : (5, "U"),
            "R" : (1, "D")
        },
        4 : {
            "R" : (1, "R"),
            "D" : (6, "R")
        },
        5 : {
            "U" : (3, "L"),
            "L" : (2, "L")
        },
        6 : {
            "L" : (2, "U"),
            "R" : (4, "D"),
            "D" : (1, "U")
        }
    }
    for face in faces:
        if x in range(faces[face]["x_range"][0], faces[face]["x_range"][1] + 1) and y in range(faces[face]["y_range"][0], faces[face]["y_range"][1] + 1):
            curr_face = face
            break
    to_face = wrap_to[curr_face][dir]
    match to_face[0]:
        case 1:
            if to_face[1] == "U":
                if board[0][100 + x] == ".":
                    return (100 + x, 0, "D")
                else:
                    return (x, y, dir)
            elif to_face[1] == "R":
                if board[49 - (y - 100)][149] == ".":
                    return (149, 49 - (y - 100), "L")
                else:
                    return (x, y, dir)
            elif to_face[1] == "D":
                if board[49][100 + (y - 50)] == ".":
                    return (100 + (y - 50), 49, "U")
                else:
                    return (x, y, dir)
        case 2:
            if to_face[1] == "U":
                if board[0][50 + (y - 150)] == ".":
                    return (50 + (y - 150), 0, "D")
                else:
                    return (x, y, dir)
            elif to_face[1] == "L":
                if board[49 - (y - 100)][50] == ".":
                    return (50, 49 - (y - 100), "R")
                else:
                    return (x, y, dir)
        case 3:
            if to_face[1] == "L":
                if board[50 + x][50] == ".":
                    return (50, 50 + x, "R")
                else:
                    return (x, y, dir)
            elif to_face[1] == "R":
                if board[50 + (x - 100)][99] == ".":
                    return (99, 50 + (x - 100), "L")
                else:
                    return (x, y, dir)
        case 4:
            if to_face[1] == "R":
                if board[49 - (y - 100)][99] == ".":
                    return (99, 49 - (y - 100), "L")
                else:
                    return (x, y, dir)
            elif to_face[1] == "D":
                if board[149][50 + (y - 150)] == ".":
                    return (50 + (y - 150), 149, "U")
                else:
                    return (x, y, dir)
        case 5:
            if to_face[1] == "U":
                if board[100][y - 50] == ".":
                    return (y - 50, 100, "D")
                else:
                    return (x, y, dir)
            elif to_face[1] == "L":
                if board[149 - y][0] == ".":
                    return (0, 149 - y, "R")
                else:
                    return (x, y, dir)
        case 6:
            if to_face[1] == "L":
                if board[150 + (x - 50)][0] == ".":
                    return (0, 150 + (x - 50), "R")
                else:
                    return (x, y, dir)
            elif to_face[1] == "R":
                if board[150 + (x - 50)][49] == ".":
                    return (49, 150 + (x - 50), "L")
                else:
                    return (x, y, dir)
            elif to_face[1] == "D":
                if board[199][x - 100] == ".":
                    return (x - 100, 199, "U")
                else:
                    return (x, y, dir)

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
            return (new_x, new_y, dir)
        elif board[new_y][new_x] == "#":
            return (x, y, dir)
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
            x, y, facing = move(board, x, y, facing)
    else:
        facing = turn[facing][instr]

print(1000 * (y + 1) + 4 * (x + 1) + dirs[facing])