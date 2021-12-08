# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day8.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---

UniqueSignalPattern = 0
FourDigitOutputValue = 1

segmentsPerDigit = dict()
segmentsPerDigit.setdefault(0, 'abcefg')
segmentsPerDigit.setdefault(1, 'cf')
segmentsPerDigit.setdefault(2, 'acdeg')
segmentsPerDigit.setdefault(3, 'acdfg')
segmentsPerDigit.setdefault(4, 'bcdf')
segmentsPerDigit.setdefault(5, 'abdfg')
segmentsPerDigit.setdefault(6, 'abdefg')
segmentsPerDigit.setdefault(7, 'acf')
segmentsPerDigit.setdefault(8, 'abcdefg')
segmentsPerDigit.setdefault(9, 'abcdfg')

# 1 = 2, 4 = 4, 7 = 3, 8 = 7
uniqueSegmentLength = [2,3,4,7]

def parseNote(line):
    parts = line.split('|')
    return (parts[0].strip().split(' '), parts[1].strip().split(' '))

lines = getInputLines()

notes = list(map(lambda x: parseNote(x), lines))
# print(notes)
# Part 1

countOutputWithUniqueSegmentLength = 0

for note in notes:
    for output in note[FourDigitOutputValue]:
        if (len(output) in uniqueSegmentLength):
            countOutputWithUniqueSegmentLength += 1


resultPart1 = countOutputWithUniqueSegmentLength
print('Anwser day 8 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 8 part 2:', resultPart2)
