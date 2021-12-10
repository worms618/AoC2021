# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day10.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


OpeningCharIndex = 0
ClosingCharIndex = 1

SyntaxErrorScoreTable = dict()
SyntaxErrorScoreTable.setdefault(')', 3)
SyntaxErrorScoreTable.setdefault(']', 57)
SyntaxErrorScoreTable.setdefault('}', 1197)
SyntaxErrorScoreTable.setdefault('>', 25137)

ChunkSyntax = dict()
ChunkSyntax.setdefault('(', ')')
ChunkSyntax.setdefault('[', ']')
ChunkSyntax.setdefault('{', '}')
ChunkSyntax.setdefault('<', '>')

lines = getInputLines()


def getChunksFromLine(line, syntax):
    chunks = []

    queue = []
    # processedChars = []

    for char in line:
        isOpeningChar = char in syntax
        if isOpeningChar:
            queue.append(char)
        else:
            nextChunkOpeningChar = queue.pop()
            chunks.append((nextChunkOpeningChar, char))
            # processedChars.append(nextChunkOpeningChar)
            # processedChars.append(char)

    for leftoverOpeningChar in queue:
        chunks.append((leftoverOpeningChar, None))
        # processedChars.append(leftoverOpeningChar)


    # print(len(processedChars), len(processedChars))
    return chunks


def getFirstIllegalChar(chunks, syntax):
    for chunk in chunks:
        openingChar = chunk[OpeningCharIndex]
        closingChar = chunk[ClosingCharIndex]

        if (openingChar == None) | (closingChar == None):
            continue

        expectedClosingChar = syntax[openingChar]
        if closingChar != expectedClosingChar:
            return closingChar

    return None


def getChunksFromLines(lines, syntax):
    return list(map(lambda x: getChunksFromLine(x, syntax), lines))


def getFirstIllegalCharPerLine(chunksPerLines, syntax):
    # get the first illegal char from the chunks per line
    # When no found return None
    # filter out the None values
    return list(filter(lambda x: x != None, map(lambda x: getFirstIllegalChar(x, syntax), chunksPerLines)))


def getTotalSyntaxErrorScore(chars, scoreTable):
    return sum(map(lambda x: scoreTable[x], chars))


# Part 1
# lines = ['{<({})>]']
# lines = ['{([(<{}[<>[]}>{[]{[(<()>']
# lines = ['{([(<{}[<>[]}>{[]{[(<()>', '[({(<(())[]>[[{[]{<()<>>']

chunksPerLines = getChunksFromLines(lines, ChunkSyntax)
# print(chunksPerLines)

firstIllegalCharsPerLine = getFirstIllegalCharPerLine(chunksPerLines, ChunkSyntax)
# print(firstIllegalCharsPerLine)

resultPart1 = getTotalSyntaxErrorScore(firstIllegalCharsPerLine, SyntaxErrorScoreTable)
print('Anwser day 10 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 10 part 2:', resultPart2)
