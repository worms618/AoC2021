# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day6.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


lines = getInputLines()

totalStatuses = 9
statusFishToReproduce = 0
statusFishReset = 6
statusFishNew = 8

def createZeroForRange(total):
    collection = []
    for i in range(total):
        collection.append(0)
    return collection


def determineStatuses(fish):
    statuses = createZeroForRange(totalStatuses)

    for f in fish:
        statuses[f] += 1

    return statuses


def executeDays(currentStatuses, days):
    statuses = currentStatuses.copy()
    for day in range(days):
        statuses = executeDay(statuses)

    return statuses


def executeDay(currentStatuses):
    statuses = createZeroForRange(len(currentStatuses))

    totalFishToReproduce = currentStatuses[statusFishToReproduce]
    statuses[statusFishReset] += totalFishToReproduce
    statuses[statusFishNew] += totalFishToReproduce

    for status in range(1, len(currentStatuses)):
        statuses[status - 1] += currentStatuses[status]

    return statuses


def calcTotalFish(fish):
    return sum(fish)


def printStases(statuses):
    for i in range(len(statuses)):
        print(i, '->', statuses[i])


inputFish = list(map(int, lines[0].split(',')))
statuses = determineStatuses(inputFish)
# printStases(statuses)

# Part 1

totalDaysToExecute = 256

part1DaysToExecute = 80
statuses = executeDays(statuses, part1DaysToExecute)
resultPart1 = calcTotalFish(statuses)
print('Anwser day 6 part 1:', resultPart1)

# Part 2
part2DaysToExecute = totalDaysToExecute - part1DaysToExecute
statuses = executeDays(statuses, part2DaysToExecute)
resultPart2 = calcTotalFish(statuses)
print('Anwser day 6 part 2:', resultPart2)
