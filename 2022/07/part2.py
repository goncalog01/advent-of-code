import math

class Node:
    def __init__(self, name, parent, size, type):
        self.name = name
        self.parent = parent
        self.size = size
        self.type = type
        self.children = dict()

        if type == "file":
            self.parent.addSize(size)

    def addSize(self, size):
        self.size += size

        if self.parent:
            self.parent.addSize(size)

    def getType(self):
        return self.type

    def getSize(self):
        return self.size

    def addChild(self, name, node):
        self.children[name] = node

    def getChild(self, name):
        return self.children[name]

    def getDirChildren(self):
        dirs = []
        for child in self.children.values():
            if child.getType() == "dir":
                dirs.append(child)
        return dirs

class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, path, name, size, type):
        current = self.root
        if path != "/":
            nodes = path[1:].split("/")
            for node in nodes:
                current = current.getChild(node)
        
        new = Node(name, current, size, type)
        current.addChild(name, new)

    def dirToDelete(self):
        dirs = [self.root]
        space_to_delete = 30000000 - (70000000 - self.root.getSize())
        size = math.inf
        while len(dirs) > 0:
            if space_to_delete <= dirs[0].getSize() < size:
                size = dirs[0].getSize()
            dirs.extend(dirs[0].getDirChildren())
            dirs.remove(dirs[0])
        return size

with open("input.txt", "r") as f:
    data = f.read().splitlines()

path = ""
root = Node("/", None, 0, "dir")
tree = Tree(root)

for line in data:
    tokens = line.split(" ")
    if tokens[0] == "$" and tokens[1] == "cd":
        if tokens[2] == "/":
            path = "/"
        elif tokens[2] == "..":
            if path.count("/") == 1:
                path = "/"
            else:
                path = path[:path.rfind("/")]
        else:
            if path != "/":
                path += "/"
            path += tokens[2]
    elif tokens[0] == "dir":
        tree.insert(path, tokens[1], 0, "dir")
    elif tokens[0].isdecimal():
        tree.insert(path, tokens[1], int(tokens[0]), "file")

print(tree.dirToDelete())