f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

dirs = ("N", "E", "S", "W")
dir_val = {dir: 0 for dir in dirs}
curr_dir = dirs[1]

for line in lines:
    action = line[0]
    val = int(line[1:])
    if action == "N" or action == "E" or action == "S" or action == "W":
        dir_val[action] += val
    elif action == "L":
        curr_dir = dirs[(dirs.index(curr_dir) - (val // 90)) % len(dirs)]
    elif action == "R":
        curr_dir = dirs[(dirs.index(curr_dir) + (val // 90)) % len(dirs)]
    else:
        dir_val[curr_dir] += val

print(abs(dir_val["S"] - dir_val["N"]) + abs(dir_val["W"] - dir_val["E"]))