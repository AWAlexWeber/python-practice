# Implementation of a stack
# This is the linked list style implementation

# Linked list
# This only supports insertion at the head for our stack implementation
class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, v):
        n = Node(v)
        n.next = self.head
        self.head = n
        self.size += 1

    def pop(self):
        if self.size <= 0:
            return None

        n = self.head
        self.head = self.head.next
        self.size -= 1
        return n.value

    def print(self):
        n = self.head
        while n:
            print(n.value,end=" ")
            n = n.next
        print()

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.linkedList = LinkedList()

    def size(self):
        return self.linkedList.size

    def add(self, v):
        self.linkedList.add(v)

    def pop(self):
        return self.linkedList.pop()

    def print(self):
        self.linkedList.print()

# Testing our stack
s = Stack()
for n in range(0,10):
    s.add(n)

s.print()

while s.size() > 0:
    print(s.pop(),end=" ")

