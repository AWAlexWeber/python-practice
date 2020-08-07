# Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node

# Now we are going to assume that we are actually given a correct node. We have absolutely no way of knowing if we are the head or not,
# so we are going to assume that the node is correct

# We will accomplish this by simply duplicated the value of our next node and then skipping it
from LinkedList import *

def deleteMiddleNode(n: Node):
    print("Deleting " + str(n.val))
    n.val = n.node.val
    n.node = n.node.node

l = randomLinkedList(10)
n = l.head
for i in range(5):
    n = n.node

l.print()
deleteMiddleNode(n)
l.print()