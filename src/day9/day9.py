# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day9.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


X = 0
Y = 1


def createVector(x=0, y=0):
    return (x, y)

def addVectors(v1, v2):
    return (
        v1[X] + v2[X],
        v1[Y] + v2[Y]
    )

def createHeightMap(lines):
    heightMap = []

    for line in lines:
        row = list(map(int, line))
        heightMap.append(row)

    return heightMap


def inboundsPoint(heightMap, point):
    if (point[Y] < 0) | (point[Y] >= len(heightMap)):
        return False
    
    if (point[X] < 0) | (point[X] >= len(heightMap[point[Y]])):
        return False

    return True


def getValue(heightMap, point):
    return heightMap[point[Y]][point[X]]


def getLowPointValues(heightMap):
    points = []

    for r in range(len(heightMap)):
        for c in range(len(heightMap[r])):
            point = createVector(c, r)
            value = getValue(heightMap, point)
            if isLowerThanAdjacent(heightMap, directAdjacentVectors, point, value):
                points.append(value) 

    return points


def isLowerThanAdjacent(heightMap, adjacentVectors, point, value):
    for adjacentVector in adjacentVectors:
        adjacentPoint = addVectors(point, adjacentVector)
        if inboundsPoint(heightMap, adjacentPoint):
            adjacentValue = getValue(heightMap, adjacentPoint)
            if value >= adjacentValue:
                return False # Found one where value is greater than adjacent value
    
    return True


lines = getInputLines()
directAdjacentVectors = [
    createVector(-1,  0),
    createVector( 0, -1),
    createVector( 1,  0),
    createVector( 0,  1)
]

# Part 1
heightMap = createHeightMap(lines)
# print(heightMap)

lowPointValues = getLowPointValues(heightMap)
# print(lowPointValues)

lowPointRiskLevels = list(map(lambda x: x + 1, lowPointValues))
# print(lowPointRiskLevels)

resultPart1 = sum(lowPointRiskLevels)
print('Anwser day 9 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 9 part 2:', resultPart2)
