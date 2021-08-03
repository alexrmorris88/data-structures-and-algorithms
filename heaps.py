# =============================================================================
# Max Heap
# =============================================================================

class MaxHeap:
    def __init__(self):
        self.heap = []

    def getParent(self, i):
        return int((i - 1) / 2)

    def getLeftChild(self, i):
        return 2 * i + 1

    def getRightChild(self, i):
        return 2 * i + 2

    def hasParent(self, i):
        return self.getParent(i) < len(self.heap)

    def hasLeftChild(self, i):
        return self.getLeftChild(i) < len(self.heap)

    def hasRightChild(self, i):
        return self.getRightChild(i) < len(self.heap)

    def insert(self, key):
        self.heap.append(key)
        self.heapify(len(self.heap) - 1)

    def heapify(self, i):
        while (self.hasParent(i) and self.heap[i] > self.heap[self.getParent(i)]):
            self.heap[i], self.heap[self.getParent(i)] = self.heap[self.getParent(i)], self.heap[i]
            i = self.getParent(i)

    def printHeap(self):
        print(self.heap)


heap = MaxHeap()
heap.insert(1)
heap.insert(4)
heap.insert(6)
heap.insert(9)
heap.insert(100)

heap.printHeap()


# =============================================================================
# Min Heap
# =============================================================================


class MinHeap:
    def __init__(self):
        self.heap = []

    def getParent(self, i):
        return int((i - 1) / 2)

    def getLeftChild(self, i):
        return 2 * i + 1

    def getRightChild(self, i):
        return 2 * i + 2

    def hasParent(self, i):
        return self.getParent(i) > len(self.heap)

    def hasLeftChild(self, i):
        return self.getLeftChild(i) > len(self.heap)

    def hasRightChild(self, i):
        return self.getRightChild(i) > len(self.heap)

    def insert(self, key):
        self.heap.append(key)
        self.heapify(len(self.heap) - 1)

    def heapify(self, i):
        while (self.hasParent(i) and self.heap[i] > self.heap[self.getParent(i)]):
            self.heap[i], self.heap[self.getParent(i)] = self.heap[self.getParent(i)], self.heap[i]
            i = self.getParent(i)

    def printHeap(self):
        print(self.heap)


heap = MinHeap()
heap.insert(1)
heap.insert(4)
heap.insert(6)
heap.insert(9)
heap.insert(100)

heap.printHeap()