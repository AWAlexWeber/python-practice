from LinkedList import *

# Given a linked list an a value, partition the linked listen whree all the values less than value are to the left, greater to the right

def partition(l: LinkedList, x: int) -> LinkedList:

    l1 = LinkedList()
    l2 = LinkedList()

    n = l.head
    while (n):
        if n.val < x:
            l1.addAtHead(n.val)
        else:
            l2.addAtHead(n.val)
        
        n = n.node

    # Linking them together
    h1 = l1.head

    while (h1.node):
        h1 = h1.node

    h1.node = l2.head
    return l1

testCase = randomLinkedList(50)
testCase.print()
partitionCase = partition(testCase,5)
partitionCase.print()