'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 'Brute Force' solution
        # O(n*k) where n is the maximal length of a list and k is the number of lists
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List
from heapq import heappush, heappop

class SolutionBetter:
    def mergeKLists(self, linkedLists: List[ListNode]) -> ListNode:
        # Creating a dummy header
        output = ListNode(0)
        pointerNode = output
        d = 0

        # Minheap containing a tuple, (value, node). O(n) space.
        minHeap = list()
        for node in linkedLists:
            if not node:
                continue
            d += 1
            heappush(minHeap, (node.val, d, node))

        # We iterate for every element in O(n) time complexity. Given that we also perform a heappush in O(logk) time, our total complexity is O(nlogk) time and O(k) space.
        while len(minHeap) > 0:
            currentValue, df, currentNode = (heappop(minHeap))
            pointerNode.next = currentNode
            pointerNode = pointerNode.next

            # Getting the next nodes value
            nextNode = currentNode.next
            if nextNode:
                d += 1
                heappush(minHeap, (nextNode.val, d, nextNode))
                

        return output.next