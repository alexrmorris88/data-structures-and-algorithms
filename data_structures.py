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

# cllist.append(1)
# cllist.append(2)
# cllist.prepend(44)
# cllist.append(3)
# cllist.append(4)
# cllist.prepend(99)

# cllist.print_list()


# ===================================================================================
# Stack - using the implementation of a linked list
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


# a = Stack()
# a.push(1)
# a.push(2)
# a.display()
# a.pop()
# a.display()
# a.pop()
# a.display()
# a.push(5)
# a.push(6)
# a.display()
# print(a.peek())


# ===================================================================================
# Queue - using a linked list to implement the queue
# ===================================================================================
"""
this tutorial is from https://www.geeksforgeeks.org/python-queue-using-doubly-linked-list/
"""


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class Queue:
    def __init__(self):
        self.head = None
        self.lastNode = None

    def enqueue(self, data):
        if self.lastNode is None:
            self.head = QueueNode(data)
            self.lastNode = self.head
        else:
            self.lastNode.nextNode = QueueNode(data)
            self.lastNode = self.lastNode.nextNode

    def dequeue(self):
        if self.head is None:
            print("Node is empty")
            return
        else:
            to_return = self.head.data
            self.head = self.head.nextNode
            return to_return

    def display(self):
        print("queue elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.nextNode


# q = Queue()
#
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
#
# q.display()


# ===================================================================================
# Priority Queue - using a linked list to implement the queue
# ===================================================================================
"""
this tutorial is from https://www.geeksforgeeks.org/priority-queue-using-linked-list/
"""


class PriorityQueueNode:
    def __init__(self, data, pr):
        self.data = data
        self.priority = pr
        self.nextNode = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def push(self, data, pr):
        if self.is_empty() == True:
            self.front = PriorityQueueNode(data, pr)
            return 1
        elif self.front.priority > pr:
            newNode = PriorityQueueNode(data, pr)
            newNode.nextNode = self.front
            self.front = newNode
            return 1
        else:
            temp = self.front
            while temp.nextNode:
                if pr <= temp.nextNode.priority:
                    break
                temp = temp.nextNode
            newNode = PriorityQueueNode(data, pr)
            newNode.nextNode = temp.nextNode
            temp.nextNode = newNode
            return 1

    def pop(self):
        if self.is_empty() == True:
            return
        else:
            self.front = self.front.nextNode
            return 1

    def peek(self):
        if self.is_empty() == True:
            return
        else:
            return self.front.data

    def traverse(self):
        if self.is_empty() == True:
            return "Queue is empty"
        else:
            temp = self.front
            while temp:
                print(temp.data, end=", ")
                temp = temp.nextNode


# pq = PriorityQueue()
# pq.push(4, 1)
# pq.push(5, 2)
# pq.push(6, 3)
# pq.push(7, 0)
#
# pq.pop()
#
# pq.traverse()


# ===================================================================================
# General Trees
# ===================================================================================
"""
this tutorial is from https://www.youtube.com/watch?v=4r_XR9fUPhQ
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = '  ' * self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.child) > 0:
            for c in self.child:
                c.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


# root = build_product_tree()
# root.print_tree()


# ===================================================================================
# Binary Trees
# ===================================================================================
"""
this tutorial is from https://www.youtube.com/watch?v=lFq5mYUWEBk
"""


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data: # checking to see if the data already exists
            return
        if data < self.data: # data is added to the left tree
            if self.left: # if there is data on the left already
                self.left.add_child(data)
            else: # if there is no data on the left already
                self.left = BinarySearchTreeNode(data)
        else: # adding data to the right tree
            if self.right:  # if there is data on the right already
                self.right.add_child(data)
            else:  # if there is no data on the right already
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left: # visit the left three first
            elements += self.left.in_order_traversal()

        else:
            if self.right: # visit the right tree
                elements += self.right.in_order_traversal()

        elements.append(self.data)  # visit the root node

        return elements

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data: # value might be in the left subtree
            if self.left:
                self.left.search(value)
            else:
                return False
        if value > self.data: # value might be in the right subtree
            if self.right:
                self.right.search(value)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

        return root


# numbers = [100, 20, 3, 4, 40, 50, 20, 77, 82]
# numbers_tree = build_tree(numbers)
# print(numbers_tree.in_order_traversal())


# ===================================================================================
# Heap - MaxHeap
# ===================================================================================
"""
this tutorial is from https://www.section.io/engineering-education/heap-data-structure-python/
"""


class MaxHeap:
    def __init__(self):
        # Initialize a heap using list
        self.heap = []

    def getParentPosition(self, i):
        # The parent is located at floor((i-1)/2)
        return int((i-1)/2)

    def getLeftChildPosition(self, i):
        # The left child is located at 2 * i + 1
        return 2*i+1

    def getRightChildPosition(self, i):
        # The right child is located at 2 * i + 2
        return 2*i+2

    def hasParent(self, i):
        # This function checks if the given node has a parent or not
        return self.getParentPosition(i) < len(self.heap)

    def hasLeftChild(self, i):
        # This function checks if the given node has a left child or not
        return self.getLeftChildPosition(i) < len(self.heap)

    def hasRightChild(self, i):
        # This function checks if the given node has a right child or not
        return self.getRightChildPosition(i) < len(self.heap)

    def getMax(self):
        return self.heap[0] # Returns the largest value in the heap in O(1) time.

    def insert(self, key):
        self.heap.append(key) # Adds the key to the end of the list
        self.heapify(len(self.heap) - 1) # Re-arranges the heap to maintain the heap property

    def heapify(self, i):
        while(self.hasParent(i) and self.heap[i] > self.heap[self.getParentPosition(i)]): # Loops until it reaches a leaf node
            self.heap[i], self.heap[self.getParentPosition(i)] = self.heap[self.getParentPosition(i)], self.heap[i] # Swap the values
            i = self.getParentPosition(i) # Resets the new position

    def printHeap(self):
        print(self.heap) # Prints the heap


# h = MaxHeap()
# h.insert(2)
# h.insert(100)
# h.insert(20)
# h.insert(40)
# h.insert(5)
# h.insert(8)
# h.insert(19)
#
# h.printHeap()
#
# print(h.getMax())


# ===================================================================================
# Heap - MinHeap using heapq
# ===================================================================================
"""
this tutorial is from https://www.section.io/engineering-education/heap-data-structure-python/
"""
import heapq


class MinHeap:
    def __init__(self, minheap): # minheap is the list that we can to convert to a heap
        heapq.heapify(minheap) # Use the heapify function to convert list to a heap
        self.minheap = minheap

    def insert(self, key):
        heapq.heappush(self.minheap, key) # Insert key into the heap (heapq automatically maintains the heap property)

    def getMin(self):
        return self.minheap[0] # Returns the smallest element of the heap in O(1) time

    def removeMin(self):
        heapq.heappop(self.minheap) # The heappop function removes the smallest element in the heap

    def printHeap(self):
        print(self.minheap) # Prints the heap

# heap_list = [2,3,4,77,8,44]
#
# h = MinHeap(heap_list)
# h.insert(1)
# h.insert(100)
# h.insert(13)
# h.insert(20)
# h.insert(50)
# h.insert(70)
# h.insert(4)
# h.insert(6)
#
# h.printHeap()


# ===================================================================================
# Hash Tables - without collisions
# ===================================================================================
"""
this tutorial is from https://www.youtube.com/watch?v=ea8BRGxGmlA
"""


class HashTable:
    def __init__(self):
        self.MAX = 20
        self.array = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char) # using ASCII coding
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.array[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.array[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.array[h] = None


# ht = HashTable()
# ht['march 6'] = 130
# ht['march 7'] = 120
# ht['march 8'] = 150
# ht['march 9'] = 110
# ht['march 17'] = 123
# ht['march 20'] = 100
#
# print(ht.array)
#
# del ht['march 20']
#
# print(ht.array)


# ===================================================================================
# Hash Tables - with collisions
# ===================================================================================
"""
this tutorial is from https://www.youtube.com/watch?v=54iv1si4YCM
"""


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.array = [[] for i in range(self.MAX)] # we change the "None" to a [] for handling collisions

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char) # using ASCII coding
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False

        # instead of overwriting the value, we have to implement the linked list

        for idx, elem in enumerate(self.array[h]): # if the key exists, handle it
            if len(elem) == 2 and elem[0] == key:
                self. array[h][idx] = (key, value)
                found = True
                break

        if not found: # if the key does not exist
            self.array[h].append((key, value))

    def __getitem__(self, key): # we need to update the 'getitem' to include multiple items with the same hash value
        h = self.get_hash(key)
        for elem in self.array[h]:
            if elem[0] == key:
                return elem[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, elem in enumerate(self.array[h]):
            if elem[0] == key:
                del self.array[h][idx]


ht = HashTable()
ht['march 6'] = 130
ht['march 6'] = 176
ht['march 7'] = 120
ht['march 8'] = 150
ht['march 9'] = 110
ht['march 9'] = 155
ht['march 17'] = 123
ht['march 20'] = 100

print(ht.array)

print(ht['march 6'])

del ht['march 20']

print(ht.array)










