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

    def __repr__(self):
        return f'{self.next}'

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


my_list = LinkedList()

my_list.set_node(1)
my_list.set_node(2)
my_list.set_node(3)
my_list.set_node(4)

my_list.display()

my_list.erase(1)

my_list.display()
print(f'the length of the list is: {my_list.length()}')
print(f"element at the 2nd index {my_list.get_index(1)}")
