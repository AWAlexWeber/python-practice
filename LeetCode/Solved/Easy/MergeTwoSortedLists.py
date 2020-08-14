from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        o = ListNode(0)
        n = o

        while l1 and l2:
            if l1.val < l2.val:
                n.next = ListNode(l1.val)
                l1 = l1.next
            else:
                n.next = ListNode(l2.val)
                l2 = l2.next
            n = n.next

        while l1:
            n.next = ListNode(l1.val)
            l1 = l1.next
            n = n.next

        while l2:
            n.next = ListNode(l2.val)
            l2 = l2.next
            n = n.next

        return o.next


