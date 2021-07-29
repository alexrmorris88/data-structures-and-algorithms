# ===================================================================================
# Singly Linked List
# ===================================================================================


class SllNode:
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        currNode = self.head
        nodeLength = 1

        if currNode is None:
            print("ERROR: no items in the list")
            return

        else:
            while currNode.nextNode is not None:
                nodeLength += 1
                currNode = currNode.nextNode

            return int(nodeLength)

    def append(self, data):
        newNode = SllNode(data)
        currNode = self.head

        if currNode is None:
            self.head = newNode

        else:
            while currNode.nextNode:
                currNode = currNode.nextNode
            currNode.nextNode = newNode

    def remove(self, index):
        removeNode = self.head

        if removeNode is not None:
            if removeNode.data == index:
                self.head = removeNode.nextNode
                return

        while removeNode is not None:
            if removeNode.data == index:
                break
            currNode = removeNode
            removeNode = removeNode.nextNode

        if removeNode is None:
            print("ERROR: index is out of range")
            return

        currNode.nextNode = removeNode.nextNode

    def printNode(self):
        currNode = self.head

        while currNode:
            print(currNode.data, end=' ')
            currNode = currNode.nextNode


# if __name__ == "__main__":
#     sll = SingleLinkedList()
#     sll.append(1)
#     sll.append(2)
#     sll.append(3)
#     sll.append(4)
#     sll.append(5)
#
#     sll.remove(1)
#
#     sll.printNode()
#
#     print(sll.length())

# ===================================================================================
# Doubly Linked List
# ===================================================================================


class DllNode:
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None
        self.prevNode = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        currNode = self.head
        countNode = 1

        if currNode is None:
            print("ERROR: list is empty")
            return
        else:
            while currNode.nextNode is not None:
                countNode += 1
                currNode = currNode.nextNode

            return countNode

    def append(self, data):
        newNode = DllNode(data)
        currNode = self.head

        if currNode is None:
            self.head = newNode
            return
        else:
            while currNode.nextNode is not None:
                currNode = currNode.nextNode
            currNode.nextNode = newNode
            newNode.prevNode = currNode

    def prepend(self, data):
        newNode = DllNode(data)
        currNode = self.head

        if currNode is None:
            self.head = newNode
            return
        else:
            currNode.prevNode = newNode  # putting the new node in front of the current node
            self.head = newNode  # Pointer
            newNode.nextNode = currNode  # linking the new node to the current node

    def remove(self, index):
        removeNode = self.head

        if removeNode is not None:
            if removeNode.data == index:
                self.head = removeNode.nextNode
                return

        while removeNode is not None:
            if removeNode.data == index:
                break
            currNode = removeNode
            removeNode = removeNode.nextNode

        if removeNode is None:
            print("ERROR: Node does not exist")
            return

        currNode.nextNode = removeNode.nextNode

    def printNode(self):
        currNode = self.head

        while currNode is not None:
            print(currNode.data, end=" ")
            currNode = currNode.nextNode


# if __name__ == "__main__":
#     dll = DoublyLinkedList()
#     dll.append("hi")
#     dll.append(2)
#     dll.append(3)
#     dll.append(4)
#     dll.append(5)
#     dll.prepend(266)
#     dll.prepend(288888)
#     dll.remove(5)
#
#     dll.printNode()
#
#     print(dll.length())


# ===================================================================================
# Circular Linked List
# ===================================================================================

class CircularNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = CircularNode(data)
        currNode = self.head
        newNode.next = currNode

        if currNode is None:
            self.head = newNode
            return
        else:
            while currNode.next is not None:
                currNode = currNode.next
                if currNode.next is self.head:
                    break
            currNode.next = newNode

    def deleteNode(self, node):
        currNode = self.head

        if currNode is None:
            print("List is empty")
            return

        if currNode.data is node and currNode.next is self.head:
            self.head = None

        if currNode.data is node:
            while currNode.next is not self.head:
                currNode = currNode.next
            currNode.next = self.head.next
            self.head = currNode.next

        while currNode.next.data is not node and currNode.next is not self.head:
            currNode = currNode.next

        if currNode.next.data is node:
            nextNode = currNode.next
            currNode.next = nextNode.next

        else:
            print("Node not found")

        return self.head

    def print_nodes(self):
        currNode = self.head
        if currNode is not None:
            while True:
                print(currNode.data, end=" ")
                currNode = currNode.next
                if currNode is self.head:
                    break


if __name__ == "__main__":
    cll = CircularLinkedList()

    cll.append(1)
    cll.append(2)
    cll.append(44)

    cll.deleteNode(2)

    cll.print_nodes()




