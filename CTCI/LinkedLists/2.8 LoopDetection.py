# Given a linked list, determine the node at the beginning of an internal loop if it exists
from LinkedList import *
import random as rand

# Set based approach
def getLoopNodeSet(l: LinkedList) -> Node:
    n, s = l.head, set()
    while n:
        if n in s:
            return n
        s.add(n)
        n = n.node

# Runner based approach
def getLoopNodeSetRunner(l: LinkedList) -> Node:
    fast, slow = l.head, l.head

    while fast and fast.node:
        slow = slow.node
        fast = fast.node.node
        if slow == fast:
            break
    
    if not fast or not fast.node:
        return None

    slow = l.head
    while slow != fast:
        slow = slow.node
        fast = fast.node

    return fast

# Generating our test case
l = randomLinkedList(25)
n = l.head
loop = None
while n.node:
    if rand.randint(0,10) > 8:
        loop = n
    n = n.node

l.print()
if loop:
    print("Loop at ",end="")
    print(loop)
else:
    print("No loop")
n.node = loop

print(getLoopNodeSet(l))
print(getLoopNodeSetRunner(l))