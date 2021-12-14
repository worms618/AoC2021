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

def applyInsertionRules(polymer, rules):
    newPolymer = ''
    pairs = getPolymerPairs(polymer)
    # print(pairs)

    for pair in pairs:
        # print(pair)
        if pair in rules:
            if len(newPolymer) == 0:
                newPolymer = pair[0]

            value = rules[pair]
            newPart = ''.join([value, pair[1]])
            # print(newPart)
            newPolymer += newPart

    return newPolymer

def getPolymerPairs(polymer):
    pairs = []

    for i in range(len(polymer) - 1):
        pairs.append(polymer[i:i+2])

    return pairs

def countElements(polymer):
    countPerElement = dict()

    for c in polymer:
        if not (c in countPerElement):
            countPerElement.setdefault(c, 0)
        
        countPerElement[c] += 1

    return countPerElement

lines = getInputLines()
[template, rules] = getTemplateAndRules(lines)

# print(template)
# print(rules)


# Part 1
steps = 10

polymer = template
# print('start ->', polymer)
for _ in range(steps):
    polymer = applyInsertionRules(polymer, rules)
    # print('after ->', polymer)
countPerElement = countElements(polymer)
# print(countPerElement)

counts = countPerElement.values()
mostCommonElementCount = max(counts)
leastCommonElementCount = min(counts)
# print(mostCommonElementCount, '-', leastCommonElementCount)

resultPart1 = mostCommonElementCount - leastCommonElementCount
print('Anwser day 14 part 1:', resultPart1)

# Part 2
steps = 30

polymer = template
# print('start ->', polymer)
for i in range(steps):
    polymer = applyInsertionRules(polymer, rules)
    print('after ->', i, len(polymer))
countPerElement = countElements(polymer)
# print(countPerElement)

counts = countPerElement.values()
mostCommonElementCount = max(counts)
leastCommonElementCount = min(counts)
# print(mostCommonElementCount, '-', leastCommonElementCount)

resultPart2 =  mostCommonElementCount - leastCommonElementCount
print('Anwser day 14 part 2:', resultPart2)
