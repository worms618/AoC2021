# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day1.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---

def getNextAmountIncreased(curDepth, nextDepth, curAmountIncreased):
    if curDepth < nextDepth:
        return curAmountIncreased + 1
    else:
        return curAmountIncreased

depths = getInputLines()

# Part 1
amountIncreased=0

amountOfDepths = len(depths)

for index in range(amountOfDepths):
    shouldCalcAmountIncreased = (index + 1) < amountOfDepths
    if shouldCalcAmountIncreased:
        curDepth = depths[index]
        nextDepth = depths[index + 1]
        amountIncreased = getNextAmountIncreased(int(curDepth), int(nextDepth), amountIncreased)

resultPart1 = amountIncreased
print('Anwser day 1 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 1 part 2:', resultPart2)
