# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day1.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


def getNextAmountIncreased(curDepth, nextDepth, curAmountIncreased):
    if curDepth < nextDepth:
        return curAmountIncreased + 1
    else:
        return curAmountIncreased


def toInt(value):
    return int(value)


lines = getInputLines()
linesAsInts = map(toInt, lines)
depths = [line for line in linesAsInts]

# Part 1
amountIncreased = 0

amountOfDepths = len(depths)

for index in range(amountOfDepths):
    shouldCalcAmountIncreased = (index + 1) < amountOfDepths
    if shouldCalcAmountIncreased:
        curDepth = depths[index]
        nextDepth = depths[index + 1]
        amountIncreased = getNextAmountIncreased(curDepth, nextDepth, amountIncreased)

resultPart1 = amountIncreased
print('Anwser day 1 part 1:', resultPart1)

# Part 2
amountIncreased = 0

measurementsGroups = []
measurementsGroupIndices = []

groupsToFill = []

for index in range(amountOfDepths):
    groupsToFill.append([])

    for groupToFill in groupsToFill:
        groupToFill.append(index)

    groupIndexToCheck = 0
    while (groupIndexToCheck < len(groupsToFill)):
        groupToCheck = groupsToFill[groupIndexToCheck]
        if len(groupToCheck) == 3:
            filledGroup = groupsToFill.pop(groupIndexToCheck)
            measurementsGroupIndices.append(filledGroup)
        else:
            groupIndexToCheck = groupIndexToCheck + 1

for measurementGroupIndices in measurementsGroupIndices:
    measurementGroup = []
    measurementsGroups.append(measurementGroup)

    for depthIndex in measurementGroupIndices:
        measurementGroup.append(depths[depthIndex])

totalMeasurementsGroups = len(measurementsGroups)
for index in range(totalMeasurementsGroups):
    shouldCalcAmountIncreased = (index + 1) < totalMeasurementsGroups
    if shouldCalcAmountIncreased:
        curDepth = sum(measurementsGroups[index])
        nextDepth = sum(measurementsGroups[index + 1])
        amountIncreased = getNextAmountIncreased(curDepth, nextDepth, amountIncreased)

resultPart2 = amountIncreased
print('Anwser day 1 part 2:', resultPart2)
