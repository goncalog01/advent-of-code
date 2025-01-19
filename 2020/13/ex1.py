f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

dep_time = int(lines[0])
bus_ids = lines[1].split(",")
id = 0
wait_time = dep_time

for bus_id in bus_ids:
    if bus_id == "x":
        continue
    time = int(bus_id)
    this_wait_time = time - (dep_time % time)
    if this_wait_time < wait_time:
        id = time
        wait_time = this_wait_time

print(id * wait_time)