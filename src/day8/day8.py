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

segmentsPerNum = dict() # Signal length
segmentsPerNum.setdefault(0, 'abcefg')  # 6
segmentsPerNum.setdefault(1, 'cf')  # 2
segmentsPerNum.setdefault(2, 'acdeg')  # 5
segmentsPerNum.setdefault(3, 'acdfg')  # 5
segmentsPerNum.setdefault(4, 'bcdf')  # 4
segmentsPerNum.setdefault(5, 'abdfg')  # 5
segmentsPerNum.setdefault(6, 'abdefg')  # 6
segmentsPerNum.setdefault(7, 'acf')  # 3
segmentsPerNum.setdefault(8, 'abcdefg')  # 7
segmentsPerNum.setdefault(9, 'abcdfg')  # 6

otherNumsNotToCheckPerNum = dict()
# 5,6 not using segment c;
# 2 not using segment f
otherNumsNotToCheckPerNum.setdefault(1, [5, 6, 2])
# 1, 7 not using segment b
# 5, 6 not using segment c
# 0 not using segment d
# 2 not using segment f
otherNumsNotToCheckPerNum.setdefault(4, [1, 7, 5, 6, 0, 2])
# 1, 4, not using segment a
# 6, not using segment c
# 2, not using segment f
otherNumsNotToCheckPerNum.setdefault(7, [1, 4, 6, 2])

# len of segments - sum per len
# E.g. (6 - 3) -> there are 3 numbers using 6 segments
# 2 - 1
# 3 - 1
# 4 - 1
# 5 - 3
# 6 - 3
# 7 - 1

# 1 = 2, 4 = 4, 7 = 3, 8 = 7
uniqueNums = [1, 4, 7, 8]
uniqueSegmentLengths = list(map(lambda x: len(segmentsPerNum[x]), uniqueNums))


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


def groupSegmentLengthsWithNums(nums):
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

signalsPerSegment = dict()

for note in notes:
    signals = note[UniqueSignalPatterns]
    signalsPerLength = groupSignalsByLength(signals)
    # print(signalsPerLength)

    # Process unique numbers
    numsToFind = list(filter(lambda x: not (x in uniqueNums), segmentsPerNum.keys()))
    signalsToConsider = list(filter(lambda x: not (len(x) in uniqueSegmentLengths), signals))

    for numWithUniqueSegmentLength in uniqueNums:
        segmentsForNum = segmentsPerNum.get(numWithUniqueSegmentLength)
        segmentsLen = len(segmentsForNum)
        newSignalsForNum = signalsPerLength[segmentsLen][0]
        newSignalsForNum = ''.join(sorted(newSignalsForNum))
        # print(numWithUniqueSegmentLength, segmentsLen, segmentsForNum, '->', newSignalsForNum)

        # print('before ->', signalsPerSegment)
        deleteNotPossibleSignalsForSegments(
            signalsPerSegment, segmentsForNum, newSignalsForNum)
        # print('after ->', signalsPerSegment)

    for numWithUniqueSegmentLength in uniqueNums:
        segmentsForNum = segmentsPerNum.get(numWithUniqueSegmentLength)
        segmentsLen = len(segmentsForNum)
        newSignalsForNum = signalsPerLength[segmentsLen][0]
        newSignalsForNum = ''.join(sorted(newSignalsForNum))

        if numWithUniqueSegmentLength in otherNumsNotToCheckPerNum:
            otherNumsNotToCheck = otherNumsNotToCheckPerNum[numWithUniqueSegmentLength]
            numsToCheck = list(filter(lambda x: not (x in otherNumsNotToCheck), numsToFind))
            segmentLengthsWithNums = groupSegmentLengthsWithNums(numsToCheck)
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
                    deleteNotPossibleSignalsForSegments(signalsPerSegment, segmentsForNum, consideredSignal)
                    # print('after ->', signalsPerSegment)
                    numsToFind.remove(foundNum)
                    signalsToConsider.remove(consideredSignal)

    print(numsToFind)
    print(signalsToConsider)
    # End - Process unique numbers


signalsPerUnsolvedSegments = dict()
signalPerSegment = dict()

# Test input
signalsPerUnsolvedSegments.setdefault('a', 'bd')
signalsPerUnsolvedSegments.setdefault('b', 'be')
signalsPerUnsolvedSegments.setdefault('c', 'ab')
signalsPerUnsolvedSegments.setdefault('d', 'bf')
signalsPerUnsolvedSegments.setdefault('e', 'bcdeg')
signalsPerUnsolvedSegments.setdefault('f', 'b')
signalsPerUnsolvedSegments.setdefault('g', 'bcd')
# End - Test input

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
    while True:    
        segmentToDoWith = getFirstSegmentWithOneSignalLeft(signalsPerUnsolvedSegments)
        if segmentToDoWith == None:
            break

        signalForSegment = signalsPerUnsolvedSegments[segmentToDoWith]
        signalPerSegment.setdefault(segmentToDoWith, signalForSegment)
        signalsPerUnsolvedSegments.pop(segmentToDoWith)
        deleteSignalFromSegments(signalsPerUnsolvedSegments, signalForSegment)

doStep3(signalsPerUnsolvedSegments, signalPerSegment)
# print(signalsPerUnsolvedSegments)
# print(signalPerSegment)

newConfigSignalForSegment = {v: k for k, v in signalPerSegment.items()}
# print(translateTabelSignalsPerSegment)

numPerSegments = {v: k for k, v in segmentsPerNum.items()}
# print(numPerSegments)

def sortSignals(signals):
    return ''.join(sorted(signals))

def translateSignals(signals, table):
    return ''.join(map(lambda s: table[s], signals))

outputValues = []

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
    
for note in notes:
    fourDigitSignals = note[FourDigitOutputValue]
    outputValue = getOutputValue(fourDigitSignals, newConfigSignalForSegment)
    outputValues.append(outputValue)

print(outputValues)
resultPart2 = sum(outputValues)
print('Anwser day 8 part 2:', resultPart2)
