def get_operands_id0(packet, i):
    i += 7
    length = int(packet[i:i+15], 2)
    i += 15
    j = i + length
    vals = []
    while i < j:
        val, i = calc(packet, i)
        vals.append(val)
    return (vals, i)

def get_operands_id1(packet, i):
    i += 7
    num_packets = int(packet[i:i+11], 2)
    i += 11
    counter = 0
    vals = []
    while counter < num_packets:
        val, i = calc(packet, i)
        vals.append(val)
        counter += 1
    return (vals, i)

def op_sum(packet, i):
    operands, i = operand_collectors[int(packet[i+6], 2)](packet, i)
    return sum(operands), i

def op_prod(packet, i):
    operands, i = operand_collectors[int(packet[i+6], 2)](packet, i)
    prod = 1
    for val in operands:
        prod *= val
    return prod, i

def op_min(packet, i):
    operands, i = operand_collectors[int(packet[i+6], 2)](packet, i)
    return min(operands), i

def op_max(packet, i):
    operands, i = operand_collectors[int(packet[i+6], 2)](packet, i)
    return max(operands), i

def literal(packet, i):
    i += 6
    val = ""
    while packet[i] == "1":
        val += packet[i+1:i+5]
        i += 5
    val += packet[i+1:i+5]
    i += 5
    return int(val, 2), i

def op_gt(packet, i):
    operands, i = operand_collectors[int(packet[i+6], 2)](packet, i)
    a, b = operands
    return a > b, i

def op_lt(packet, i):
    operands, i = operand_collectors[int(packet[i+6], 2)](packet, i)
    a, b = operands
    return a < b, i

def op_eq(packet, i):
    operands, i = operand_collectors[int(packet[i+6], 2)](packet, i)
    a, b = operands
    return a == b, i

def calc(packet, i):
    type = int(packet[i+3:i+6], 2)
    return operations[type](packet, i)

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

operand_collectors = [get_operands_id0, get_operands_id1]
operations = [op_sum, op_prod, op_min, op_max, literal, op_gt, op_lt, op_eq]

print(calc(packet, 0)[0])