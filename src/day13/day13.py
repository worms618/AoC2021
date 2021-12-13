# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day13.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


vX = 0
vY = 1

pvEmpty = 0
pvDot = 1
pvFoldX = 2
pvFoldY = 3


def createVector(x, y):
    return (x, y)


def getDotAndFoldValues(lines):
    dotValues = []
    foldValues = []

    listToFill = dotValues
    for line in lines:
        if len(line.strip()) == 0:
            listToFill = foldValues
            continue
        listToFill.append(line)

    return (dotValues, foldValues)


def createDotVector(value):
    parts = value.split(',')
    return createVector(int(parts[0]), int(parts[1]))


def createFold(value):
    parts = str(value).replace('fold', '').replace(
        'along', '').strip().split('=')
    return (parts[0], int(parts[1]))


def getPageDimensions(dotVectors):
    xValues = []
    yValues = []
    for v in dotVectors:
        xValues.append(v[vX])
        yValues.append(v[vY])

    # The max x and y value are inclusive, so plus one
    return (max(xValues) + 1, max(yValues) + 1)


def createPage(width, height):
    page = []
    for _ in range(height):
        page.append(list(map(lambda _: pvEmpty, range(width))))
    return page


def printPage(page):
    for row in page:
        columnValues = map(lambda x: getPageChar(x), row)
        print(''.join(columnValues))

    print('')


def getPageChar(value):
    if value == pvDot:
        return '#'

    if value == pvFoldX:
        return '|'

    if value == pvFoldY:
        return '-'

    return '.'


def fillPageWithDots(page, dots):
    for dot in dots:
        (x, y) = dot
        page[y][x] = pvDot


def fillPageWithFold(page, fold):
    [axis, value] = fold
    if axis == 'x':
        fillPageWithFoldX(page, value)
    elif axis == 'y':
        fillPageWithFoldY(page, value)


def fillPageWithFoldX(page, x):
    for r in range(len(page)):
        page[r][x] = pvFoldX


def fillPageWithFoldY(page, y):
    for c in range(len(page[y])):
        page[y][c] = pvFoldY


def applyFold(page, fold):
    [axis, value] = fold
    if axis == 'x':
        return applyXAxisFold(page, value)
    elif axis == 'y':
        return applyYAxisFold(page, value)


def applyYAxisFold(page, y):
    newPage = []

    # Because fold from bottom half up
    # No need to check if lines are unaffected below the fold line

    # ignore fold line
    rowsBelowFoldLine = page[y+1:]
    expectedRows = len(rowsBelowFoldLine)
    expectedColumns = len(rowsBelowFoldLine[0])

    # Get the same amount of rows above the fold line
    # as below, while ignoring the fold line
    fromAboveLine = y - (len(page) - (y + 1))
    rowsAboveFoldLine = page[fromAboveLine:y]

    unaffectedRows = page[0: fromAboveLine]

    # reverse the lines below the fold line
    # so the order is a 'reflecting' when you:
    # fold the bottom half up
    rowsBelowFoldLine.reverse()

    newPage = unaffectedRows
    for iRow in range(expectedRows):
        newRow = []
        for iColumn in range(expectedColumns):
            valueAbove = rowsAboveFoldLine[iRow][iColumn]
            valueBelow = rowsBelowFoldLine[iRow][iColumn]
            if (valueAbove == pvDot) or (valueBelow == pvDot):
                newRow.append(pvDot)
            else:
                newRow.append(pvEmpty)
        newPage.append(newRow)

    return newPage


def applyXAxisFold(page, x):
    newPage = []

    totalColumns = len(page[0])
    totalColumnsRightOfFoldLine = totalColumns - (x + 1)
    fromLeftColumn = x - totalColumnsRightOfFoldLine

    columnsUnaffected = []
    columnsLeftOfFoldLine = []
    columnsRightOfFoldLine = []

    listToFill = columnsLeftOfFoldLine
    for iColumn in range(len(page[0])):
        # ignore fold line
        if iColumn == x:
            continue
        if iColumn < fromLeftColumn:
            listToFill = columnsUnaffected
        elif iColumn < x:
            listToFill = columnsLeftOfFoldLine
        else:
            listToFill = columnsRightOfFoldLine
        column = []
        for iRow in range(len(page)):
            value = page[iRow][iColumn]
            column.append(value)
        listToFill.append(column)

    # reverse the columns right of the fold line
    # so the order if is a 'reflecting' when you:
    # fold left
    columnsRightOfFoldLine.reverse()

    for iRow in range(len(columnsRightOfFoldLine[0])):
        newRow = []
        for iColumn in range(len(columnsUnaffected) + len(columnsLeftOfFoldLine)):
            if iColumn < fromLeftColumn:
                newRow.append(columnsUnaffected[iColumn][iRow])
            else:
                scaledIColumn = iColumn - fromLeftColumn
                valueLeft = columnsLeftOfFoldLine[scaledIColumn][iRow]
                valueRight = columnsRightOfFoldLine[scaledIColumn][iRow]
                if (valueLeft == pvDot) or (valueRight == pvDot):
                    newRow.append(pvDot)
                else:
                    newRow.append(pvEmpty)
        newPage.append(newRow)

    return newPage


def countDotsOnPage(page):
    dots = 0
    for row in page:
        dots += sum(filter(lambda x: x == pvDot, row))
    return dots


lines = getInputLines()

[dotValues, foldValues] = getDotAndFoldValues(lines)
dots = list(map(lambda x: createDotVector(x), dotValues))
folds = list(map(lambda x: createFold(x), foldValues))

# print(dots, folds)

[pageWidth, pageHeight] = getPageDimensions(dots)
print(pageWidth, pageHeight)

page = createPage(pageWidth, pageHeight)
# printPage(page)

fillPageWithDots(page, dots)
# printPage(page)

# Part 1
for fold in folds[:1]:
    fillPageWithFold(page, fold)
    # printPage(page)

    page = applyFold(page, fold)
    # printPage(page)


resultPart1 = countDotsOnPage(page)
print('Anwser day 13 part 1:', resultPart1)

# Part 2
for fold in folds[1:]:
    fillPageWithFold(page, fold)
    # printPage(page)

    page = applyFold(page, fold)
    # printPage(page)
printPage(page)
resultPart2 = 0
print('Anwser day 13 part 2:', resultPart2)
