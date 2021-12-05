# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day5.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


X = 0
Y = 1

FirstCoor = 0
SecondCoor = 1


def getLineCoordinates(textLine):
    parts = textLine.split(' -> ')

    # FirstCoor, SecondCoor
    return (getCoordinates(parts[0]), getCoordinates(parts[1]))


def getCoordinates(text):
    parts = text.split(',')
    # X, Y
    return (int(parts[0]), int(parts[1]))


def getFurtherstCoordinate(lines):
    biggestX = 0
    biggestY = 0

    for line in lines:
        biggestX = max(biggestX, line[FirstCoor][X], line[SecondCoor][X])
        biggestY = max(biggestY, line[FirstCoor][Y], line[SecondCoor][Y])

    return (biggestX, biggestY)


def defineGrid(maxRows, maxColumns):
    grid = []
    while len(grid) < maxRows + 1:
        column = []
        while len(column) < maxColumns + 1:
            column.append(0)
        grid.append(column)

    return grid


def isHorizontalOrVertical(line):
    sameX = line[FirstCoor][X] == line[SecondCoor][X]
    sameY = line[FirstCoor][Y] == line[SecondCoor][Y]

    return sameX | sameY


def placeLine(grid, line):
    # print('<placeLine>')
    # print('line', line)

    # Assume moving from line[FirstCoor] towards line[SecondCoor]
    xDelta = getDelta(line[FirstCoor][X], line[SecondCoor][X])
    yDelta = getDelta(line[FirstCoor][Y], line[SecondCoor][Y])
    # print('xDelta', xDelta)
    # print('yDelta', yDelta)

    x = line[FirstCoor][X]
    y = line[FirstCoor][Y]
    # print('x', x)
    # print('y', y)

    xEnd = line[SecondCoor][X]
    yEnd = line[SecondCoor][Y]
    # print('xEnd', xEnd)
    # print('yEnd', yEnd)

    shouldLoop = True
    while shouldLoop:
        # print('x', x)
        # print('y', y)

        # print(len(grid))
        # print(len(grid[y]))

        grid[y][x] = grid[y][x] + 1

        shouldLoop = False

        if x != xEnd:
            x = x + xDelta
            shouldLoop = True
        
        if y != yEnd:
            y = y + yDelta
            shouldLoop = True

    # print('</placeLine>')
    return grid


def getDelta(v1, v2):
    # Assume moving from v1 towards v2
    if v1 < v2:
        return 1
    elif v1 > v2:
        return -1
    else:
        return 0


def countAmountOfAtleastOverlaps(grid, overlap):
    overlaps = 0

    for r in grid:
        for c in r:
            if c >= overlap:
                overlaps = overlaps + 1

    return overlaps


def printGrid(grid):
    for r in grid:
        textC = ''
        for c in r:
            if c == 0:
                textC = textC + '.'
            else:
                textC = textC + str(c)
        print(textC)


textLines = getInputLines()

# Part 1
lines = list(map(lambda x: getLineCoordinates(x), textLines))
# print(lines)

furtherestCoordinates = getFurtherstCoordinate(lines)
# print(furtherestCoordinates)

grid = defineGrid(furtherestCoordinates[Y], furtherestCoordinates[X])
# print('After define', grid)

for line in lines:
    if isHorizontalOrVertical(line):
        # print('Is hor or ver', line)
        grid = placeLine(grid, line)
# printGrid(grid)

resultPart1 = countAmountOfAtleastOverlaps(grid, 2)
print('Anwser day 5 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 5 part 2:', resultPart2)
