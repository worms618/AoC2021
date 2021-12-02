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


lines = getInputLines()

# Part 1
resultPart1 = 0
print('Anwser day 2 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 2 part 2:', resultPart2)
