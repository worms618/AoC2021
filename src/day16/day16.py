# --- <Do not edit> ---
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

def getPacket(bits, startBit):
    curBit = int(startBit)

    # Bit 0-2
    version = getVersion(bits, curBit)
    # Set cursor next 3 position to the right
    curBit += 3

    # Bit 3-5
    typeId = getTypeId(bits, curBit)
    curBit += 3

    if typeId == LiteravalValueTypeId:
        return getPacketWithLiteralValue(bits, version, typeId, curBit)
    else:
        return getPacketWithOperator(bits, version, typeId, curBit)

def getPacketWithLiteralValue(bits, version, typeId, startBit):
    # Literal value packets encode a single binary number
    # startBit is first bit after the header bits
    
    totalUsedBits = 6 # Basic six for the header
    groups = []
    groupSize = 5

    for i in range(startBit, len(bits), groupSize):
        group = bits[i: i + groupSize]
        firstBit = group[0]
        groupValue = group[1:groupSize]
        groups.append(groupValue)

        if firstBit == '0':
            break
    
    literalValueDecimal = ''.join(groups)
    literalValue = int(literalValueDecimal, 2)

    totalUsedBits += len(groups) * groupSize
        
    return (version, typeId, literalValue, totalUsedBits)

def getPacketWithOperator(bits, version, typeId, startBit):
    # Every other type of packet (any packet with a type ID other than 4) represent an operator 
    # that performs some calculation on one or more sub-packets contained within
    
    # startBit is first bit after the header bits
    curBit = int(startBit)

    totalUsedBits = 6 # Basic six for the header
    subPackets = []

    lengthTypeId = getLengthTypeId(bits, curBit) # bit 6 (immediately after header bits)
    curBit += 1
    totalUsedBits += 1

    if lengthTypeId == 1:
        totalOfSubPackets = getTotalOfSubPackets(bits, curBit)
        curBit += 11

        while len(subPackets) < totalOfSubPackets:
            subPacket = getPacket(bits, curBit)

            curBit += subPacket[3]
            subPackets.append(subPacket)
            totalUsedBits += subPacket[3]

    else:
        totalLengthOfBitsOfSubPacket = getTotalLengthOfBitsOfSubPackets(bits, curBit)
        curBit += 15
        
        bitsWithSubPackets = getBitsForSubPackets(bits, curBit, totalLengthOfBitsOfSubPacket)
        subPacketCurBit = 0

        while subPacketCurBit < len(bitsWithSubPackets):
            subPacket = getPacket(bitsWithSubPackets, subPacketCurBit)
            
            subPacketCurBit += subPacket[3]
            subPackets.append(subPacket)

        totalUsedBits += totalLengthOfBitsOfSubPacket

    # Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.
    return (version, typeId, subPackets, totalUsedBits)

def getVersion(bits, startBit):
    # bits 0-2; e.g. 100 -> 4; 1*2^2+0*2^1+0*2^0
    versionBits = bits[startBit:startBit + 3]

    return int(versionBits, 2)

def getTypeId(bits, startBit):
    # bits 0-2; e.g. 100 -> 4; 1*2^2+0*2^1+0*2^0
    versionBits = bits[startBit:startBit + 3]

    return int(versionBits, 2)

def getLengthTypeId(bits, startBit):
    # bits 0; e.g. 1 -> 1; 1*2^0
    lengthTypeIds = bits[startBit:startBit + 1]

    return int(lengthTypeIds, 2)

def getTotalLengthOfBitsOfSubPackets(bits, startBit):
    # If the length type ID is 0, then the next 15 bits 
    # are a number that represents the total length in bits of the sub-packets contained by this packet.

    # bits 0-15; e.g. 000000000011011 -> 27
    bits = bits[startBit:startBit + 15]

    return int(bits, 2)

def getBitsForSubPackets(bits, startBit, totalBits):
    endIndex = startBit + totalBits
    bitsForSubPackerts = bits[startBit: endIndex]

    return bitsForSubPackerts

def getTotalOfSubPackets(bits, startBit):
        # If the length type ID is 1, then the next 11 bits 
        # # are a number that represents the number of sub-packets immediately contained by this packet.
    bitsToUse = bits[startBit:startBit + 11]

    return int(bitsToUse, 2)


def getVersions(packet):
    versions = []

    version = packet[0]
    typeId = packet[1]

    versions.append(version)

    if typeId != LiteravalValueTypeId:
        subs = packet[2]
        for subPacket in subs:
            otherVersions = getVersions(subPacket)
            versions += otherVersions

    return versions

def printPositionInBits(bits, index):
    print(bits)
    prefixPointer = ''.join(map(lambda _:' ', range(index)))
    print(prefixPointer + '^')


lines = getInputLines()
inputHexadecimal = ''.join(lines)

binarysForHChars = createFourBitBinaryForHexadecimalChar()

# example of packet with literal value -> D2FE28 (hexadecimal string)
# Bits: 110100101111111000101000
# Contains are literal value
# With binary number: 011111100101
# Which is in decimal: 2021

# example of packet with operator packet -> 38006F45291200 (hexadecimal string)
# Bits: 00111000000000000110111101000101001010010001001000000000
# length type ID = 0

# example of packet with operator packet -> EE00D40C823060 (hexadecimal string)
# Bits: 11101110000000001101010000001100100000100011000001100000
# length type ID = 0

hexadecimalInBits = getBitsOfHexadecimal(inputHexadecimal, binarysForHChars)

# Part 1
print(inputHexadecimal)
print(hexadecimalInBits, '11101110000000001101010000001100100000100011000001100000' == hexadecimalInBits)

packet = getPacket(hexadecimalInBits, 0)
print(packet)
printPositionInBits(hexadecimalInBits, packet[3])

versions = getVersions(packet)
print(versions)

resultPart1 = sum(versions)
print('Anwser day 16 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 16 part 2:', resultPart2)
