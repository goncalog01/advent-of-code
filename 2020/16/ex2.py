with open("input.txt", "r") as f:
    lines = [line for line in f.read().splitlines() if line != ""]

fields = {}

i = 0

while lines[i] != "your ticket:":
    fields[lines[i].split(": ")[0]] = (int(lines[i].split(": ")[1].split(" or ")[0].split("-")[0]), int(lines[i].split(": ")[1].split(" or ")[0].split("-")[1]), int(lines[i].split(": ")[1].split(" or ")[1].split("-")[0]), int(lines[i].split(": ")[1].split(" or ")[1].split("-")[1]))
    i += 1

i += 1
my_ticket = [int(x) for x in lines[i].split(",")]
tickets = []

for line in lines[i + 2:]:
    ticket = [int(x) for x in line.split(",")]
    for n in ticket:
        valid = False
        for field in fields:
            if fields[field][0] <= n <= fields[field][1] or fields[field][2] <= n <= fields[field][3]:
                valid = True
                break
        if not valid:
            break
    if valid:
        tickets += [ticket]

possible_fields_all = []

for x in range(len(tickets[0])):
    possible_fields = []
    for field in fields:
        possible_fields += [field]
    for y in range(len(tickets)):
        for field in possible_fields:
            if not (fields[field][0] <= tickets[y][x] <= fields[field][1] or fields[field][2] <= tickets[y][x] <= fields[field][3]):
                possible_fields.remove(field)
    possible_fields_all += [possible_fields]

assigned_fields = ["" for i in range(20)]

for i in range(1, 21):
    for pos in possible_fields_all:
        if len(pos) == i:
            for field in pos:
                if field not in assigned_fields:
                    assigned_fields[possible_fields_all.index(pos)] = field
                    break

res = 1

for i in range(len(assigned_fields)):
    if assigned_fields[i].startswith("departure"):
        res *= my_ticket[i]

print(res)