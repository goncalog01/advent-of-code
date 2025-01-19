def paths(source, dest):
    return paths_aux(source, dest, [])

def paths_aux(source, dest, visited):
    paths = []
    new_visited = visited + [source]

    if source == dest:
        return [new_visited]

    for cave in caves[source]:
        if cave != "start":
            if cave[0].isupper():
                paths += paths_aux(cave, dest, new_visited)
            else:
                small_caves = [x for x in new_visited if x[0].islower()]
                visited_twice = False

                for small in small_caves:
                    if small_caves.count(small) > 1:
                        visited_twice = True
                        break
                if (visited_twice and new_visited.count(cave) < 1) or (not visited_twice and new_visited.count(cave) < 2):
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