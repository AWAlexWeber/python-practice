# A linked list is a special datastructure where data is represented by a series of nodes that point to the next
# 0 -> 1 -> 2 -> 3
# One of the benefits of a linked lis is that inserting at the tail and/or head is O(1)
# However in order to access a value, you do need O(n)
# Linked lists generally make excellent ways of implementing stacks/queues since stacks/queues really only do stuff with the head

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
            print(n.val,end="")
            n = n.node
        print("")

l = LinkedList()
for n in range(10):
    l.addAtHead(n)
    l.print()
for n in range(10):
    l.popAtHead()
    l.print()