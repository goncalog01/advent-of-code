def iter_literal(packet, i):
    version = int(packet[i:i+3], 2)
    i += 3
    type = int(packet[i:i+3], 2)
    i += 3
    while packet[i] == "1":
        i += 5
    i += 5
    yield (version, type, i)

def iter_op_id0(packet, i):
    version = int(packet[i:i+3], 2)
    i += 3
    type = int(packet[i:i+3], 2)
    i += 4
    length = int(packet[i:i+15], 2)
    i += 15
    yield (version, type, i)

    j = i + length
    while i < j:
        for (version, type, i) in iter(packet, i):
            yield (version, type, i)

def iter_op_id1(packet, i):
    version = int(packet[i:i+3], 2)
    i += 3
    type = int(packet[i:i+3], 2)
    i += 4
    num_packets = int(packet[i:i+11], 2)
    i += 11
    yield (version, type, i)

    counter = 0
    while counter < num_packets:
        for (version, type, i) in iter(packet, i):
            yield (version, type, i)
        counter += 1

def iter(packet, i):
    version = int(packet[i:i+3], 2)
    type = int(packet[i+3:i+6], 2)

    if type == 4:
        yield from iter_literal(packet, i)
    else:
        if packet[i+6] == "1":
            yield from iter_op_id1(packet, i)
        else:
            yield from iter_op_id0(packet, i)

with open("input.txt") as f:
    packet = f.read()

hex_to_bin = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111",
}

for char in hex_to_bin:
    packet = packet.replace(char, hex_to_bin[char])

print(sum(v for (v, _, _) in iter(packet, 0)))