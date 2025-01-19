def neighbors(i, j):
    return ((i-1, j-1), (i-1, j), (i-1,j+1), (i, j-1), (i, j), (i, j+1), (i+1,j-1), (i+1, j), (i+1, j+1))

def index(s):
    index = ""
    for char in s:
        if char == ".":
            index += "0"
        else:
            index += "1"
    return int(index, 2)

def enhance(image, iter):
    output = [""] * len(image)
    for i in range(len(image)):
        for j in range(len(image[0])):
            s = ""
            for (x, y) in neighbors(i, j):
                if 0 <= x < len(image) and 0 <= y < len(image[0]):
                    s += image[x][y]
                else:
                    if not alternate:
                        s += "."
                    else:
                        if iter % 2 == 0:
                            s += "."
                        else:
                            s += "#"
            output[i] += enhancement[index(s)]
    return output

def expand(image, iter):
    if not alternate:
        new_image = ["." * (len(image[0]) + 2)]
        for i in range(len(image)):
            new_image += ["." + image[i] + "."]
        new_image += ["." * (len(image[0]) + 2)]
    else:
        if iter % 2 == 0:
            new_image = ["." * (len(image[0]) + 2)]
            for i in range(len(image)):
                new_image += ["." + image[i] + "."]
            new_image += ["." * (len(image[0]) + 2)]
        else:
            new_image = ["#" * (len(image[0]) + 2)]
            for i in range(len(image)):
                new_image += ["#" + image[i] + "#"]
            new_image += ["#" * (len(image[0]) + 2)]
    return new_image

with open("input.txt", "r") as f:
    input = f.read().splitlines()

enhancement = input[0]
alternate = False
if enhancement[0] == "#":
    alternate = True
image = input[2:]

for i in range(50):
    image = enhance(expand(image, i), i)

lit_pixels = 0

for line in image:
    lit_pixels += line.count("#")

print(lit_pixels)