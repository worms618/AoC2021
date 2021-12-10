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


UniqueSignalPatterns = 0
FourDigitOutputValue = 1

segmentsPerNumber = dict() # Signal length
segmentsPerNumber.setdefault(0, 'abcefg')  # 6
segmentsPerNumber.setdefault(1, 'cf')  # 2
segmentsPerNumber.setdefault(2, 'acdeg')  # 5
segmentsPerNumber.setdefault(3, 'acdfg')  # 5
segmentsPerNumber.setdefault(4, 'bcdf')  # 4
segmentsPerNumber.setdefault(5, 'abdfg')  # 5
segmentsPerNumber.setdefault(6, 'abdefg')  # 6
segmentsPerNumber.setdefault(7, 'acf')  # 3
segmentsPerNumber.setdefault(8, 'abcdefg')  # 7
segmentsPerNumber.setdefault(9, 'abcdfg')  # 6

otherNumbersNotToCheckPerNumber = dict()
# 5,6 not using segment c;
# 2 not using segment f
otherNumbersNotToCheckPerNumber.setdefault(1, [5, 6, 2])
# 1, 7 not using segment b
# 5, 6 not using segment c
# 0 not using segment d
# 2 not using segment f
otherNumbersNotToCheckPerNumber.setdefault(4, [1, 7, 5, 6, 0, 2])
# 1, 4, not using segment a
# 6, not using segment c
# 2, not using segment f
otherNumbersNotToCheckPerNumber.setdefault(7, [1, 4, 6, 2])

# len of segments - sum per len
# E.g. (6 - 3) -> there are 3 numbers using 6 segments
# 2 - 1
# 3 - 1
# 4 - 1
# 5 - 3
# 6 - 3
# 7 - 1

# 1 = 2, 4 = 4, 7 = 3, 8 = 7
uniqueNumbers = [1, 4, 7, 8]
uniqueSegmentLengths = list(map(lambda x: len(segmentsPerNumber[x]), uniqueNumbers))


def parseNote(line):
    parts = line.split('|')
    return (parts[0].strip().split(' '), parts[1].strip().split(' '))


def groupSignalsByLength(signals):
    signalsByLen = dict()

    for signal in signals:
        signalLen = len(signal)

        if not (signalLen in signalsByLen):
            signalsByLen.setdefault(signalLen, [])

        signalsByLen[signalLen].append(signal)

    return signalsByLen


def deleteNotPossibleSignalsForSegments(signalsPerSegment, segments, possibleSignals):
    for segment in segments:
        if not (segment in signalsPerSegment):
            signalsPerSegment.setdefault(segment, possibleSignals)
        else:
            currentPossibleSignals = signalsPerSegment[segment]
            newPossibleSignals = ''
            for currentPossibleSignal in currentPossibleSignals:
                if currentPossibleSignal in possibleSignals:
                    newPossibleSignals += currentPossibleSignal
            signalsPerSegment[segment] = newPossibleSignals

    return signalsPerSegment


def groupSegmentLengthsWithNums(nums, segmentsPerNum):
    segmentLengthsWithNums = dict()

    for num in nums:
        segmentLength = len(segmentsPerNum[num])
        if not (segmentLength in segmentLengthsWithNums):
            segmentLengthsWithNums.setdefault(segmentLength, [])
        segmentLengthsWithNums[segmentLength].append(num)

    return segmentLengthsWithNums


def check(signal, newSignalsForNum):
    isValid = True

    for s in newSignalsForNum:
        isValid = isValid & (s in signal)

    return isValid


lines = getInputLines()

notes = list(map(lambda x: parseNote(x), lines))
# print(notes)
# Part 1

resultPart1 = 0

for note in notes:
    for output in note[FourDigitOutputValue]:
        if (len(output) in uniqueSegmentLengths):
            resultPart1 += 1

print('Anwser day 8 part 1:', resultPart1)

# Part 2

def sortSignals(signals):
    return ''.join(sorted(signals))
# Test input

