with open("input.txt", "r") as f:
    input = f.read().splitlines()

def bfs(machine):
    lights, buttons = machine
    queue = [[set(), 0]]
    visited = [set()]
    while len(queue) > 0:
        current, steps = queue.pop(0)
        if current == lights:
            return steps
        for button in buttons:
            next = current.copy()
            for n in button:
                if n in current:
                    next.remove(n)
                else:
                    next.add(n)
            if next not in visited:
                visited.append(next)
                queue.append([next, steps + 1])

machines = []
for line in input:
    info = line.split(" ")
    lights = set()
    for i, c in enumerate(info[0][1:-1]):
        if c == "#":
            lights.add(i)
    buttons = [list(map(int, x[1:-1].split(","))) for x in info[1:-1]]
    machines.append([lights, buttons])

print(sum(bfs(m) for m in machines))