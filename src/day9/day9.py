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


def createProcessedMap(heightMap):
    return list(map(lambda x: list(map(lambda _: False, x)), heightMap))


def inboundsPoint(heightMap, point):
    if (point[Y] < 0) | (point[Y] >= len(heightMap)):
        return False

    if (point[X] < 0) | (point[X] >= len(heightMap[point[Y]])):
        return False

    return True


def getInboundAdjacentPoints(point, adjacentVectors):
    adjacentPoints = []

    for adjacentVector in adjacentVectors:
        adjacentPoint = addVectors(point, adjacentVector)
        if inboundsPoint(heightMap, adjacentPoint):
            adjacentPoints.append(adjacentPoint)

    return adjacentPoints


def setValue(map, point, value):
    map[point[Y]][point[X]] = value
    return map


def getValue(map, point):
    return map[point[Y]][point[X]]


def getLowPoints(heightMap):
    points = []

    for r in range(len(heightMap)):
        for c in range(len(heightMap[r])):
            point = createVector(c, r)
            value = getValue(heightMap, point)
            if isLowerThanAdjacents(heightMap, directAdjacentVectors, point, value):
                points.append(point)

    return points


def getLowPointValues(lowPoints):
    return list(map(lambda x: getValue(heightMap, x), lowPoints))


def isLowerThanAdjacents(heightMap, adjacentVectors, point, value):
    inboundAdjacentPoints = getInboundAdjacentPoints(point, adjacentVectors)
    for adjacentPoint in inboundAdjacentPoints:
        adjacentValue = getValue(heightMap, adjacentPoint)
        if value >= adjacentValue:
            return False  # Found one where value is greater than adjacent value


    return True


def setProcessedForValue(heightMap, processedMap, value):
    for r in range(len(heightMap)):
        for c in range(len(heightMap[r])):
            point = createVector(c, r)
            pointValue = getValue(heightMap, point)
            if pointValue == value:
                setValue(processedMap, point, True)

def pointIsProcessed(processedMap, point):
    return getValue(processedMap, point)

def getBasinsPoints(heightMap, processedMap, lowPoints):
    basinsPoints = []
    for lowPoint in lowPoints:
        basinsPoints.append(getBasinPointsFromPoint(
            heightMap, processedMap, lowPoint))

    return basinsPoints


def getBasinPointsFromPoint(heightMap, processedMap, lowPoint):
    basinPoints = [lowPoint]
    lowPointValue = getValue(heightMap, lowPoint)

    # print(lowPoint, lowPointValue)

    isNewBasinPoint = False

    inboundAdjacentPoints = getInboundAdjacentPoints(lowPoint, directAdjacentVectors)
    newBasinPoints = []
    for adjacentPoint in inboundAdjacentPoints:
        adjacentPointValue = getValue(heightMap, adjacentPoint)
        isNewBasinPoint = (not pointIsProcessed(processedMap, adjacentPoint)) and (adjacentPointValue > lowPointValue)
        if isNewBasinPoint:
            newBasinPoints.append(adjacentPoint)
            basinPoints.append(adjacentPoint)

    # Set new basis points processed
    for newBasinPoint in newBasinPoints:
        setValue(processedMap, newBasinPoint, True)
    
    for newBasinPoint in newBasinPoints:
        otherBasinPoints = getBasinPointsFromPoint(heightMap, processedMap, newBasinPoint)
        for otherBasinPoint in otherBasinPoints:
            if not (otherBasinPoint in basinPoints):
                basinPoints.append(otherBasinPoint)

    # print(newBasinPoints)

    return basinPoints


lines = getInputLines()
directAdjacentVectors = [
    createVector(-1,  0),
    createVector(0, -1),
    createVector(1,  0),
    createVector(0,  1)
]

# Part 1
heightMap = createHeightMap(lines)
# print(heightMap)

lowPoints = getLowPoints(heightMap)
lowPointValues = getLowPointValues(lowPoints)
# print(lowPointValues)

lowPointRiskLevels = list(map(lambda x: x + 1, lowPointValues))
# print(lowPointRiskLevels)

resultPart1 = sum(lowPointRiskLevels)
print('Anwser day 9 part 1:', resultPart1)

# Part 2
processedMap = createProcessedMap(heightMap)
setProcessedForValue(heightMap, processedMap, 9)
basinsPoints = getBasinsPoints(heightMap, processedMap, lowPoints)
# for basinPoints in basinsPoints:
#     print(basinPoints)

basinsVolumes = list(map(lambda x: len(x), basinsPoints))
# print(basinsVolumes)

xLargestVolumes = []
basinsVolumesCopy = basinsVolumes.copy()
while (len(xLargestVolumes) < 3) and (len(basinsVolumesCopy) > 0):
    maxValue = max(basinsVolumesCopy)
    xLargestVolumes.append(maxValue)
    basinsVolumesCopy.remove(maxValue)

# print(xLargestVolumes)

resultPart2 = xLargestVolumes[0]
for i in range(1, len(xLargestVolumes)):
    resultPart2 *= xLargestVolumes[i]

print('Anwser day 9 part 2:', resultPart2)
