# Given two linked lists with an intersectting node, find that intersecting node
from LinkedList import *

def getIntersection(l1: LinkedList, l2: LinkedList) -> Node:
    # Getting lengths
    length1 = length2 = 0

    n1 = l1.head
    n2 = l2.head

    while n1.node:
        length1 += 1
        n1 = n1.node

    while n2.node:
        length2 += 1
        n2 = n2.node

    if n1 != n2:
        return False

    # Resetting heads
    n1 = l1.head
    n2 = l2.head

    while length1 > length2:
        length1 -= 1
        n1 = n1.node

    while length2 > length1:
        length2 -= 1
        n2 = n2.node

    # Our node has been adjusted
    print(n1.val,n2.val)

    while n1 != n2:
        n1 = n1.node
        n2 = n2.node

    return n1

# Generating our test case
l1 = randomLinkedList(10)
l2 = randomLinkedList(25)

n1 = l1.head
while n1.node:
    n1 = n1.node

n2 = l2.head
while n2.node:
    n2 = n2.node

n = Node(15)

n1.node = n
n2.node = n

# Randomly addng more
for i in range(0,15):
    t = Node(100 * i)
    n.node = t
    n = n.node

l1.print()
l2.print()

print(getIntersection(l1,l2))
