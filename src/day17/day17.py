# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day17.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---

class Vector(object):

    def __init__(self, x=0, y=0):
        self._x, self._y = x, y

    def setx(self, x): self._x = int(x)
    def sety(self, y): self._y = int(y)
    def asString(self): return ','.join([str(self._x), str(self._y)])
    def copy(self): return Vector(self.x, self.y)

    x = property(lambda self: int(self._x), setx)
    y = property(lambda self: int(self._y), sety)

def getAreaCoordinates(line):
    parts = line.replace('target area: ', '').split(',')

    xPartValues = list(map(int,parts[0].strip()[2:].split('..')))
    yPartValues = list(map(int,parts[1].strip()[2:].split('..')))

    # Assume
    # top left -> minX, maxY
    # bottom right -> maxX, minY
    # E.g. target area: x=20..30, y=-10..-5
    # minX = 20; maxX = 30
    # minY = -10; maxY = -5
    minX = min(xPartValues)
    minY = min(yPartValues)

    maxX = max(xPartValues)
    maxY = max(yPartValues)

    topLeft = Vector(minX, maxY)
    bottomRight = Vector(maxX, minY)

    return (topLeft, bottomRight)

def doStep(pos, vel):
    nextPos = pos.copy()
    nextVel = vel.copy()
    
    # The probe's x position increases by its x velocity.
    # The probe's y position increases by its y velocity.
    # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, 
    #   it decreases by 1 if it is greater than 0, 
    #   increases by 1 if it is less than 0, 
    #   or does not change if it is already 0.
    # Due to gravity, the probe's y velocity decreases by 1.

    nextPos.x += vel.x
    nextPos.y += vel.y

    if nextVel.x > 0:
        nextVel.x -= 1
    elif nextVel.x < 0:
        nextVel.x += 1

    nextVel.y -= 1

    return (nextPos, nextVel)

def didPassArea(areaCoordinates, pos):
    # areaCoordinates:
    # first coordinate - top left point
    # second coordinate - right bottom point

    # Assume:
    # Area is right of pos
    # Area is beneath pos

    [_, c2] = areaCoordinates

    maxY = c2.y
    maxX = c2.x

    isPassedX = pos.x > maxX
    isPassedY = pos.y < maxY

    return isPassedX | isPassedY

def isInArea(areaCoordinates, pos):
    # areaCoordinates:
    # first coordinate - top left point
    # second coordinate - right bottom point

    # Assume:
    # Area is right of pos
    # Area is beneath pos

    [c1, c2] = areaCoordinates

    minY = c1.y
    minX = c1.x

    maxY = c2.y
    maxX = c2.x

    isPassedMinX = pos.x > minX
    isPassedMinY = pos.y < minY

    isPassedMaxX = pos.x > maxX
    isPassedMaxY = pos.y < maxY

    isPassedBothMins = isPassedMinX & isPassedMinY
    isPassedOneMax = isPassedMaxX | isPassedMaxY

    return isPassedBothMins and (not isPassedOneMax)

def getAllPathsThatReachArea(area, startPos):
    paths = []

    potentialVels = getPotentialVelocities(area)

    while len(potentialVels) > 0:
        potVel = potentialVels.pop()

        path = getPathIfReachArea(area, startPos, potVel)
        if path != None:
            paths.append(path)

    return paths

def getPotentialVelocities(area):
    return [Vector(7,2), Vector(6,3), Vector(9,0), Vector(17,-4)]

def getPathIfReachArea(area, initialPos, initialVel):
    positions = [initialPos]

    probePos = initialPos.copy()
    probeVel = initialVel.copy()

    while True:
        [nextProbePos, nextProbeVel] = doStep(probePos, probeVel)

        # In area?
        # Yes? positions.append(nextProbePos.copy())

        InArea = isInArea(area, nextProbePos)
        if InArea:
            positions.append(nextProbePos.copy())
            break
        
        if didPassArea(area, nextProbePos):
            return None
        
        probePos = nextProbePos.copy()
        probeVel = nextProbeVel.copy()
        positions.append(nextProbePos.copy())

    return positions


lines = getInputLines()

probePos = Vector(0,0)
probeVel = Vector(7,2)
area = getAreaCoordinates(lines[0])

while True:
    [nextProbePos, nextProbeVel] = doStep(probePos, probeVel)
    if didPassArea(area, nextProbePos):
        break
    probePos = nextProbePos
    probeVel = nextProbeVel


print(probePos.asString(), probeVel.asString(), didPassArea(area, probePos))

paths = getAllPathsThatReachArea(area, Vector(0,0))
for path in paths:
    print('->'.join(map(lambda x: x.asString(), path)))

# Part 1
resultPart1 = 0
print('Anwser day 17 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 17 part 2:', resultPart2)
