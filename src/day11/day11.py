# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day11.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


X = 0
Y = 1

lines = getInputLines()
totalFlashes = 0


def createVector(x, y):
    return (x, y)


def addVector(v1, v2):
    return (v1[X] + v2[X], v1[Y] + v2[Y])


def pointInbounds(grid, point):
    if (point[Y] < 0) | (point[Y] >= len(grid)):
        return False

    if (point[X] < 0) | (point[X] >= len(grid[point[Y]])):
        return False

    return True


def getAdjacentPointInbounds(grid, point, adjacentVectors):
    return list(
        filter(lambda x: pointInbounds(grid, x),
               map(lambda x: addVector(point, x), adjacentVectors)
               )
    )


def createGrid(lines):
    grid = []

    for line in lines:
        row = list(map(int, line))
        grid.append(row)

    return grid


def printGrid(grid):
    for row in grid:
        print(row)


def doStep(grid, onFlash, adjacentVectors):
    newGrid = []

    # Increase the energy level with one
    for row in grid:
        newGrid.append(list(map(lambda x: x + 1, row)))

    pointsDidFlash = []
    for r in range(len(newGrid)):
        for c in range(len(newGrid[r])):
            point = createVector(c, r)
            doPointStep(newGrid, point, adjacentVectors, pointsDidFlash, onFlash)

    for point in pointsDidFlash:
        newGrid[point[Y]][point[X]] = 0

    return newGrid

def doPointStep(grid, point, adjacentVectors, pointsDidFlash, onFlash):
    value = grid[point[Y]][point[X]]
    if (value > 9) & (not (point in pointsDidFlash)):
        onFlash()
        pointsDidFlash.append(point)

        for adjacentPoint in getAdjacentPointInbounds(grid, point, adjacentVectors):
            grid[adjacentPoint[Y]][adjacentPoint[X]] += 1
            doPointStep(grid, adjacentPoint, adjacentVectors, pointsDidFlash, onFlash)


def doOnFlash():
    global totalFlashes
    totalFlashes += 1

def didAllFlash(grid):
    for r in grid:
        for value in r:
            if value > 0:
                return False
    return True

adjacents = [
    # top row
    createVector(-1, -1),
    createVector(0, -1),
    createVector(1, -1),
    # middle row
    createVector(-1, 0),
    createVector(1, 0),
    # bottom row
    createVector(-1, 1),
    createVector(0, 1),
    createVector(1, 1),
]


totalFlashes = 0
grid = createGrid(lines)

# print(grid)

# Part 1
totalFlashes = 0
steps = 100

# printGrid(grid)
for i in range(steps):
    grid = doStep(grid, doOnFlash, adjacents)
    # print('-------')
    # printGrid(grid)

# printGrid(grid)

resultPart1 = totalFlashes
print('Anwser day 11 part 1:', resultPart1)

# Part 2
part2Steps = 0
while True:
    grid = doStep(grid, doOnFlash, adjacents)
    part2Steps += 1
    if didAllFlash(grid):
        break
    # print('-------')
    # printGrid(grid)
# printGrid(grid)

resultPart2 = steps + part2Steps
print('Anwser day 11 part 2:', resultPart2)
