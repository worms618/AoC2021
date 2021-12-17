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
    topLeft = Vector(20, -5)
    bottomRight = Vector(30, -10)

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

# Part 1
resultPart1 = 0
print('Anwser day 17 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 17 part 2:', resultPart2)
