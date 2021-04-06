from numpy.lib.scimath import sqrt
import sys

class Graph:
    def __init__(self, nodes):
        self._num = nodes[0].getNum()       # banyak node
        self._nodeList = [nodes[i] for i in range(self._num)]   # list of nodes

        self._matrix = [[-1 for j in range(getNum())] for i in range(getNum())]
        constructMatrix()

        self._dictionary = {}
        constructDictionary()

    def constructMatrix(self):
        for i in range(getNum()):
            for j in range(0, i):
                distance = getNode(i).euclidean(getNode(j))
                self._matrix[i][j] = distance
                self._matrix[j][i] = distance
    
    def constructDictionary(self):
        i = 0
        for node in self._nodeList:
            self._dictionary.update({node.getName(): i})
            i += 1

    def resetNodes(self):
        for i in range(getNum()):
            self._nodeList[i].resetVal()
    

    # [internal] getter
    def getNum(self):
        return self._num
    def getNode(self, i):
        return self._nodeList[i]
    def getIndex(self, node):
        return self._dictionary[node]
    def getWeight(self, i, j):
        return self._matrix[i][j]

    # node h g f setter
    def updateVal(self, currentNode, prec, goal):
        # currentNode, prec, goal: string, valid
        # currentNode dievaluasi dari prec node ke goal node
        idxCurrentNode = getIndex(currentNode)
        idxPrec = getIndex(prec)
        idxGoal = getIndex(goal)
        currentNode.setGVal(getNode(idxPrec).getGVal() + currentNode.getGVal())
    
    ### A* Algorithm ###
    def aStar(self, startNode, goalNode):
        # Prekondisi: startNode (string) dan goalNode (string) valid
        # Mengembalikan list yang berisi jalur dari startNode ke goalNode. [] jika tidak ada
        # f = g + h
        if (startNode == goalNode):
            return [startNode]

        closedList = [False for i in range(getNum())]
        openList = PrioQueue()
        path = []
        idxGoalNode = getIndex(goalNode)

        idxCurrentNode = getIndex(startNode)
        getNode(idxCurrentNode).setGVal(0)
        openList.enqueue((idxCurrentNode, getNode(idxCurrentNode).getFVal()))

        while openList.getSize() > 0:
            idxCurrentNode = openList.dequeue()[0]
            if idxCurrentNode == idxGoalNode:
                return
            
            closedList[idxCurrentNode] = True

            for k in range(getNum()):
                adjacentDistance = getWeight(idxCurrentNode, k)
                if (adjacentDistance > 0):
                    if closedList[k]:
                        continue

                    cost = getNode(idxCurrentNode).getGVal() + adjacentDistance
                    if openList.hasNode(k) and cost < getNode(k).getGVal():
                        # n in openList and path to k through currentNode < path to n previously
                        openList.removeNode(k)
                    if closedList[k] == True and cost < getNode(k).getGVal():
                        # n in closedList and path to k through currentNode < path to n previously
                        closedList[k] = False
                    if not (openList.hasNode(k)) and closedList[k] == False:
                        openList.enqueue(k, getNode(k).getFVal())
                        getNode(k).setGVal(cost)
                        getNode(k).setHVal(getNode(idxGoalNode))
                        getNode(k).setFVal()


        return 1

class Node:
    _num = 0    # static variable banyaknya node
    def __init__(self, nodeName, xCoor, yCoor):
        Node._num += 1
        self._name = nodeName
        self._xCoor = xCoor       # belum yakin wujudnya gimana dari gmap
        self._yCoor = yCoor
        self._hVal = sys.maxsize
        self._gVal = 0
        self._fVal = self._hVal + self._gVal
    
    # getter
    def getName(self):
        return self._name
    def getX(self):
        return self._xCoor
    def getY(self):
        return self._YCoor
    def getNum(self):
        return Node._num
    def getGVal(self):
        return self._gVal
    def getHVal(self):
        return self._hVal
    def getFVal(self):
        return self._fVal

    # setter
    def setGVal(self, val):
        self._gVal = val
        self.setFVal()
    def setHVal(self, goalNode):
        val = euclidean(goalNode)
        self._hVal = val
    def setFVal(self):
        self._fVal = self._gVal + self._hVal
    def resetVal(self):
        self.setGVal(0)
        self.setHVal(sys.maxsize)
        self.setFVal()
    
    def euclidean(self, otherNode):
        return sqrt((self.getX() - otherNode.getX())**2 + (self.getY() - otherNode.getY())**2)


class PrioQueue:
    # PrioQueue of tuple (nodeIndex, FVal), sorted by FVal (ascending)
    def __init__ (self):
        self._data = []
        self._size = 0

    def getSize(self):
        return self._size
    def isEmpty(self):
        return self._size == 0

    # Particular node operation
    def hasNode(self, idxNode):
        for i in range(getSize()):
            if (self._data[i][0] == idxNode):
                return True
        return False
    def removeNode(self, idxNode):
        deletedIdx = -1
        for i in range(getSize()):
            if (self._data[i][0] == idxNode):
                deletedIdx = i
                break
        if deletedIdx != -1:
            del self._data[deletedIdx]

    # Enqueue and Dequeue
    def enqueue(self, node):
        # add arbitrarily
        self._data.append(node)
    def dequeue(self):
        idxMax = 0
        for i in range(self._size):
            if (self._data[i][1] > self._data[idxMax][1]):
                idxMax = i
        item = self._data[i]
        del self._data[i]
        return item


    


N = int(input("Banyak node: "))
matrix = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(0, i):
        matrix[i][j] = int(input("M[{}][{}] = ".format(i, j)))
