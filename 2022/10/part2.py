def draw_pixel(x, pixel):
    if x - 1 <= pixel % 40 <= x + 1:
        s = "#"
    else:
        s = "."

    if pixel % 40 == 39:
        s += "\n"

    return s

with open("input.txt", "r") as f:
    program = f.read().splitlines()

x = 1
pixel = 0
image = ""

for line in program:
    instr = line.split(" ")
    if instr[0] == "noop":
        image += draw_pixel(x, pixel)
        pixel += 1
    else:
        image += draw_pixel(x, pixel)
        pixel += 1
        image += draw_pixel(x, pixel)
        pixel += 1
        x += int(instr[1])

print(image)