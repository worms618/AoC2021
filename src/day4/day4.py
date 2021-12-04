# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day4.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


numGrid = 0
boolGrid = 1
boolGridColumns = 2


def createBoard(boardLines):
    numGrid = []
    boolGrid = []
    boolGridColumns = []

    # First line is empty
    for line in boardLines[1::]:
        # Split the line by space
        # Filter out all whitespace only elements
        # Whitespace only element when element is stripped and length did become zero
        numsInStr = list(filter(lambda x: len(x.strip()) > 0, line.split(' ')))
        numLine = list(map(int, numsInStr))
        numGrid.append(numLine)
        # Create a line of falses for each number
        boolLine = [False for i in range(0, len(numLine))]
        boolGrid.append(boolLine)

    # Convert boolGrid to boolGridColumns
    for c in range(len(boolGrid[0])):
        numLine = []
        for r in range(len(boolGrid)):
            numLine.append(boolGrid[r][c])
        boolGridColumns.append(numLine)

    return (numGrid, boolGrid, boolGridColumns)


def doMarkNumber(board, number):
    row = -1
    column = -1

    for r in range(len(board[numGrid])):
        for c in range(len(board[numGrid][r])):
            if board[numGrid][r][c] == number:
                row = r
                column = c
                break

    if row >= 0 & column >= 0:
        board[boolGrid][row][column] = True
        board[boolGridColumns][column][row] = True

    return


def boardHasFilledRowOrColumn(board):
    # Check rows
    for r in range(len(board[boolGrid])):
        if allTrue(board[boolGrid][r]):
            return True

    # Check Columns
    for c in range(len(board[boolGridColumns])):
        if allTrue(board[boolGridColumns][c]):
            return True

    return False


def allTrue(collection):
    # Filter out all elements with value True
    # When resulting collection is empty, everything had value True
    return len(list(filter(lambda x: x != True, collection))) == 0


def getUnmarkedNumbers(board):
    unmarkedNumbers = []

    for r in range(len(board[boolGrid])):
        for c in range(len(board[boolGrid][r])):
            if not board[boolGrid][r][c]:
                unmarkedNumbers.append(board[numGrid][r][c])

    return unmarkedNumbers


lines = getInputLines()

drawNumbersLine = lines[0]
# get everything starting at index 1
boardLines = lines[1::]

# print(boardLines)

drawNumbers = list(map(int, drawNumbersLine.split(',')))
# Splice the boardLines into chunks of 6
rawBoards = [boardLines[i:i+6] for i in range(0, len(boardLines), 6)]

# print(drawNumbers)
# print(rawBoards)

boards = list(map(lambda x: createBoard(x), rawBoards))

# idea is to have 2 2d grids, one containing the numbers and one containing booleans
# When a number is draw, mark the boolean field

# Part 1

part1Boards = boards.copy()
winningBoard = None
numberLetToWin = -1

for drawNumber in drawNumbers:
    for board in part1Boards:
        doMarkNumber(board, drawNumber)
        if boardHasFilledRowOrColumn(board):
            numberLetToWin = drawNumber
            winningBoard = board
            break

    if winningBoard != None:
        break

# print('0', boards[0])
# print('1', boards[1])
# print('2', boards[2])

# print('Winningboard')
# print(winningBoard[numGrid])
# print(winningBoard[boolGrid])
# print(winningBoard[boolGridColumns])

# print('numberLetToWin', numberLetToWin)

unmarkedNumbers = getUnmarkedNumbers(winningBoard)
# print('unmarkedNumbers', unmarkedNumbers)

sumUnmarkedNumbers = sum(unmarkedNumbers)
# print('sumUnmarkedNumbers', sumUnmarkedNumbers)

resultPart1 = numberLetToWin * sumUnmarkedNumbers
print('Anwser day 4 part 1:', resultPart1)

# Part 2
winningBoard = None
numberLetToWin = -1

part2Boards = boards.copy()

for drawNumber in drawNumbers:
    for board in part2Boards:
        doMarkNumber(board, drawNumber)

    lastRemovedBoard = None
    for board in part2Boards:
        if boardHasFilledRowOrColumn(board):
            part2Boards.remove(board)
            lastRemovedBoard = board
    
    if len(part2Boards) == 0:
        winningBoard = lastRemovedBoard
        numberLetToWin = drawNumber
        break

# print('numberLetToWin', numberLetToWin)

unmarkedNumbers = getUnmarkedNumbers(winningBoard)
# print('unmarkedNumbers', unmarkedNumbers)

sumUnmarkedNumbers = sum(unmarkedNumbers)
# print('sumUnmarkedNumbers', sumUnmarkedNumbers)

resultPart2 = numberLetToWin * sumUnmarkedNumbers
print('Anwser day 4 part 2:', resultPart2)
