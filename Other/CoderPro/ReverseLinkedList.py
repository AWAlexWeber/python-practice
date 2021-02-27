'''
Reverse a linkedlist
'''

# TODO: Iterative, non-recursive solution

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next=next

    def toString(self):
        return (str(self.val) + ("" if not self.next else self.next.toString()))

class Solution():
    def reverseLinkedList(self, node: 'Node') -> 'Node':
        ''' Recursing downwards '''
        print(node.toString())
        self.recurseReverse(node).next = None
        print(self.lastNode.toString())
        return self.lastNode

    def recurseReverse(self, node: 'Node') -> 'Node':
        if not node.next:
            self.lastNode = node
            return node
        else:
            nextNode = self.recurseReverse(node.next)
            nextNode.next = node
            return node

class IterativeSolution:
    # We can solve this in O(n) and O(1) time/space.
    def reverse(self, node: 'Node') -> 'Node':
        curr = node
        nxt = curr.next
        curr.next = None
        while nxt:
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp
        return curr
        



# Building our linked list
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = IterativeSolution()
s.reverse(n1)