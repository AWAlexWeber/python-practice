''' Given two linked lists, determine the intersection point. If they do not intersect, return None'''

# Basic linked list processing question.
from typing import List

class Node:
    def __init__(self, val, nextNode: 'Node'=None):
        self.val, self.nextNode = val, nextNode

    def __repr__(self):
        return str(self.val) + " -> " + ('Null' if not self.nextNode else str(self.nextNode))

class Solution:
    def intersection(self, list1: Node, list2: Node) -> Node:
        # Keeping track of our visisted nodes
        visitNode = set()

        while list1:
            visitNode.add(list1)
            list1 = list1.nextNode

        while list2:
            if list2 in visitNode:
                return list2
            list2 = list2.nextNode
        
        return None

    def intersectionCount(self, list1: Node, list2: Node) -> Node:
        # First we count the lengths
        length1, length2 = 0, 0
        head1, head2 = list1, list2

        while head1:
            length1 += 1
            head1 = head1.nextNode
        while head2:
            length2 += 1
            head2 = head2.nextNode

        while length1 < length2:
            list1 = list1.nextNode
            length1 += 1

        while length2 < length1:
            list2 = list2.nextNode
            length2 += 1

        # Finally attempting to find our join
        while list1 != list2:
            list1 = list1.nextNode
            list2 = list2.nextNode

        return list1


def buildLinkedList(values: List[int]) -> Node:
    head = Node(0)
    current = head
    for i in range(0, len(values)):
        current.nextNode = Node(values[i])
        current = current.nextNode
    return head.nextNode

n1 = buildLinkedList([1,2,3,4])
n2 = buildLinkedList([1,2,3,4,5,6,7,8,9,10])

s = Solution()
print(s.intersectionCount(n1,n2))