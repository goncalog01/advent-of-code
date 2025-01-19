from queue import PriorityQueue
import math

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]

    def add_edge(self, u, v):
        self.edges[u][v] = 1

def dijkstra(graph, start_vertex):
    D = { v : math.inf for v in range(graph.v) }
    D[start_vertex] = 0
    visited = []

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

def index_to_num(i, j, len_line):
    return len_line * j + i

def height(letter):
    if letter == "S":
        l = "a"
    elif letter == "E":
        l = "z"
    else:
        l = letter

    return ord(l) - ord("a")

def get_neighbors(heightmap, i, j):
    neighbors = []
    if i > 0 and height(heightmap[j][i-1]) - height(heightmap[j][i]) <= 1:
        neighbors.append(index_to_num(i-1, j, len(heightmap[0])))
    if i < len(heightmap[0]) - 1 and height(heightmap[j][i+1]) - height(heightmap[j][i]) <= 1:
        neighbors.append(index_to_num(i+1, j, len(heightmap[0])))
    if j > 0 and height(heightmap[j-1][i]) - height(heightmap[j][i]) <= 1:
        neighbors.append(index_to_num(i, j-1, len(heightmap[0])))
    if j < len(heightmap) - 1 and height(heightmap[j+1][i]) - height(heightmap[j][i]) <= 1:
        neighbors.append(index_to_num(i, j+1, len(heightmap[0])))
    return neighbors

with open("input.txt", "r") as f:
    heightmap = f.read().splitlines()

graph = Graph(len(heightmap) * len(heightmap[0]))

for j in range(len(heightmap)):
    for i in range(len(heightmap[0])):
        curr = index_to_num(i, j, len(heightmap[0]))
        if heightmap[j][i] == "S":
            start = curr
        elif heightmap[j][i] == "E":
            end = curr
        for n in get_neighbors(heightmap, i, j):
            graph.add_edge(curr, n)

print(dijkstra(graph, start)[end])