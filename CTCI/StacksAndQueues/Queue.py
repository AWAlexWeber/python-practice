# Queue implementation
# This is the list style implementation

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, v):
        if self.tail:
            self.tail.next = Node(v)
            self.tail = self.tail.next
        else:
            self.tail = Node(v)

        if not self.head:
            self.head = self.tail

        self.size += 1
    
    def pop(self):
        n = self.head.value
        self.head = self.head.next

        if not self.head:
            self.tail = self.head

        self.size -= 1

        return n

    def print(self):
        n = self.head
        while n:
            print(n.value,end=" ")
            n = n.next
        print()


class Queue:

    def __init__(self):
        self.data = LinkedList()

    def size(self):
        return self.data.size
        
    def add(self, v):
        self.data.add(v)

    def pop(self):
        return self.data.pop()

    def print(self):
        self.data.print()#

# Testing our queue
s = Queue()
for n in range(0,10):
    s.add(n)

s.print()

while s.size() > 0:
    print(s.pop(),end=" ")