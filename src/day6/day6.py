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


def executeDays(currentFish, days):
    fish = currentFish.copy()
    for day in range(days):
        fish = executeDay(fish)
        print(day, 'of', days, 'resulting in', len(fish), 'fish')

    return fish


def executeDay(currentFish):
    fish = []

    for existingFish in currentFish:
        if existingFish <= 0:
            fish.append(6)  # Fish reset
            fish.append(8)  # New fish
        else:
            fish.append(existingFish - 1)  # Decrease one on counter

    return fish


inputFish = list(map(int, lines[0].split(',')))

# Part 1

totalDaysToExecute = 80

part1DaysToExecute = 80
inputFish = executeDays(inputFish, part1DaysToExecute)
resultPart1 = len(inputFish)
print('Anwser day 6 part 1:', resultPart1)

# Part 2
part2DaysToExecute = totalDaysToExecute - part1DaysToExecute
inputFish = executeDays(inputFish, part2DaysToExecute)
resultPart2 = len(inputFish)
print('Anwser day 6 part 2:', resultPart2)
