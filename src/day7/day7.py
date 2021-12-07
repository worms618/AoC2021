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

def countFuelTowardsPositions(groupedPositions, positionTowards):
    totalFuel = 0

    for position in groupedPositions:
        multiplier = groupedPositions[position]
        fuel = abs(positionTowards - position) * multiplier
        totalFuel += fuel

    return totalFuel


lines = getInputLines()
positions = list(map(int, lines[0].split(',')))

# Part 1
positionsPart1 = positions.copy()
maxPosition = max(positionsPart1)
minPosition = min(positionsPart1)
# print(minPosition, maxPosition)

groupedPositions = groupPositions(positionsPart1)
# print(groupedPositions)

leastFuel = -1
leastPosition = -1
for position in groupedPositions:
    fuel = countFuelTowardsPositions(groupedPositions, position)
    if (leastFuel < 0) | (fuel < leastFuel):
        leastFuel = fuel
        leastPosition = position
    
# print(leastPosition)
resultPart1 = leastFuel
print('Anwser day 7 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 7 part 2:', resultPart2)
