'''
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

# Process here will be to keep track of our next position
# If we ever reach a point where we have not completed a group but made it to the end, we simply skip

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        n = self
        i = 0
        while n:
            print(n.val, end=" ")
            i += 1
            n = n.next

            if i > 15:
                break

        print("")

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        self.output, self.currentNode, self.entrance, exitNode, self.breakOut = None, head, None, None, False

        while True:
            self.currentNode = self.recurseReverse(self.currentNode, k)
            if self.breakOut:
                break

            if exitNode:
                exitNode.next = self.entrance
            exitNode, self.currentNode = self.currentNode, self.currentNode.next

        return self.output

    # This recursive approach ensures that we only make a pass once we've gone deep enough
    def recurseReverse(self, node: ListNode, k: int) -> ListNode:

        if k == 0:
            self.currentNode.next = node
            return None

        elif k == 1:
            if not self.output:
                self.output = node
            self.entrance = node

        if not node or self.breakOut:
            self.breakOut = True
            return None

        deeperNode = self.recurseReverse(node.next, k - 1)

        if deeperNode:
            deeperNode.next = node

        if self.breakOut:
            return None

        return node

# Generating our test case
head = ListNode(0)
n = head

for v in range(1,10):
    n.next = ListNode(v)
    n = n.next

s = Solution()
head = s.reverseKGroup(head, 2)
head.print()