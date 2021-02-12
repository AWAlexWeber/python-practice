'''
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # Recursing down n points, then going up until we're at m
        
        # Tracking the 'final' node in our downward recursion for purposes of pointing to it at the end
        self.finalNode, self.startNode, self.beginNode, self.entranceNode = None, None, None, None
        
        # Starting the downward recurse process
        self.recurseDown(head, m, n)
        
        # Linking up the rest of our nodes
        if m != 1:
            self.beginNode.next = self.startNode
            self.entranceNode.next = self.finalNode
        
            return head
        else:
            head.next = self.finalNode
            return self.startNode
        
    '''
    Function for recursing through our linked list. Note that we use the same params as the parent function,
    however c represents our current depth.
    '''
    def recurseDown(self, node: ListNode, m: int, n: int, c: int=1):
        if c == n:
            # We've reached the bottom. Grabbing the final node and heading up
            self.startNode, self.finalNode = node, node.next
            return

        elif c == m - 1:
            self.beginNode, self.entranceNode = node, node.next
        
        self.recurseDown(node.next, m, n, c + 1)
            
        # At this stage we've completed recursing. The primary issue here is to link the nodes back together
        if c >= m and c < n:
            node.next.next = node
        