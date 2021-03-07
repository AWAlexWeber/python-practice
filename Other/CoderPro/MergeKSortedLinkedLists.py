'''
Given a bunch of linked lists that are sorted, merge them together in one big sorted linked list.
'''

# The approach we're going to take is to keep a minheap of every nodes value. When we pop from the minheap we will insert the next value in that linked list.
# We will use O(logk) for every insertion, and will do it for every element, giving us a total time complexity of O(nlogk) where N is the total number of nodes and K is the total number of linked lists
from typing import List
from heapq import heappush, heappop

class Node:
    def __init__(self, val, nextNode: 'Node'=None):
        self.val, self.nextNode = val, nextNode

    def __repr__(self):
        return str(self.val) + " -> " + ('Null' if not self.nextNode else str(self.nextNode))


class Solution:
    def mergeLinkedLists(self, linkedLists: List[Node]) -> Node:
        # Creating a dummy header
        output = Node(0)
        pointerNode = output

        # Minheap containing a tuple, (value, node). O(n) space.
        minHeap = list()
        for node in linkedLists:
            heappush(minHeap, (node.val, node))

        # We iterate for every element in O(n) time complexity. Given that we also perform a heappush in O(logk) time, our total complexity is O(nlogk) time and O(k) space.
        while len(minHeap) > 0:
            currentValue, currentNode = (heappop(minHeap))
            pointerNode.nextNode = currentNode
            pointerNode = pointerNode.nextNode

            # Getting the next nodes value
            nextNode = currentNode.nextNode
            if nextNode:
                heappush(minHeap, (nextNode.val, nextNode))

        return output
        

def buildLinkedList(values: List[int]) -> Node:
    head = Node(0)
    current = head
    for i in range(0, len(values)):
        current.nextNode = Node(values[i])
        current = current.nextNode
    return head.nextNode


# Building our test cases
llOne = buildLinkedList([1,6,8])
llTwo = buildLinkedList([2,3,7,9])
llThree = buildLinkedList([4,5,10])

s = Solution()
print(s.mergeLinkedLists([llOne, llTwo, llThree]))