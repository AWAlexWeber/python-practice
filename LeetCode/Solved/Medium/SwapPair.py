'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Swapping pairs
        o, n, p = None, head, None

        while n and n.next:
            if not o:
                o = n.next

            if p:
                p.next = n.next
            
            p = n

            t = n.next.next

            # Swaps
            n.next.next = n
            n.next = t
            n = t

        if not o:
            return head
            
        return o