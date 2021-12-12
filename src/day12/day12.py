# --- <Do not edit> ---
def getInputLines():
    import sys

    if len(sys.argv) < 1:
        raise ValueError('Path of this script not available in sys.argv')

    lines = []
    inputFilePath = sys.argv[0].replace('day12.py', 'input.txt')
    with open(inputFilePath) as f:
        lines = [line.strip() for line in f]

    return lines
# --- </Do not edit> ---


FromNodesIndex = 0
ToNodesIndex = 1

NodeName = 0
NodeFrom = 1
NodeTo = 2
NodeEndPath = 3


def createCaveConnection(line):
    parts = line.split('-')
    return (parts[FromNodesIndex], parts[ToNodesIndex])


def createCaveGraphNode(name):
    return (name, [], [], [])


def getNodeAndInsertIfNotExists(nodeName, nodes):
    if not (nodeName in nodes):
        newNode = createCaveGraphNode(nodeName)
        nodes.setdefault(nodeName, newNode)

    return nodes[nodeName]


def createCaveGraph(caveConnections):
    startNode = createCaveGraphNode('start')
    endNode = createCaveGraphNode('end')

    nodes = dict()
    nodes.setdefault('start', startNode)
    nodes.setdefault('end', endNode)

    for caveConnection in caveConnections:
        [fromNodeName, toNodeName] = caveConnection

        fromNode = getNodeAndInsertIfNotExists(fromNodeName, nodes)
        toNode = getNodeAndInsertIfNotExists(toNodeName, nodes)

        fromNode[NodeTo].append(toNodeName)
        toNode[NodeFrom].append(fromNodeName)

    return nodes


def printCaveGraph(graph):
    for nodeName in graph:
        node = graph[nodeName]
        nodeFromNames = ','.join(map(lambda x: x, node[NodeFrom]))
        nodeToNames = ','.join(map(lambda x: x, node[NodeTo]))
        print(nodeName, '->', nodeToNames)


def getIsBigCave(caveNode):
    nodeName = caveNode[NodeName]

    return nodeName.upper() == nodeName


def getPathsToEnd(graph, startNodeName, endNodeName):
    pathsToEnd = []

    if startNodeName == endNodeName:
        pathsToEnd.append([endNodeName])
        return pathsToEnd

    startNode = graph[startNodeName]
    toNodes = startNode[NodeTo]
    fromNodes = startNode[NodeFrom]

    pathPrefix = [startNodeName]

    for toNodeName in toNodes:
        otherPathsToEnd = getPathsToEnd(graph, toNodeName, endNodeName)
        for otherPathToEnd in otherPathsToEnd:
            path = pathPrefix + otherPathToEnd
            pathsToEnd.append(path)

    return pathsToEnd


lines = getInputLines()
caveConnections = list(map(lambda x: createCaveConnection(x), lines))
print(caveConnections)

caveGraph = createCaveGraph(caveConnections)
printCaveGraph(caveGraph)

# print(caveGraph['start'][NodeTo])

# Part 1
pathsToEnd = getPathsToEnd(caveGraph, 'start', 'end')
print(pathsToEnd)
resultPart1 = len(pathsToEnd)
print('Anwser day 12 part 1:', resultPart1)

# Part 2
resultPart2 = 0
print('Anwser day 12 part 2:', resultPart2)
