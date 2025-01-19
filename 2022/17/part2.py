from math import gcd

from copy import deepcopy

class Rock:
    def __init__(self, num, bottom, left = 3):
        match num % 5:
            case 0: # horizontal
                self.tiles = [[left, bottom], [left+1, bottom], [left+2, bottom], [left+3, bottom]]
                self.top = bottom
                self.left = left
                self.right = left + 3
                self.bottom = bottom
            case 1: # plus
                self.tiles = [[left, bottom+1], [left+1, bottom], [left+1, bottom+1], [left+1, bottom+2], [left+2, bottom+1]]
                self.top = bottom + 2
                self.left = left
                self.right = left + 2
                self.bottom = bottom
            case 2: # inverted 'L'
                self.tiles = [[left, bottom], [left+1, bottom], [left+2, bottom], [left+2, bottom+1], [left+2, bottom+2]]
                self.top = bottom + 2
                self.left = left
                self.right = left + 2
                self.bottom = bottom
            case 3: # vertical
                self.tiles = [[left, bottom], [left, bottom+1], [left, bottom+2], [left, bottom+3]]
                self.top = bottom + 3
                self.left = left
                self.right = left
                self.bottom = bottom
            case 4: # square
                self.tiles = [[left, bottom], [left, bottom+1], [left+1, bottom], [left+1, bottom+1]]
                self.top = bottom + 1
                self.left = left
                self.right = left + 1
                self.bottom = bottom

    def get_tiles(self):
        return self.tiles

    def get_top(self):
        return self.top

    def fall(self, dir, rocks):
        match dir:
            case '<':
                if self.left > 1:
                    new_tiles = deepcopy(self.tiles)
                    for tile in new_tiles:
                        tile[0] -= 1
                    if not any(tile in new_tiles for tile in rocks):
                        self.tiles = deepcopy(new_tiles)
                        self.left -= 1
                        self.right -= 1
            case '>':
                if self.right < 7:
                    new_tiles = deepcopy(self.tiles)
                    for tile in new_tiles:
                        tile[0] += 1
                    if not any(tile in new_tiles for tile in rocks):
                        self.tiles = deepcopy(new_tiles)
                        self.left += 1
                        self.right += 1
        if self.bottom > 1:
            new_tiles = deepcopy(self.tiles)
            for tile in new_tiles:
                tile[1] -= 1
            if not any(tile in new_tiles for tile in rocks):
                self.tiles = deepcopy(new_tiles)
                self.top -= 1
                self.bottom -= 1
                return True
            else:
                return False
        else:
            return False

def lcm(numbers):
    lcm = 1
    for n in numbers:
        lcm = lcm * n // gcd(lcm, n)
    return lcm

with open("input.txt", "r") as f:
    pattern = f.read()

total = 0
l = len(pattern)
modulo = lcm([l, 5])
times = 1000000000000 // modulo
rocks = []
top = 0
j = -1
for i in range(modulo):
    rock = Rock(i, top + 4)
    while True:
        j += 1
        if not rock.fall(pattern[j%l], rocks):
            break
    rocks.extend(rock.get_tiles())
    top = max(top, rock.get_top())
total += top
top = 0
j = -1
for i in range(modulo):
    rock = Rock(i, top + 4)
    while True:
        j += 1
        if not rock.fall(pattern[j%l], rocks):
            break
    rocks.extend(rock.get_tiles())
    top = max(top, rock.get_top())
total += (times - 1) * top
print(total)