def doStep1(segmentsPerNum, otherNumsNotToCheckPerNum, uniqueNums, numsToFind, signalsToConsider, signalsPerLength, signalsPerUnsolvedSegments):
    for numWithUniqueSegmentLength in uniqueNums:
        segmentsForNum = segmentsPerNum.get(numWithUniqueSegmentLength)
        segmentsLen = len(segmentsForNum)
        newSignalsForNum = signalsPerLength[segmentsLen][0]
        newSignalsForNum = ''.join(sorted(newSignalsForNum))
        # print(numWithUniqueSegmentLength, segmentsLen, segmentsForNum, '->', newSignalsForNum)

        # print('before ->', signalsPerSegment)
        deleteNotPossibleSignalsForSegments(signalsPerUnsolvedSegments, segmentsForNum, newSignalsForNum)
        # print('after ->', signalsPerSegment)

    for numWithUniqueSegmentLength in uniqueNums:
        segmentsForNum = segmentsPerNum.get(numWithUniqueSegmentLength)
        segmentsLen = len(segmentsForNum)
        newSignalsForNum = signalsPerLength[segmentsLen][0]
        newSignalsForNum = ''.join(sorted(newSignalsForNum))

        if numWithUniqueSegmentLength in otherNumsNotToCheckPerNum:
            otherNumsNotToCheck = otherNumsNotToCheckPerNum[numWithUniqueSegmentLength]
            numsToCheck = list(filter(lambda x: not (x in otherNumsNotToCheck), numsToFind))
            segmentLengthsWithNums = groupSegmentLengthsWithNums(numsToCheck, segmentsPerNumber)
            sortedSegmentLengths = sorted(segmentLengthsWithNums.keys())
            for segmentLength in sortedSegmentLengths:
                signalsForLength = signalsPerLength[segmentLength]
                SegmentLengthForNums = segmentLengthsWithNums[segmentLength]
                signalsForLengthToCheck = list(filter(lambda x: x in signalsToConsider, signalsForLength))

                signalsToUse = list(filter(lambda x: check(x, newSignalsForNum), signalsForLengthToCheck))
                if len(signalsToUse) == 1 & len(SegmentLengthForNums) == 1:
                    # print('before ->', signalsPerSegment)
                    foundNum = SegmentLengthForNums[0]
                    segmentsForNum = segmentsPerNum[foundNum]
                    consideredSignal = signalsToUse[0]
                    # print(foundNum, segmentsForNum, consideredSignal)
                    deleteNotPossibleSignalsForSegments(signalsPerUnsolvedSegments, segmentsForNum, consideredSignal)
                    # print('after ->', signalsPerSegment)
                    numsToFind.remove(foundNum)
                    signalsToConsider.remove(consideredSignal)    

def getNumToFindWithUniqueSegmentLength(numsToFind, segmentsPerNum):
    segmentLenPerNums = list(map(lambda x: len(segmentsPerNum[x]), numsToFind))
    groupedSegmentLens = dict()
    for i in range(len(segmentLenPerNums)):
        segmentLen = segmentLenPerNums[i]
        num = numsToFind[i]
        if not (segmentLen in groupedSegmentLens):
            groupedSegmentLens[segmentLen] = []
        
        groupedSegmentLens[segmentLen].append(num)
    
    for length in groupedSegmentLens:
        if len(groupedSegmentLens[length]) == 1:
            return groupedSegmentLens[length][0]

    return None

def deleteSignalCharPerSegmentWhichNotInNewSignal(signalPerSegment, originalSignal, newSignal):
    for segment in signalPerSegment:
        signal = signalPerSegment[segment]
        if segment in originalSignal:
            newSignalForSegmentChars = list(filter(lambda x: x in newSignal, signal))            
            newSignalForSegment = ''.join(newSignalForSegmentChars)
            signalPerSegment[segment] = newSignalForSegment

def doStep2(signalPerSegment, numsToFind, signalsToConsider, segmentsPerNum):
    # Look if a number to find, with a unique segment length is leftover
    # If so, that one is linked to the signalToConsider with the same length
    while True:
        numToCheck = getNumToFindWithUniqueSegmentLength(numsToFind, segmentsPerNum)
        if numToCheck == None:
            break
        numsToFind.remove(numToCheck)
        originalSignal = segmentsPerNum[numToCheck]
        numToCheckSegmentLength = len(originalSignal)
        signalToConsider = list(filter(lambda x: len(x) == numToCheckSegmentLength, signalsToConsider))[0]
        signalsToConsider.remove(signalToConsider)
        # print(numToCheck, originalSignal, sortSignals(signalToConsider))
        deleteSignalCharPerSegmentWhichNotInNewSignal(signalPerSegment, originalSignal, signalToConsider)

