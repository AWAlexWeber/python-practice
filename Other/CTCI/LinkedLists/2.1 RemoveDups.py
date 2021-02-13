# Write code to remove duplicates from an unsorted linked list
from LinkedList import *

def removeDups(l: LinkedList):
    c = l.head.node
    p = l.head

    # Tracking our set
    s = set()
    s.add(p.val)

    while (c):
        if c.val not in s:
            p.node = c
            p = p.node
            s.add(c.val)

        c = c.node

    p.node = None


# Test cases
testCase = randomLinkedList(5000)
removeDups(testCase)
testCase.print()