import math
import heapq

def dijkstra(source):
    distances = {v: math.inf for v in graph}
    distances[source] = 0

    queue = [(0, source)]
    while len(queue) > 0:
        curr_dist, curr_vert = heapq.heappop(queue)

        if curr_dist > distances[curr_vert]:
            continue

        for neighbor, weight in graph[curr_vert].items():
            dist = curr_dist + weight

            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(queue, (dist, neighbor))

    return distances[(size**2) - 1]

with open("input.txt", "r") as f:
    input = f.read().splitlines()

size = len(input)

map = [[0 for i in range(size * 5)] for i in range(size * 5)]

for i in range(size):
    for j in range(size):
        map[i][j] = int(input[i][j])

for i in range(size):
    for j in range(size):
        for k in range(1, 5):
            if map[i][j+(size*(k-1))] == 9:
                map[i][j+(size*k)] = 1
            else:
                map[i][j+(size*k)] = map[i][j+(size*(k-1))] + 1

for i in range(size):
    for j in range(size*5):
        for k in range(1, 5):
            if map[i+(size*(k-1))][j] == 9:
                map[i+(size*k)][j] = 1
            else:
                map[i+(size*k)][j] = map[i+(size*(k-1))][j] + 1

graph = {}
size *= 5
k = 0

for i in range(size):
    for j in range(size):
        graph[k] = {}
        if i > 0:
            graph[k][k-size] = map[i-1][j]
        if j > 0:
            graph[k][k-1] = map[i][j-1]
        if j < size - 1:
            graph[k][k+1] = map[i][j+1]
        if i < size - 1:
            graph[k][k+size] = map[i+1][j]
        k += 1

print(dijkstra(0))