'''
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

from collections import deque 

### One pass by keeping a queue that will pop off the back when we've reached the end to give us the proper node
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # Creating our queue
        c = 0
        q, l = deque(), head
        while l:
            c = c + 1
            q.append(l)
            if len(q) > n + 1:
                q.popleft()
            l = l.next

        # Popping the first value
        if c == n:
            return head.next

        m = q.popleft()
        m.next = m.next.next

        return head
        
# Building our list
nodeHead = ListNode()
node = nodeHead
for n in range(1,6):
    node.next = ListNode()
    node = node.next
    node.val = n

node = nodeHead.next

s = Solution()
ns = s.removeNthFromEnd(nodeHead.next, 2)

print("")

while ns:
    print(ns.val)
    ns = ns.next