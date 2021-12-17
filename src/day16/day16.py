# --- <Do not edit> ---
from sys import version


def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day16.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


LiteravalValueTypeId = 4


def createFourBitBinaryForHexadecimalChar():
    binaryForChar = dict()
    binaryForChar.setdefault('0', '0000')
    binaryForChar.setdefault('1', '0001')
    binaryForChar.setdefault('2', '0010')
    binaryForChar.setdefault('3', '0011')
    binaryForChar.setdefault('4', '0100')
    binaryForChar.setdefault('5', '0101')
    binaryForChar.setdefault('6', '0110')
    binaryForChar.setdefault('7', '0111')
    binaryForChar.setdefault('8', '1000')
    binaryForChar.setdefault('9', '1001')
    binaryForChar.setdefault('A', '1010')
    binaryForChar.setdefault('B', '1011')
    binaryForChar.setdefault('C', '1100')
    binaryForChar.setdefault('D', '1101')
    binaryForChar.setdefault('E', '1110')
    binaryForChar.setdefault('F', '1111')
    return binaryForChar


def getBitsOfHexadecimal(hexadecimal, binaryForChar):
    return ''.join(map(lambda x: binaryForChar[x], hexadecimal))


def mPop(collection, startIndex, endIndex):
    subCollection = []
    for _ in range(startIndex, endIndex):
        element = collection.pop(0)
        subCollection.append(element)

    return subCollection


def getDecimalValue(bitsInList):
    bitsInStr = ''.join(bitsInList)
    return int(bitsInStr, 2)


def getPacket(bits):
    versionBits = mPop(bits, 0, 3)
    typeIdBits = mPop(bits, 0, 3)
    
    typeId = getDecimalValue(typeIdBits)

    if typeId == LiteravalValueTypeId:
        return getPacketWithLiteralValue(bits, versionBits, typeIdBits)
    else:
        return getPacketWithOperator(bits, versionBits, typeIdBits)


def getPacketWithLiteralValue(bits, versionBits, typeIdBits):
    # Literal value packets encode a single binary number
    # startBit is first bit after the header bits
    groups = []
    groupSize = 5

    while len(bits) > 0:
        group = mPop(bits, 0, groupSize)
        groupFirstBit = group[0]
        groups.append(group)

        if groupFirstBit == '0':
            break
    
    literalValueGroup = list(map(lambda x: x[1:], groups))
    literalValueInBits = ''.join(map(lambda x: ''.join(x), literalValueGroup))
    literalValue = getDecimalValue(literalValueInBits)

    return (versionBits, typeIdBits, literalValue, groups, literalValueGroup)


def getPacketWithOperator(bits, versionBits, typeIdBits):
    # Every other type of packet (any packet with a type ID other than 4) represent an operator
    # that performs some calculation on one or more sub-packets contained within

    subPackets = []

    lengthTypeIdBits = mPop(bits, 0, 1)
    lengthTypeId = getDecimalValue(lengthTypeIdBits)

    subPacketDefinitionBits = []
    subPacketDefinitionValue = -1
    subPacketBits = []

    if lengthTypeId == 1:
        subPacketDefinitionBits = mPop(bits, 0, 11)
        subPacketDefinitionValue = getDecimalValue(subPacketDefinitionBits)
    
        while len(subPackets) < subPacketDefinitionValue:
            if len(bits) < 11:
                raise ValueError('Did not satisfy amount of requested subpacket')
            
            subPacket = getPacket(bits)
            subPackets.append(subPacket)

    else:
        subPacketDefinitionBits = mPop(bits, 0, 15)
        subPacketDefinitionValue = getDecimalValue(subPacketDefinitionBits)

        subPacketBits = mPop(bits, 0, subPacketDefinitionValue)

        # Greater than 11, because literal value packet needs atleast 11 digits
        # Header needs atleast 6 and literal value bits need to be atleast 5
        while len(subPacketBits) >= 11:
            subPacket = getPacket(subPacketBits)
            subPackets.append(subPacket)

    # # Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.
    return (versionBits, typeIdBits, subPackets, 
    lengthTypeIdBits, subPacketDefinitionBits, subPacketBits)

def getTotalLengthOfBitsOfSubPackets(bits, startBit):
    # If the length type ID is 0, then the next 15 bits
    # are a number that represents the total length in bits of the sub-packets contained by this packet.

    # bits 0-15; e.g. 000000000011011 -> 27
    bits = bits[startBit:startBit + 15]

    return int(bits, 2)

def getVersions(packet):
    versions = []

    versionBits = packet[0]
    typeIdBits = packet[1]

    version = getDecimalValue(versionBits)
    typeId = getDecimalValue(typeIdBits)

    versions.append(version)
    if typeId != LiteravalValueTypeId:
        subs = packet[2]
        for subPacket in subs:
            otherVersions = getVersions(subPacket)
            versions += otherVersions

    return versions

def packetToString(packet):
    versionBits = packet[0]
    typeIdBits = packet[1]

    versionPart = ''.join(versionBits)
    typeIdParts = ''.join(typeIdBits)

    typeId = getDecimalValue(typeIdBits)
    if typeId == LiteravalValueTypeId:
        return packetLiteralValueToString(packet, versionPart, typeIdParts)
    else:
        return packetOperatorToString(packet, versionPart, typeIdParts)

def packetLiteralValueToString(packet, version, typeId):
    groups = packet[3]
    parts = [version, typeId] + list(map(lambda x: ''.join(x), groups))
    return '|'.join(parts)

def packetOperatorToString(packet, version, typeId):
    subPackets = packet[2]
    lengthTypeBits = packet[3]
    subPacketDefinitionBits = packet[4]

    lengthTypeIdPart = ''.join(lengthTypeBits)
    subPacketDefinitionPart = ''.join(subPacketDefinitionBits)

    parts = [version, typeId, lengthTypeIdPart, subPacketDefinitionPart]
    for subPacket in subPackets:
        subPacketInStr = packetToString(subPacket)
        parts.append(subPacketInStr)
    
    return '|'.join(parts)

def getPacketResult(packet):

    return 0


lines = getInputLines()
inputHexadecimal = ''.join(lines)

binarysForHChars = createFourBitBinaryForHexadecimalChar()

hexadecimalInBits = getBitsOfHexadecimal(inputHexadecimal, binarysForHChars)

# print(inputHexadecimal)

hexadecimalInBitsAsList = list(hexadecimalInBits)
packet = getPacket(hexadecimalInBitsAsList.copy())

# print(packet)

# print(''.join(hexadecimalInBitsAsList))
# print(packetToString(packet))

# Part 1
versions = getVersions(packet)
# print(versions)
resultPart1 = sum(versions)
print('Anwser day 16 part 1:', resultPart1)

# Part 2 
resultPart2 = getPacketResult(packet)
print('Anwser day 16 part 2:', resultPart2)
