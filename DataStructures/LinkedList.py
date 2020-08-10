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

# Advantages of a doubly linked list is that traversal becomes much easier to handle
# More importantly, you have easy access to the back which allows you to pop and insert at various locations more easily
# Specifically, head/tail insertions deletions become O(1)
# Doubly linked list node
class DoubleNode:
    def __init__(self, v: int):
        self.value = v
        self.next = None
        self.previous = None

# Doubly linked list
class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addAtHead(self, v: int):
        # Appending to head
        doubleNode = DoubleNode(v)
        doubleNode.next = self.head

        # Pointing the head to this new node since we added it to the head
        if self.head:
            self.head.previous = doubleNode

        self.head = doubleNode

        # If our tail has not been initialized, it now points to this since its both the front and the back
        if not self.tail:
            self.tail = doubleNode

    def addAtTail(self, v: int):
        doubleNode = DoubleNode(v)

        # Pointing properly
        doubleNode.previous = self.tail

        if self.tail:
            self.tail.next = doubleNode

        self.tail = doubleNode

        # If our head has not been initialized, this is also our head
        if not self.head:
            self.head = doubleNode

    def printForwards(self):
        n = self.head
        while n:
            print(n.value,end=" ")
            n = n.next
        print("")

    def printBackwards(self):
        n = self.tail
        while n:
            print(n.value,end=" ")
            n = n.previous
        print("")

    # Popping at head
    def popAtHead(self) -> int:
        v = self.head.value
        self.head = self.head.next

        if self.head:
            self.head.previous = None

        else:
            self.tail = None

        return v

    # Popping at tail
    def popAtTail(self) -> int:
        v = self.tail.value
        self.tail = self.tail.previous

        if self.tail:
            self.tail.next = None

        else:
            self.head = None

        return v




#l = LinkedList()
#for n in range(10):
#    l.addAtHead(n)
#    l.print()
#for n in range(10):
#    l.popAtHead()
#    l.print()

l = DoubleLinkedList()
for n in range(10):
    l.addAtHead(n)

l.addAtTail(150)
l.printForwards()
l.printBackwards()

l.popAtTail()
l.popAtTail()
l.popAtTail()
l.popAtTail()

l.printForwards()
l.printBackwards()

l.popAtHead()
l.popAtHead()
l.popAtHead()
l.popAtHead()
l.popAtHead()
l.popAtHead()

l.printForwards()
l.printBackwards()

l.popAtTail()

l.printForwards()
l.printBackwards()

l = DoubleLinkedList()
for n in range(10):
    l.addAtHead(n)

l.addAtTail(150)
l.printForwards()
l.printBackwards()
