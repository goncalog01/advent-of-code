def readData(inpath):
    with open(inpath, 'r') as infile:
        rawRules, rawStrings = infile.read().split("\n\n")
        return parseRules(rawRules), rawStrings.split("\n")

def parseRules(rawRules):
    rules = {}
    for line in rawRules.split('\n'):
        k, rule = line.split(': ')
        if rule[0] == '"':
            rule = rule[1:-1]
        else:
            rule = [seq.split(' ') if ' ' in seq else [seq]
                    for seq in (rule.split(' | ') if ' | ' in rule else [rule])]
        rules[k] = rule
    return rules

def checkSequence(grammar, seq, string):
    if not seq:
        yield string
    else:
        index, *seq = seq
        for string in run(grammar, index, string):
            yield from checkSequence(grammar, seq, string)

def runExpand(grammar, alt, string):
    for seq in alt:
        yield from checkSequence(grammar, seq, string)

def run(grammar, index, string):
    if isinstance(grammar[index], list):
        yield from runExpand(grammar, grammar[index], string)
    else:
        if string and string[0] == grammar[index]:
            yield string[1:]

def match(grammar, string):
    return any(m == '' for m in run(grammar, '0', string))

rules, strings = readData("input.txt")
print(sum(match(rules, s) for s in strings))