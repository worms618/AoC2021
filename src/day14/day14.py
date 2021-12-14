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
        [pair, element] = line.split(' -> ')
        rules.setdefault(pair, element)

    return rules

def applyInsertionRules(pairs, newPartPerRule):
    newPairs = []

    for pair in pairs:
        newPart = newPartPerRule[pair]
        newPairLeft = newPart[:2]
        newPairRight = newPart[1:]
        newPairs.append(newPairLeft)
        newPairs.append(newPairRight)

    return newPairs

def getPolymerPairs(polymer):
    pairs = []

    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        pairs.append(pair)

    return pairs


def createNewPartPerRule(rules):
    newPartPerRule = dict()

    for rule in rules:
        newPart = rule[0]+rules[rule]+rule[1]
        newPartPerRule.setdefault(rule, newPart)

    return newPartPerRule

def createPolymerFromPairs(pairs):
    polymer = pairs[0][0]

    for pair in pairs:
        nextPart = pair[1:]
        polymer += nextPart

    return polymer

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

# Part 1
part1Steps = 10

polymer = template
polymerPairs = getPolymerPairs(polymer)
for i in range(part1Steps):
    polymerPairs = applyInsertionRules(polymerPairs, newPartPerRule)

polymer = createPolymerFromPairs(polymerPairs)
countPerElement = countElements(polymer)

counts = countPerElement.values()
mostCommonElementCount = max(counts)
leastCommonElementCount = min(counts)

resultPart1 = mostCommonElementCount - leastCommonElementCount
print('Anwser day 14 part 1:', resultPart1)

# Part 2
part2Steps = 0

for i in range(part2Steps):
    polymerPairs = applyInsertionRules(polymerPairs, newPartPerRule)
    # print(i+part1Steps, len(polymerPairs))

polymer = createPolymerFromPairs(polymerPairs)
countPerElement = countElements(polymer)

counts = countPerElement.values()
mostCommonElementCount = max(counts)
leastCommonElementCount = min(counts)

resultPart2 =  mostCommonElementCount - leastCommonElementCount
print('Anwser day 14 part 2:', resultPart2)
