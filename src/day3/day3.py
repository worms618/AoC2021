# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day3.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---

def countCharactersAtIndex(values, index):
    counter = {}

    for chars in map(lambda x: list(x), values):
        charAtIndex = chars[index]
        if not charAtIndex in counter:
            counter.setdefault(charAtIndex, 0)
        
        counter[charAtIndex] = counter[charAtIndex] + 1

    return counter

def countCharactersPerIndex(values):
    counter = []
    totalCharsPerValue = len(values[0])

    for index in range(totalCharsPerValue):
        counter.append(countCharactersAtIndex(values, index))

    return counter

def getGammaRate(values):
    charsPerIndex = countCharactersPerIndex(values)
    gammaRate = ""

    for charsAtIndex in charsPerIndex:
        nextValue = ""
        nextValueOccures = 0
        for char in charsAtIndex:
            if charsAtIndex[char] > nextValueOccures:
                nextValue = char
                nextValueOccures = charsAtIndex[char]
        
        gammaRate = gammaRate + nextValue

    return gammaRate

def getEpsilonRate(values):
    charsPerIndex = countCharactersPerIndex(values)
    epsilonRate = ""

    for charsAtIndex in charsPerIndex:
        nextValue = ""
        nextValueOccures = -1
        for char in charsAtIndex:
            if (nextValueOccures < 0) | (charsAtIndex[char] < nextValueOccures):
                nextValue = char
                nextValueOccures = charsAtIndex[char]
        epsilonRate = epsilonRate + nextValue

    return epsilonRate

def getOxygenGeneratorRating(values):
    cValues = values.copy()

    charIndex = 0
    while (len(cValues) > 1) & (charIndex < len(values[0])):
        charsAtIndex = countCharactersAtIndex(cValues, charIndex)
        nextValue = ""
        nextValueOccures = 0
        for char in charsAtIndex:
            if charsAtIndex[char] > nextValueOccures:
                nextValue = char
                nextValueOccures = charsAtIndex[char]
            elif charsAtIndex[char] == nextValueOccures:
                nextValue = "1"
        
        newValues = []
        for line in cValues:
            if line[charIndex] == nextValue:
                newValues.append(line)
        
        cValues = newValues.copy()
        charIndex = charIndex + 1
    
    return cValues[0]

def getCO2ScrubberRating(values):
    cValues = values.copy()

    charIndex = 0
    while (len(cValues) > 1) & (charIndex < len(values[0])):
        charsAtIndex = countCharactersAtIndex(cValues, charIndex)
        nextValue = ""
        nextValueOccures = -1
        for char in charsAtIndex:
            if (nextValueOccures < 0) | (charsAtIndex[char] < nextValueOccures):
                nextValue = char
                nextValueOccures = charsAtIndex[char]
            elif charsAtIndex[char] == nextValueOccures:
                nextValue = "0"
        
        newValues = []
        for line in cValues:
            if line[charIndex] == nextValue:
                newValues.append(line)
        
        cValues = newValues.copy()
        charIndex = charIndex + 1
    return cValues[0]

def binaryToInt(value):
    return int(value, 2)

lines = getInputLines()

# Part 1

gammaRateInBinary = getGammaRate(lines)
epsilonRateInBinary = getEpsilonRate(lines)
# print(gammaRateInBinary, epsilonRateInBinary)

gammaRate = binaryToInt(gammaRateInBinary)
epsilonRate = binaryToInt(epsilonRateInBinary)
# print(gammaRate, epsilonRate)

resultPart1 = gammaRate * epsilonRate
print('Anwser day 3 part 1:', resultPart1)

# Part 2

oxygenGeneratorRatingInBinary = getOxygenGeneratorRating(lines)
CO2ScrubberRatingInBinary = getCO2ScrubberRating(lines)
# print(oxygenGeneratorRatingInBinary, CO2ScrubberRatingInBinary)

oxygenGeneratorRating = binaryToInt(oxygenGeneratorRatingInBinary)
CO2ScrubberRating = binaryToInt(CO2ScrubberRatingInBinary)
# print(oxygenGeneratorRating, CO2ScrubberRating)

resultPart2 = oxygenGeneratorRating * CO2ScrubberRating
print('Anwser day 3 part 2:', resultPart2)
