# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day2.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


def calcNextSimplePos(command, position):
    cmdIdentifier = command[0]
    cmdUnits = command[1]

    posHorizontal = position[0]
    posDepth = position[1]

    if cmdIdentifier.startswith('f'):
        posHorizontal = posHorizontal + cmdUnits
    elif cmdIdentifier.startswith('d'):
        posDepth = posDepth + cmdUnits
    elif cmdIdentifier.startswith('u'):
        posDepth = posDepth - cmdUnits

    return (posHorizontal, posDepth)

def calcNextPosByAim(command, position):
    cmdIdentifier = command[0]
    cmdUnits = command[1]

    posHorizontal = position[0]
    posDepth = position[1]
    posAim = position[2]

    if cmdIdentifier.startswith('f'):
        posHorizontal = posHorizontal + cmdUnits
        posDepth = posDepth + (posAim * cmdUnits)
    elif cmdIdentifier.startswith('d'):
        posAim = posAim + cmdUnits
    elif cmdIdentifier.startswith('u'):
        posAim = posAim - cmdUnits

    return (posHorizontal, posDepth, posAim)


def createCommand(line):
    commandParts = line.split(" ", 1)
    # Index 0: identifier
    # Index 1: units
    return (commandParts[0], int(commandParts[1]))


lines = getInputLines()

# Part 1

# Index 0: horizontal
# Index 1: depth
position = (0, 0)

for line in lines:
    command = createCommand(line)
    position = calcNextSimplePos(command, position)

# horizontal * depth
resultPart1 = position[0] * position[1]
print('Anwser day 2 part 1:', resultPart1)

# Part 2

# Index 0: horizontal
# Index 1: depth
# Index 2: aim
position = (0, 0, 0)

for line in lines:
    command = createCommand(line)
    position = calcNextPosByAim(command, position)

# horizontal * depth
resultPart2 = position[0] * position[1]
print('Anwser day 2 part 2:', resultPart2)
