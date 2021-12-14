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


# Below is after reading a comment on the reddit thread
# Hugh thanks to: https://www.reddit.com/r/adventofcode/comments/rfzq6f/comment/hok6quo/?utm_source=share&utm_medium=web2x&context=3
# Gave 98% of the solution
# Self created names for variables and build functions to do part 1 and part 2

# Could not sleep after seeing solution
# So took the solution and finally get some sleep
lines = getInputLines()


def doCountPairsInNextPolymer(countOfPairsInPolymer, rules):
    countOfPairsInNextPolymer = countOfPairsInPolymer.copy()

    # For every count of pairs
    # Where k is rule
    # Where v is count of rule in s
    for pair, count in countOfPairsInPolymer.items():
        # If the pair has been counted
        # This means the pair exists in the current polymer
        if countOfPairsInPolymer[pair] > 0:
            # The amount of times the pair is counted in the current polymer
            # will be substracted of the next count amount.
            # The pair will be split into two new pairs
            # therefore its amount count in the current polymer
            # will not be in the next polymer anymore
            countOfPairsInNextPolymer[pair] -= count

            # The current pair will be split into two new pairs

            # Get the char that will be inserted in between the pair
            insertitionChar = rules[pair]

            leftPair = pair[0] + insertitionChar
            rightPair = insertitionChar + pair[1]

            # Add the two new pairs into the new count
            # with the amount of the current pair.
            # Why the amount of the current pair? No idea at the moment
            countOfPairsInNextPolymer[leftPair] += count
            countOfPairsInNextPolymer[rightPair] += count

    return countOfPairsInNextPolymer


def doGetAmountMostCommonAndLeastCommonElement(countOfPairsInPolymer):
    pairs = countOfPairsInPolymer.keys()
    joinedPairs = ''.join(pairs)
    uniqueChars = set(joinedPairs)
    amountPerElement = {elementChar: 0 for elementChar in uniqueChars}
    for pair, count in countOfPairsInPolymer.items():
        # Add per element in the pair, the amount counted
        # Count divided by two? No idea why
        amountPerElement[pair[0]] += count / 2
        amountPerElement[pair[1]] += count / 2

    allAmounts = amountPerElement.values()
    amountMostCommon = max(allAmounts)
    amountLeastCommon = min(allAmounts)
    return (amountMostCommon, amountLeastCommon)


def doGetResult(countOfPairsInPolymer):
    [amountMostCommon, amountLeastCommon] = doGetAmountMostCommonAndLeastCommonElement(countOfPairsInPolymer)
    # Plus 1 for rounding issues
    return (int(amountMostCommon) - int(amountLeastCommon)) + 1


polymerTemplate = lines[0]

# Create Rules
# Create a dictionary for every line
# Where key is chars 0 until 2 -> rule
# Where value is chars -1 aka the last char -> insert value
rules = {line[:2]: line[-1] for line in lines[2:]}

# Create the count per pair
# Create a dictionary where the amount counted per pair is registered
# Where key is the unique key of rules -> pair for rule
# Where value is the amount counted the pair is in polymerTemplate
countOfPairsInPolymer = {pair: polymerTemplate.count(pair) for pair in rules.keys()}

# Part 1
stepsPart1 = 10
for i in range(stepsPart1):
    countOfPairsInPolymer = doCountPairsInNextPolymer(countOfPairsInPolymer, rules)

resultPart1 = doGetResult(countOfPairsInPolymer)
print('Anwser day 14 part 1:', resultPart1)

# Part 2
part2Steps = 30
for i in range(part2Steps):
    countOfPairsInPolymer = doCountPairsInNextPolymer(countOfPairsInPolymer, rules)

resultPart2 = doGetResult(countOfPairsInPolymer)
print('Anwser day 14 part 2:', resultPart2)

# Below here, my own try for the solution
# Works in brute force with enough memory and time
# lines = getInputLines()
# def getTemplateAndRules(lines):
#     template = lines[0]
#     rules = createRules(lines[2:])

#     return (template, rules)

# def createRules(lines):
#     rules = dict()

#     for line in lines:
#         [pair, element] = line.split(' -> ')
#         rules.setdefault(pair, element)

#     return rules

# def applyInsertionRules(pairs, newPartPerRule):
#     newPairs = []

#     for pair in pairs:
#         newPart = newPartPerRule[pair]
#         newPairLeft = newPart[:2]
#         newPairRight = newPart[1:]
#         newPairs.append(newPairLeft)
#         newPairs.append(newPairRight)

#     return newPairs

# def getPolymerPairs(polymer):
#     pairs = []

#     for i in range(len(polymer) - 1):
#         pair = polymer[i:i+2]
#         pairs.append(pair)

#     return pairs


# def createNewPartPerRule(rules):
#     newPartPerRule = dict()

#     for rule in rules:
#         newPart = rule[0]+rules[rule]+rule[1]
#         newPartPerRule.setdefault(rule, newPart)

#     return newPartPerRule

# def createPolymerFromPairs(pairs):
#     polymer = pairs[0][0]

#     for pair in pairs:
#         nextPart = pair[1:]
#         polymer += nextPart

#     return polymer

# def countElements(polymer):
#     countPerElement = dict()

#     for c in polymer:
#         if not (c in countPerElement):
#             countPerElement.setdefault(c, 0)

#         countPerElement[c] += 1

#     return countPerElement


# [template, rules] = getTemplateAndRules(lines)
# newPartPerRule = createNewPartPerRule(rules)

# # Part 1
# part1Steps = 10

# polymer = template
# polymerPairs = getPolymerPairs(polymer)
# for i in range(part1Steps):
#     polymerPairs = applyInsertionRules(polymerPairs, newPartPerRule)

# polymer = createPolymerFromPairs(polymerPairs)
# countPerElement = countElements(polymer)

# counts = countPerElement.values()
# mostCommonElementCount = max(counts)
# leastCommonElementCount = min(counts)

# resultPart1 = mostCommonElementCount - leastCommonElementCount
# print('Anwser day 14 part 1:', resultPart1)

# # Part 2
# part2Steps = 0

# for i in range(part2Steps):
#     polymerPairs = applyInsertionRules(polymerPairs, newPartPerRule)
#     # print(i+part1Steps, len(polymerPairs))

# polymer = createPolymerFromPairs(polymerPairs)
# countPerElement = countElements(polymer)

# counts = countPerElement.values()
# mostCommonElementCount = max(counts)
# leastCommonElementCount = min(counts)

# resultPart2 =  mostCommonElementCount - leastCommonElementCount
# print('Anwser day 14 part 2:', resultPart2)
