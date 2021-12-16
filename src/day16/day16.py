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

    if typeId == LiteravalValueTypeId:
        return getPacketWithLiteralValue(bits, version, typeId, startBit)
    else:
        return getPacketWithOperator(bits, version, typeId)

def getVersion(bits, startBit):
    # bits 0-2; e.g. 100 -> 4; 1*2^2+0*2^1+0*2^0
    versionBits = bits[startBit:startBit + 3]

    return int(versionBits, 2)

def getTypeId(bits, startBit):
    # bits 0-2; e.g. 100 -> 4; 1*2^2+0*2^1+0*2^0
    versionBits = bits[startBit:startBit + 3]

    return int(versionBits, 2)

def getPacketWithLiteralValue(bits, version, typeId, startBit):
    # Literal value packets encode a single binary number
    print(bits, startBit)

    return (version, typeId, -1)

def getPacketWithOperator(bits, version, typeId):
    # Every other type of packet (any packet with a type ID other than 4) represent an operator 
    # that performs some calculation on one or more sub-packets contained within

    lengthTypeId = -1 # bit 6 (immediately after header bits)
    subPackets = []

    if lengthTypeId == 1:
        # If the length type ID is 1, then the next 11 bits 
        # # are a number that represents the number of sub-packets immediately contained by this packet.
        lengthTypeId = 1
    else:
        # If the length type ID is 0, then the next 15 bits 
        # are a number that represents the total length in bits of the sub-packets contained by this packet.
        lengthTypeId = 0

    # Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.
    
    return (version, typeId, subPackets)

def getVerions(packet):
    versions = []

    version = packet[0]
    typeId = packet[1]

    versions.append(version)

    if typeId != LiteravalValueTypeId:
        subs = packet[2]
        for subPacket in subs:
            otherVersions = getVerions(subPacket)
            versions += otherVersions

    return versions


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
print(hexadecimalInBits, '110100101111111000101000' == hexadecimalInBits)

packet = getPacket(hexadecimalInBits, 0)
print(packet)

versions = getVerions(packet)
print(versions)

resultPart1 = sum(versions)
print('Anwser day 16 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 16 part 2:', resultPart2)
