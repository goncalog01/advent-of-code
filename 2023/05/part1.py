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
locations = []

for seed in almanac["seeds"]:
    current = seed
    for step in steps:
        for line in almanac[step]:
            if line[1] <= current <= line[1] + line[2] - 1:
                current = line[0] + current - line[1]
                break
    locations.append(current)

print(min(locations))

