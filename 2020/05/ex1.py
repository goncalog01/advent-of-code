f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

max_seat_id = 0

for line in lines:
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    for char in line:
        if char == "F":
            max_row = (max_row - min_row) // 2 + min_row
        elif char == "B":
            min_row = (max_row - min_row) // 2 + min_row + 1
        elif char == "L":
            max_col = (max_col - min_col) // 2 + min_col
        elif char == "R":
            min_col = (max_col - min_col) // 2 + min_col + 1
    seat_id = max_row * 8 + max_col
    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)