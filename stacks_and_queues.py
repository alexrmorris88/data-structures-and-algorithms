# =============================================================================
# Stacks
# =============================================================================


class StackNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.top = None

    def append(self, data):
        newNode = StackNode(data)
        currNode = self.head

        if currNode is None:
            self.head = newNode
            self.top = self.head
        else:
            while currNode.next is not None:
                currNode = currNode.next
            self.top.next = newNode
            self.top = self.top.next

    def pop(self):
        currNode = self.head
        topNode = self.top

        if currNode is None:
            print("Stack is empty")
            return
        elif currNode.next is None:
            self.head = None
            self.top = None
            return topNode.data
        while currNode.next is not topNode:
            currNode = currNode.next
        currNode.next = None
        return topNode.data

    def peek(self):
        currNode = self.head

        if currNode is None:
            print("Stack is empty")
            return
        return self.top.data

    def empty(self):
        currNode = self.head
        if currNode is None:
            return True
        else:
            return False

    def print_node(self):
        currNode = self.head
        while currNode:
            print(currNode.data, end=" ")
            currNode = currNode.next


# if __name__ == "__main__":
#     stack = Stack()
#
#     stack.append(1)
#     stack.append(2)
#     stack.append(3)
#     stack.append(4)
#
#     stack.pop()
#
#     stack.print_node()
#     print("\n", stack.peek())
#     print(stack.empty())


# =============================================================================
# Queues
# =============================================================================


class QueueNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.prevNode = None

    def enqueue(self, data):
        newNode = QueueNode(data)
        currNode = self.head

        if currNode is None:
            self.head = newNode
            self.prevNode = self.head
        else:
            while currNode.next is not None:
                currNode = currNode.next
            self.prevNode.next = newNode
            self.prevNode = self.prevNode.next

    def dequeue(self):
        currNode = self.head

        if currNode is None:
            print("Queue is empty")
            return
        else:
            self.head = self.head.next
            return self.head.data

    def print_nodes(self):
        currNode = self.head
        while currNode is not None:
            print(currNode.data, end="->")
            currNode = currNode.next


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    queue.dequeue()
    queue.dequeue()

    queue.print_nodes()



