def paths(source, dest):
    return paths_aux(source, dest, [])

def paths_aux(source, dest, visited):
    paths = []
    new_visited = visited + [source]

    if source == dest:
        return [new_visited]

    for cave in caves[source]:
        if cave not in visited or cave[0].isupper():
                paths += paths_aux(cave, dest, new_visited)
    return paths

with open("input.txt", "r") as f:
    map = f.read().splitlines()

caves = {}

for connection in map:
    p1, p2 = connection.split("-")

    if p1 not in caves:
        caves[p1] = [p2]
    else:
        caves[p1] += [p2]

    if p2 not in caves:
        caves[p2] = [p1]
    else:
        caves[p2] += [p1]

print(len(paths("start", "end")))