# print('After part 2')
# print(signalsPerUnsolvedSegments)
# print(signalPerSegment)
# print(numsToFind)
# print(signalsToConsider)

# # End - Test input

def getUnsolvedSegment(segments, solvedSegments):
    return list(filter(lambda x: not (x in solvedSegments), segments))

def getFirstSegmentWithOneSignalLeft(signalsPerSegment):
    for segment in signalsPerSegment:
        signalsLeft = signalsPerSegment[segment]
        if len(signalsLeft) == 1:
            return segment

    return None

def deleteSignalFromSegments(signalsPerSegment, signal):
    for segment in signalsPerSegment:
        signals = signalsPerSegment[segment]
        signals = ''.join(filter(lambda x: not (x in signal), signals))
        signalsPerSegment[segment] = signals

def doStep3(signalsPerUnsolvedSegments, signalPerSegment):
    # Check if an unsolved segment has a possible signal with 1 char left
    # If so, delete that char at the other segment possible chars
    while True:    
        segmentToDoWith = getFirstSegmentWithOneSignalLeft(signalsPerUnsolvedSegments)
        if segmentToDoWith == None:
            break

        signalForSegment = signalsPerUnsolvedSegments[segmentToDoWith]
        signalPerSegment.setdefault(segmentToDoWith, signalForSegment)
        signalsPerUnsolvedSegments.pop(segmentToDoWith)
        deleteSignalFromSegments(signalsPerUnsolvedSegments, signalForSegment)


# print(signalsPerUnsolvedSegments)
# print(signalPerSegment)

def translateSignals(signals, table):
    return ''.join(map(lambda s: table[s], signals))

def getOutputValue(fourDigitSignals, configSignalForSegment):
    digits = []
    for digitSignals in fourDigitSignals:
        translated = translateSignals(digitSignals, configSignalForSegment)
        sTranslated = sortSignals(translated)
        # print(digitSignals, translated, sTranslated)
        num = numPerSegments[sTranslated]
        digits.append(num)
    # print(digits)
    return int(''.join(map(lambda x: str(x), digits)))

outputValues = []
for note in notes:
    signals = note[UniqueSignalPatterns]
    fourDigitSignals = note[FourDigitOutputValue]

    signalsPerLength = groupSignalsByLength(signals)
    # print(signalsPerLength)

    # Process unique numbers
    numbersToFind = list(filter(lambda x: not (x in uniqueNumbers), segmentsPerNumber.keys()))
    signalsToConsider = list(filter(lambda x: not (len(x) in uniqueSegmentLengths), signals))

    signalsPerUnsolvedSegments = dict()
    signalsPerSegment = dict()
    
    doStep1(segmentsPerNumber, otherNumbersNotToCheckPerNumber, 
            uniqueNumbers, numbersToFind, 
            signalsToConsider, signalsPerLength, signalsPerUnsolvedSegments)

    # print('--- after step 1 --- ')
    # print(numbersToFind)
    # print(signalsToConsider)
    # print(signalsPerUnsolvedSegments)
    # print(signalsPerSegment)

    doStep2(signalsPerUnsolvedSegments, numbersToFind, signalsToConsider, segmentsPerNumber)
    
    # print('--- after step 2 --- ')
    # print(numbersToFind)
    # print(signalsToConsider)
    # print(signalsPerUnsolvedSegments)
    # print(signalsPerSegment)

    doStep3(signalsPerUnsolvedSegments, signalsPerSegment)
    # print('--- after step 3 --- ')
    # print(numbersToFind)
    # print(signalsToConsider)
    # print(signalsPerUnsolvedSegments)
    # print(signalsPerSegment)
    
    newConfigSignalForSegment = {v: k for k, v in signalsPerSegment.items()}
    # print(translateTabelSignalsPerSegment)

    numPerSegments = {v: k for k, v in segmentsPerNumber.items()}
    # print(numPerSegments)
    outputValue = getOutputValue(fourDigitSignals, newConfigSignalForSegment)
    
    outputValues.append(outputValue)

    # print(numsToFind)
    # print(signalsToConsider)
    # End - Process unique numbers

# print(outputValues)
resultPart2 = sum(outputValues)
print('Anwser day 8 part 2:', resultPart2)
