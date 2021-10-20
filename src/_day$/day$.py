import sys
import os

if len(sys.argv) < 1:
    raise ValueError('Path of this script not available in sys.argv')

lines = []
inputFilePath=sys.argv[0].replace('day$.py', 'input.txt')
with open(inputFilePath) as f:
    lines = [line.strip() for line in f]

# Part 1
resultPart1 = 0
print('Anwser day $ part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day $ part 2:', resultPart2)