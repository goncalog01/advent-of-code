def check_winner(board):
    for row in board:
        winner_row = True
        for n in row:
            if n[1] == False:
                winner_row = False
                break
        if winner_row:
            return True

    for i in range(5):
        winner_col = True
        for j in range(5):
            if board[j][i][1] == False:
                winner_col = False
                break
        if winner_col:
            return True

    return False


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

numbers = [int(x) for x in lines[0].split(",")]

boards = []
board = []

for line in lines[2:]:
    if line == "":
        boards += [board]
        board = []
        continue
    board += [[[int(x), False] for x in line.replace("  ", " ").strip().split(" ")]]

boards += [board]

found_winner = False

for number in numbers:
    for board in boards:
        found_number = False
        for row in board:
            for i in range(5):
                if row[i][0] == number:
                    row[i][1] = True
                    found_number = True
                    if check_winner(board):
                        winner = board
                        last_num = number
                        found_winner = True
                if found_number:
                    break
            if found_number:
                break
        if found_winner:
            break
    if found_winner:
            break

sum = 0

for row in winner:
    for n in row:
        if n[1] == False:
            sum += n[0]

print(sum * last_num)