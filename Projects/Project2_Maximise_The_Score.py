from timeit import default_timer as timer
import sys


# 2801 A2 - 20%
# due Week 11 - Friday, june 3

# if sys.argv[1] != "input.txt":
#     print("<Incorrect file name>\ninput:python3 s5240487_Maximise_The_Score input.txt")
#     quit()

# 2i
def leftChild(heapList, i):
    if (2 * i) < len(heapList) and i >= 1:
        return 2 * i
    return -1


# 2i + 1
def rightChild(heapList, i):
    if (2 * i) + 1 < len(heapList) and i >= 1:
        return (2 * i) + 1
    return -1


def maxHeapify(heapList, i):
    leftChildIndex = leftChild(heapList, i)
    rightChildIndex = rightChild(heapList, i)
    largest = i

    # if left child is larger than root
    if currentHeapSize >= leftChildIndex > 0:
        if heapList[leftChildIndex] > heapList[largest]:
            largest = leftChildIndex

    # if right child is larger than root
    if currentHeapSize >= rightChildIndex > 0:
        if heapList[rightChildIndex] > heapList[largest]:
            largest = rightChildIndex

    # if largest is not root
    if largest != i:
        heapList[i], heapList[largest] = heapList[largest], heapList[i]
        maxHeapify(heapList, largest)


def extractMaxNode(heapList):
    global currentHeapSize
    root = heapList[1]
    heapList[1] = heapList[currentHeapSize]
    currentHeapSize -= 1
    maxHeapify(heapList, 1)
    return root


def percolateItemUp(heapList, i, k):
    # i // 2 == parent
    heapList[i] = k
    while i > 1 and heapList[i // 2] < heapList[i]:
        heapList[i], heapList[i // 2] = heapList[i // 2], heapList[i]
        i = i // 2


def insert(heapList, k):
    global currentHeapSize
    currentHeapSize += 1
    percolateItemUp(heapList, currentHeapSize, k)


def digitSum(n):
    ds = 0
    for d in str(n):
        ds += int(d)
    return ds


with open("input.txt", "r", encoding="utf-8") as fd:
    testCases = fd.readlines()

# add file content 3 lines at a time
a, b = 1, 4
fileImport = {}
for i in range(1, 11):
    fileImport[f'Test case {i}'] = testCases[a:b]
    a = b
    b += 3

# create the variables and convert to correct format ints and string
testCaseContainer = {}
t = 1
for item in fileImport.values():
    n, k = item[0].split()
    weights = [int(i) for i in item[1].split()]
    player = item[2].strip()
    testCase = [int(n), int(k), weights, player]
    testCaseContainer[f'Test case {t}'] = testCase
    t += 1

# loop through dict to run the test cases
currentHeapSize = 0
rustyScore, scottScore = 0, 0
for caseNum in range(len(testCaseContainer)):
    digitSumNodes = []

    # extract data from the test case
    numNodes, numTurns, nodeWeights, player = testCaseContainer[f'Test case {caseNum + 1}']

    # fill rusty list with tuple data (sum, num)
    for num in nodeWeights:
        dSum = digitSum(num)
        digitSumNodes.append((dSum, num))

    # decide starting player
    if player == 'TAILS':
        player = 'Rusty'
    else:
        player = 'Scott'

    print(f'Test case {caseNum + 1}')
    start = timer()
    while numNodes > 0:
        if player == 'Rusty':

            # init tree
            maxHeap = [None] * (numNodes + 1)

            # fill rusty maxheap with correct tuple data
            for item in digitSumNodes:
                insert(maxHeap, item)

            # adjust nodes to pick, to that of the available nodes
            if numNodes < numTurns:
                numTurns = numNodes

            # extract max node numTurns times
            for i in range(1, numTurns + 1):
                extracted = extractMaxNode(maxHeap)
                rustyScore += extracted[1]

                # # remove node from pool
                if extracted in digitSumNodes:
                    # remove the tuple value from the
                    nodeWeights.remove(extracted[1])
                    digitSumNodes.remove(extracted)

            # adjust nodes available in the pool, reset heap size, change player
            numNodes -= numTurns
            currentHeapSize = 0
            player = 'Scott'

        elif player == 'Scott':

            # init tree
            maxHeap = [None] * (numNodes + 1)

            # fill heap with node values
            for item in nodeWeights:
                insert(maxHeap, item)

            # adjust nodes to pick, to that of the available nodes
            if numNodes < numTurns:
                numTurns = numNodes

            # extract balls k turns times
            for i in range(1, numTurns + 1):
                extracted = extractMaxNode(maxHeap)
                scottScore += extracted

                # remove nodes from lists
                if extracted in nodeWeights:
                    nodeWeights.remove(extracted)

                    # locates the index of extracted node within the tuple
                    extractedLocationInTuple = [nodeValue[1] for nodeValue in digitSumNodes].index(extracted)
                    digitSumNodes.pop(extractedLocationInTuple)

            # adjust nodes available in the pool, reset heap size, change player
            numNodes -= numTurns
            currentHeapSize = 0
            player = 'Rusty'

    stop = timer()
    print(f'Scott:{scottScore}\nRusty:{rustyScore}')

    print(f'Finished in {stop - start:0.5f} seconds')
    print('==============')
    rustyScore = 0
    scottScore = 0
