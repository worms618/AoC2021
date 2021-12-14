# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day14.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---

def getTemplateAndRules(lines):
    template = lines[0]
    rules = createRules(lines[2:])

    return (template, rules)

def createRules(lines):
    rules = dict()

    for line in lines:
        # print(line)
        [pair, element] = line.split(' -> ')
        rules.setdefault(pair, element)

    return rules

def applyInsertionRules(polymer, newPartPerRule):
    newPolymer = polymer[0]
    print('start - getPolymerPairs')
    [pairs, total] = getPolymerPairs(polymer)
    print('end - getPolymerPairs')
    # print(total, pairs)

    for i in range(total):
        for pair in pairs:
            pairIndices = pairs[pair]
            if i in pairIndices:
                newPart = newPartPerRule[pair]
                newPolymer += newPart[1:]
                break
    print('end - create new polymer')

    return newPolymer

def getPolymerPairs(polymer):
    pairs = dict()
    totalPairs = 0

    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        if not (pair in pairs):
            pairs.setdefault(pair, [])
        pairs[pair].append(i)
        totalPairs += 1

    return (pairs, totalPairs)

def createNewPartPerRule(rules):
    newPartPerRule = dict()

    for rule in rules:
        newPart = rule[0]+rules[rule]+rule[1]
        newPartPerRule.setdefault(rule, newPart)

    return newPartPerRule

def countElements(polymer):
    countPerElement = dict()

    for c in polymer:
        if not (c in countPerElement):
            countPerElement.setdefault(c, 0)
        
        countPerElement[c] += 1

    return countPerElement

lines = getInputLines()
[template, rules] = getTemplateAndRules(lines)
newPartPerRule = createNewPartPerRule(rules)

# print(template)
# print(rules)
# print(newPartPerRule)


# Part 1
part1Steps = 10

polymer = template
# print('start ->', polymer)
for i in range(part1Steps):
    polymer = applyInsertionRules(polymer, newPartPerRule)
    # print('after ->', i, len(polymer), polymer)
countPerElement = countElements(polymer)
# print(countPerElement)

counts = countPerElement.values()
mostCommonElementCount = max(counts)
leastCommonElementCount = min(counts)
print(mostCommonElementCount, '-', leastCommonElementCount)

resultPart1 = mostCommonElementCount - leastCommonElementCount
print('Anwser day 14 part 1:', resultPart1)

# Part 2
part2Steps = 30

# print('start ->', polymer)
for i in range(part2Steps):
    print('start')
    polymer = applyInsertionRules(polymer, newPartPerRule)
    print('after ->', i + part1Steps, len(polymer))
countPerElement = countElements(polymer)
# print(countPerElement)

counts = countPerElement.values()
mostCommonElementCount = max(counts)
leastCommonElementCount = min(counts)
print(mostCommonElementCount, '-', leastCommonElementCount)

resultPart2 =  mostCommonElementCount - leastCommonElementCount
print('Anwser day 14 part 2:', resultPart2)
