'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # While we have more numbers in both (with numbers to add)
        c = 0
        r = ListNode()
        t = r

        while l1 or l2 or c:
            v1 = (l1.val if l1 else 0)
            v2 = (l2.val if l2 else 0)
            c, v = divmod(v1 + v2 + c, 10)

            t.next = ListNode(v)
            t = t.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return r.next

    def setupList(self, values) -> ListNode:
        output = ListNode()
        outputHead = output

        for val in values:
            output.next = ListNode()
            output.next.val = val
            output = output.next

        return outputHead.next

    def printList(self, l):
        while (l != None):
            print(l.val, end=" ")
            l = l.next
        print()

solution = Solution()

listNodeValuesA = [5]#[2, 4, 3, 0, 5]
listNodeValuesB = [5]#[5, 6, 4]

a = solution.setupList(listNodeValuesA)
b = solution.setupList(listNodeValuesB)

solution.printList(a)
solution.printList(b)

solution.printList(solution.addTwoNumbers(a, b))