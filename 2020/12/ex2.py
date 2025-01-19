f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

def rotL(hor_val, vert_val, times):
    new_dir = {"vert": vert_val, "hor": hor_val}
    while times > 0:
        aux = new_dir["vert"] * -1
        new_dir["vert"] = new_dir["hor"]
        new_dir["hor"] = aux
        times -= 1
    return new_dir

def rotR(hor_val, vert_val, times):
    new_dir = {"vert": vert_val, "hor": hor_val}
    while times > 0:
        aux = new_dir["hor"] * -1
        new_dir["hor"] = new_dir["vert"]
        new_dir["vert"] = aux
        times -= 1
    return new_dir

curr_dir = {"vert": 1, "hor": 10}
ship = {"vert": 0, "hor": 0}

for line in lines:
    action = line[0]
    val = int(line[1:])
    if action == "N":
        curr_dir["vert"] += val
    elif action == "S":
        curr_dir["vert"] -= val
    elif action == "E":
        curr_dir["hor"] += val
    elif action == "W":
        curr_dir["hor"] -= val
    elif action == "L":
        curr_dir = rotL(curr_dir["hor"], curr_dir["vert"], val // 90)
    elif action == "R":
        curr_dir = rotR(curr_dir["hor"], curr_dir["vert"], val // 90)
    else:
        ship["vert"] += curr_dir["vert"] * val
        ship["hor"] += curr_dir["hor"] * val

print(abs(ship["vert"]) + abs(ship["hor"]))