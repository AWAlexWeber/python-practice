'''
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListRecursively(self, head: ListNode) -> ListNode:
        # Handling empty.
        if not head:
            return None
        
        # Recursive solution:
        self.ghead = None
        self.reverseCurrent(head)
        head.next = None
        return self.ghead
        
    def reverseCurrent(self, node: ListNode) -> ListNode:
        nxt = None
        if node.next:
            nxt = self.reverseCurrent(node.next)
        else:
            # We've found the bottom node
            self.ghead = node
            return node
            
        # Reversing upwards
        nxt.next = node
        return node