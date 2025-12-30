with open("input.txt", "r") as f:
    input = f.read().splitlines()

def number_paths(graph, start, end):
    def count_paths(current):
        if current == end:
            return 1
        
        count = 0
        for neighbor in graph[current]:
            count += count_paths(neighbor)

        return count
    
    return count_paths(start)

graph = dict()
for line in input:
    node, neighbors = line.split(": ")
    graph[node] = neighbors.split(" ")

print(number_paths(graph, "you", "out"))