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

CompletationScoreTable = dict()
CompletationScoreTable.setdefault(')', 1)
CompletationScoreTable.setdefault(']', 2)
CompletationScoreTable.setdefault('}', 3)
CompletationScoreTable.setdefault('>', 4)

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

def hasAIllegalChunk(chunks, syntax):
    illegalChar = getFirstIllegalChar(chunks, syntax)

    if illegalChar == None:
        return False
    return True

def getChunksFromLines(lines, syntax):
    return list(map(lambda x: getChunksFromLine(x, syntax), lines))

def divideInIncompleteAndIllegal(chunksPerLines, syntax):
    incompletes = []
    illegals = []

    for chunksForLine in chunksPerLines:
        if hasAIllegalChunk(chunksForLine, syntax):
            illegals.append(chunksForLine)
        else:
            incompletes.append(chunksForLine)

    return (incompletes, illegals)


def getFirstIllegalCharPerLine(chunksPerLines, syntax):
    # get the first illegal char from the chunks per line
    # When no found return None
    # filter out the None values
    return list(filter(lambda x: x != None, map(lambda x: getFirstIllegalChar(x, syntax), chunksPerLines)))


def getTotalSyntaxErrorScore(chars, scoreTable):
    return sum(map(lambda x: scoreTable[x], chars))

def getIncompleteChunks(chunks):
    return list(filter(lambda x: x[ClosingCharIndex] == None, chunks))

def getCompletationOfChunks(incompleteChunks, syntax):
    return ''.join(map(lambda x: syntax[x[OpeningCharIndex]],incompleteChunks))

def getCompletationScore(completation, scoreTable):
    score = 0

    for char in completation:
        score *= 5
        score += scoreTable[char]

    return score


# Part 1
# lines = ['{<({})>]']
# lines = ['{([(<{}[<>[]}>{[]{[(<()>']
# lines = ['{([(<{}[<>[]}>{[]{[(<()>', '[({(<(())[]>[[{[]{<()<>>']

chunksPerLines = getChunksFromLines(lines, ChunkSyntax)
# print(chunksPerLines)

[incompletes, illegals] = divideInIncompleteAndIllegal(chunksPerLines, ChunkSyntax)

firstIllegalCharsPerLine = getFirstIllegalCharPerLine(illegals, ChunkSyntax)
# print(firstIllegalCharsPerLine)

resultPart1 = getTotalSyntaxErrorScore(firstIllegalCharsPerLine, SyntaxErrorScoreTable)
print('Anwser day 10 part 1:', resultPart1)

# Part 2

scores = []
for incomplete in incompletes:
    chunks = getIncompleteChunks(incomplete)
    chunks.reverse()
    completation = getCompletationOfChunks(chunks, ChunkSyntax)
    completationScore = getCompletationScore(completation, CompletationScoreTable)
    # print(completation, completationScore)
    scores.append(completationScore)

scores.sort()
middleScoreIndex = int(len(scores) / 2)
# print(scores)
# print(len(scores), len(scores) / 2, middleScoreIndex)
resultPart2 = scores[middleScoreIndex]
print('Anwser day 10 part 2:', resultPart2)
