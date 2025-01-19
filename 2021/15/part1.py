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

map = []
size = len(input)

for i in range(size):
    map += [[int(x) for x in input[i]]]

graph = {}

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