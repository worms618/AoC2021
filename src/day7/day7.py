# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day7.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


def groupPositions(positions):
    groupedPositions = dict()
    # Count amount per position

    for position in positions:
        if not (position in groupedPositions):
            groupedPositions.setdefault(position, 1)
        else:
            groupedPositions[position] += 1

    return groupedPositions


def sumFuelTowardsPostion(groupedPositions, positionTowards):
    totalFuel = 0

    for position in groupedPositions:
        multiplier = groupedPositions[position]
        positionAbsDiff = abs(positionTowards - position)

        if positionAbsDiff == 0:
            continue

        fuel = positionAbsDiff * multiplier
        totalFuel += fuel

    return totalFuel


def sumFuelCumulativeTowardsPostion(groupedPositions, positionTowards):
    totalFuel = 0

    for position in groupedPositions:
        multiplier = groupedPositions[position]
        positionAbsDiff = abs(positionTowards - position)

        if positionAbsDiff == 0:
            continue

        fuel = getCumulativeOfRange(positionAbsDiff) * multiplier
        totalFuel += fuel

    return totalFuel

def getCumulativeOfRange(stop):
    if not (stop in cumulativeCache):
        value = calcCumulativeOrRange(stop)
        cumulativeCache.setdefault(stop, value)
    
    return cumulativeCache[stop]

def calcCumulativeOrRange(stop):
    value = 0

    # stop inclusive
    for step in range(stop + 1):
        value += step
    
    return value

cumulativeCache = dict()

lines = getInputLines()
positions = list(map(int, lines[0].split(',')))
maxPosition = max(positions)
minPosition = min(positions)
# print(minPosition, maxPosition)

groupedPositions = groupPositions(positions)
# print(groupedPositions)

# Part 1
leastFuel = -1
for position in range(minPosition, maxPosition):
    fuel = sumFuelTowardsPostion(groupedPositions, position)
    if (leastFuel < 0) | (fuel < leastFuel):
        leastFuel = fuel

resultPart1 = leastFuel
print('Anwser day 7 part 1:', resultPart1)

# Part 2
leastFuel = -1
for position in range(minPosition, maxPosition):
    fuel = sumFuelCumulativeTowardsPostion(groupedPositions, position)
    if (leastFuel < 0) | (fuel < leastFuel):
        leastFuel = fuel

resultPart2 = leastFuel
print('Anwser day 7 part 2:', resultPart2)
