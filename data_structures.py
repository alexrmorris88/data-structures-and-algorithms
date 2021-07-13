"""
This tutorial came from Brian Faure at https://www.youtube.com/watch?v=JlMyYuY1aXU
"""

# ===================================================================================
# Singly Linked List
# ===================================================================================


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node() # user cannot access this head node, it is a placeholder to access the next node

    def set_node(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1
            curr = curr.next
        return total

    def display(self):
        elems = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elems.append(curr_node.data)
        print(elems)

    def get_index(self, index):
        if index >= self.length():
            print("ERROR: 'get' index out of range")
            return None
        curr_index = 0
        curr_node = self.head
        while True:
            curr_node = curr_node.next
            if curr_index == index:
                return curr_node.data
            curr_index += 1

    def erase(self, index):
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


# my_list = LinkedList()
#
# my_list.set_node(1)
# my_list.set_node(2)
# my_list.set_node(3)
# my_list.set_node(4)
#
# my_list.display()
#
# my_list.erase(1)
#
# my_list.display()
# print(f'The length of the list is: {my_list.length()}')
# print(f"element at the 2nd index {my_list.get_index(1)}")


# ===================================================================================
# Doubly Linked List
# ===================================================================================
"""
this tutorial is by LucidProgramming at https://www.youtube.com/watch?v=8kptHdreaTA
"""


class DoublyNode:
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None
        self.prevNode = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            newNode = DoublyNode(data)
            newNode.prevNode = None
            self.head = newNode
        else:
            newNode = DoublyNode(data)
            currNode = self.head
            while currNode.nextNode != None:
                currNode = currNode.nextNode
            currNode.nextNode = newNode
            newNode.prevNode = currNode
            newNode.nextNode = None

    def prepend(self, data):
        if self.head is None:
            newNode = DoublyNode(data)
            newNode.prevNode = None
            self.head = newNode
        else:
            newNode = DoublyNode(data)
            self.head.prevNode = newNode
            newNode.nextNode = self.head
            self.head = newNode
            newNode.prevNode = None

    def print_list(self):
        nodesList = []
        currNode = self.head
        while currNode:
            nodesList.append(currNode.data)
            currNode = currNode.nextNode
        print(nodesList)


# dllist = DoublyLinkedList()
#
# dllist.prepend(99)
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.prepend(66)
# dllist.append(4)
#
# dllist.print_list()


# ===================================================================================
# Circular Linked List
# ===================================================================================
"""
this tutorial is by LucidProgramming at https://www.youtube.com/watch?v=5WoNhm7sOnA
"""


class CircularNode:
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        newNode = CircularNode(data)
        currNode = self.head
        newNode.nextNode = self.head
        if not self.head:
            newNode.nextNode = newNode
        else:
            while currNode.nextNode != self.head:
                currNode = currNode.nextNode
            currNode.nextNode = newNode
        self.head = newNode

    def append(self, data):
        if not self.head:
            self.head = CircularNode(data)
            self.head.nextNode = self.head
        else:
            newNode = CircularNode(data)
            currNode = self.head
            while currNode.nextNode != self.head:
                currNode = currNode.nextNode
            currNode.nextNode = newNode
            newNode.nextNode = self.head

    def print_list(self):
        nodesList = []
        currNode = self.head
        while currNode:
            nodesList.append(currNode.data)
            currNode = currNode.nextNode
            if currNode == self.head:
                break
        print(nodesList)


# cllist = CircularLinkedList()
#
# cllist.append(1)
# cllist.append(2)
# cllist.prepend(44)
# cllist.append(3)
# cllist.append(4)
# cllist.prepend(99)
#
# cllist.print_list()




# ===================================================================================
# Stacks using the implementation of a linked list
# ===================================================================================
"""
this tutorial is from https://chercher.tech/python-data-structures/stack-python-ds
"""

class StackNode:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class Stack:
    def __init__(self):
        self.head = None
        self.top = None

    def push(self, data):
        if self.is_empty() is True:
            self.head = StackNode(data)
            self.top = self.head
        else:
            self.top.nextNode = StackNode(data)
            self.top = self.top.nextNode

    def pop(self):
        if self.is_empty() is True:
            print("Stack is empty")
            return None
        elif self.head.nextNode is None:
            qtr = self.top
            self.head = None
            self.top = None
            return qtr.data
        ptr = self.head
        qtr = self.top
        while ptr.nextNode != self.top:
            ptr = ptr.nextNode
        ptr.nextNode = None
        return qtr.data

    def peek(self):
        if self.is_empty() is True:
            print("Stack is empty")
            return None
        return self.top.data

    def size(self):
        if self.is_empty() is True:
            print("Stack is empty")
        else:
            ptr = self.head
            while ptr.nextNode is not None:
                print(len(ptr.nextNode))

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def display(self):
        if self.is_empty() is True:
            print("Stack is empty")
            return None
        ptr = self.head
        print("The Stack")
        while ptr.nextNode is not None:
            print(ptr.nextNode.data)
            ptr = ptr.nextNode
        print(ptr.data, "<-- Top")


a = Stack()
a.push(1)
a.push(2)
a.display()
a.pop()
a.display()
a.pop()
a.display()
a.push(5)
a.push(6)
a.display()
print(a.peek())

