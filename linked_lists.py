# ===================================================================================
# Singly Linked List
# ===================================================================================


class SinglyLinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        currNode = self.head
        total = 0
        while currNode.next is not None:
            total += 1
            currNode = currNode.next
        return total

    def append(self, data):
        newNode = SinglyLinkedListNode(data)
        currNode = self.head

        if currNode is None:
            self.head = newNode
        else:
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = newNode

    def removeNode(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index our of range")
            return
        curr_index = 0
        curr_node = self.head
        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if curr_index == index:
                last_node.next = curr_node.next # would be erasing current node
                return
            curr_index += 1

    def printList(self):
        nodes = []
        currNode = self.head
        while currNode:
            nodes.append(currNode.data)
            currNode = currNode.next
        print(nodes)


sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)

sll.removeNode(2)

sll.printList()