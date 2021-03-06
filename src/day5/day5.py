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


def isDiagonal45Degrees(line):
    # Calculate the magnitude
    # When magnitude is an integer
    # Then line is diagonal with 45 degrees
    xDiff = line[SecondCoor][X] - line[FirstCoor][X]
    yDiff = line[SecondCoor][Y] - line[FirstCoor][Y]

    if (xDiff == 0) | (yDiff == 0):
        return False

    magnitude = xDiff / yDiff

    return magnitude.is_integer()


def placeLine(grid, line):
    # Assume moving from line[FirstCoor] towards line[SecondCoor]
    xDelta = getDelta(line[FirstCoor][X], line[SecondCoor][X])
    yDelta = getDelta(line[FirstCoor][Y], line[SecondCoor][Y])

    x = line[FirstCoor][X]
    y = line[FirstCoor][Y]

    xEnd = line[SecondCoor][X]
    yEnd = line[SecondCoor][Y]

    shouldLoop = True
    while shouldLoop:
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

lines = list(map(lambda x: getLineCoordinates(x), textLines))
# print(lines)

furtherestCoordinates = getFurtherstCoordinate(lines)
# print(furtherestCoordinates)


# Part 1
grid = defineGrid(furtherestCoordinates[Y], furtherestCoordinates[X])
# print('After define', grid)

for line in lines:
    if isHorizontalOrVertical(line):
        # print('Is hor or ver', line)
        grid = placeLine(grid, line)
# printGrid(part1Grid)

resultPart1 = countAmountOfAtleastOverlaps(grid, 2)
print('Anwser day 5 part 1:', resultPart1)

# Part 2
grid = defineGrid(furtherestCoordinates[Y], furtherestCoordinates[X])
# print('After define', grid)

for line in lines:
    if isHorizontalOrVertical(line) | isDiagonal45Degrees(line):
        # print('Is hor or ver or diag 45degrees', line)
        grid = placeLine(grid, line)
# printGrid(part2Grid)

resultPart2 = countAmountOfAtleastOverlaps(grid, 2)
print('Anwser day 5 part 2:', resultPart2)
