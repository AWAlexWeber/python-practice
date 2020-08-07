import random as rand

# Classic stack implementation
class Node:

    def __init__(self, v):
        self.node = None
        self.val = v

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, v):
        n = Node(v)
        n.node = self.head
        self.head = n
        self.size += 1

    def popAtHead(self) -> Node:
        if self.size <= 0:
            return None

        n = self.head
        self.head = self.head.node
        self.size -= 1

        return n

    def print(self):
        n = self.head
        while n:
            print(n.val,end=" ")
            n = n.node
        print("")

# Generator for building a random linked list
def randomLinkedList(size=10):
    rand.seed(15)

    l = LinkedList()
    for i in range(size):
        l.addAtHead(rand.randint(0, 10))
    return l