import portion as P

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

almanac = {
    "seeds" : [int(x) for x in lines[0].split(": ")[1].split(" ") if len(x) > 0],
    "seed_soil" : [],
    "soil_fertilizer" : [],
    "fertilizer_water" : [],
    "water_light" : [],
    "light_temperature" : [],
    "temperature_humidity" : [],
    "humidity_location" : []
}

current = "seed_soil"
for line in lines[3:]:
    if line == "soil-to-fertilizer map:":
        current = "soil_fertilizer"
    elif line == "fertilizer-to-water map:":
        current = "fertilizer_water"
    elif line == "water-to-light map:":
        current = "water_light"
    elif line == "light-to-temperature map:":
        current = "light_temperature"
    elif line == "temperature-to-humidity map:":
        current = "temperature_humidity"
    elif line == "humidity-to-location map:":
        current = "humidity_location"
    elif line == "":
        continue
    else:
        almanac[current].append([int(x) for x in line.split(" ") if len(x) > 0])

steps = ["seed_soil", "soil_fertilizer", "fertilizer_water", "water_light", "light_temperature", "temperature_humidity", "humidity_location"]
ranges = []

for i in range(0, len(almanac["seeds"]), 2):
    ranges.append(P.closed(almanac["seeds"][i], almanac["seeds"][i] + almanac["seeds"][i+1] - 1))

for step in steps:
    translation = {}
    for line in almanac[step]:
        translation[P.closed(line[1], line[1] + line[2] - 1)] = P.closed(line[0], line[0] + line[2] - 1)
    almanac[step] = translation

for step in steps:
    next_ranges = []
    while len(ranges) > 0:
        range = ranges.pop()
        for interval in almanac[step]:
            intersection = range & interval
            if not intersection.empty:
                length = intersection.upper - intersection.lower
                diff = intersection.lower - interval.lower
                translation = almanac[step][interval]
                next_ranges.append(P.closed(translation.lower + diff, translation.lower + diff + length))
                if intersection.lower > range.lower:
                    ranges.append(P.closed(range.lower, intersection.lower - 1))
                if intersection.upper < range.upper:
                    ranges.append(P.closed(intersection.upper + 1, range.upper))
                break
        else:
            next_ranges.append(range)
    ranges = next_ranges

min_location = P.inf
for range in ranges:
    if range.left == P.CLOSED and range.lower < min_location:
        min_location = range.lower

print(min_location)