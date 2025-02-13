import math
from collections import Counter

transforms = [
  lambda a: [ a[0],  a[1],  a[2]],
  lambda a: [ a[1],  a[2],  a[0]],
  lambda a: [ a[2],  a[0],  a[1]],
  lambda a: [-a[0],  a[2],  a[1]],
  lambda a: [ a[2],  a[1], -a[0]],
  lambda a: [ a[1], -a[0],  a[2]],
  lambda a: [ a[0],  a[2], -a[1]],
  lambda a: [ a[2], -a[1],  a[0]],
  lambda a: [-a[1],  a[0],  a[2]],
  lambda a: [ a[0], -a[2],  a[1]],
  lambda a: [-a[2],  a[1],  a[0]],
  lambda a: [ a[1],  a[0], -a[2]],
  lambda a: [-a[0], -a[1],  a[2]],
  lambda a: [-a[1],  a[2], -a[0]],
  lambda a: [ a[2], -a[0], -a[1]],
  lambda a: [-a[0],  a[1], -a[2]],
  lambda a: [ a[1], -a[2], -a[0]],
  lambda a: [-a[2], -a[0],  a[1]],
  lambda a: [ a[0], -a[1], -a[2]],
  lambda a: [-a[1], -a[2],  a[0]],
  lambda a: [-a[2],  a[0], -a[1]],
  lambda a: [-a[0], -a[2], -a[1]],
  lambda a: [-a[2], -a[1], -a[0]],
  lambda a: [-a[1], -a[0], -a[2]],
]

def vlen(a):
    return int(math.sqrt(sum([i * i for i in a])))

def dist(a, b):
    return vlen([abs(i - j) for i, j in zip(*[a, b])])

def pathdist(a, b):
    return str([abs(i - j) for i, j in zip(*[a, b])])

def distset(b):
    output = set()
    for i in b:
        for j in b:
            output.add(dist(i, j))
        output.remove(0)
    return output

def pathdistlist(a, b):
    output = list()
    for i in a:
        for j in b:
            output.append(pathdist(i, j))
    return output

def process(content):
    beacons = []
    for scan in content:
        beacons.append([list(map(int, l.split(','))) for l in scan.splitlines()[1:]])

    field = beacons[0].copy()
    transformed_beacons = {0: beacons[0].copy()}

    while len(transformed_beacons) < len(beacons):
        comparisons = transformed_beacons.copy().keys()
        for scan in range(1, len(beacons)):
            if scan in transformed_beacons.keys():
                continue
            eligible = False
            for compar in comparisons:
                fielddist = distset(transformed_beacons[compar])
                bdist = distset(beacons[scan])
                if len(bdist.intersection(fielddist)) >= 11:
                    tdistances = []
                    maxes = []
                    for tdx in range(0, len(transforms)):
                        tbeacons = [transforms[tdx](p) for p in beacons[scan]]
                        pd = Counter(pathdistlist(tbeacons, transformed_beacons[compar]))
                        maxes.append([tdx, max(pd.values())])
                    maxes.sort(key=(lambda a: a[1]))
                    if len(maxes) and len([m for m in maxes if m[1] >= 12]):
                        maxes = [m for m in maxes if m[1] == maxes[-1][1]]
                        tbeacons = [transforms[maxes[-1][0]](p) for p in beacons[scan]]
                        if not eligible:
                            transformed_beacons[scan] = tbeacons.copy()
                            eligible = True
                            pd = Counter(pathdistlist(tbeacons, transformed_beacons[compar]))
                            commondist = pd.most_common(1)[0][0]
                            offset = None
                            for i in transformed_beacons[compar]:
                                for j in tbeacons:
                                    if pathdist(i, j) == commondist:
                                        offset = [
                                            i[0] - j[0],
                                            i[1] - j[1],
                                            i[2] - j[2]
                                        ]
                                        break
                                if offset:
                                    continue
                            for j in tbeacons:
                                j[0] += offset[0]
                                j[1] += offset[1]
                                j[2] += offset[2]
                                field.append(j)
                if eligible:
                    break

    field = [list(i) for i in set(map(tuple, field))]
    return len(field)

with open("input.txt", "r") as f:
    input = f.read().split("\n\n")

print(process(input))