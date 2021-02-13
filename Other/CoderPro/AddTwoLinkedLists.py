''' 
#4
Given two numbers represented in reverse as linked list, add the two numbers together. Return in the form of a reversed linked list. Assuming no leading zeros
'''

from typing import List

# Recurse down to the bottom, recurse back up adding the numbers together
# 345 + 2567 =
# 5 -> 4 -> 3
# 7 -> 6 -> 5 -> 2
# 2 -> 1 -> 9 -> 2

# Time complexity is O(n + m) where n is the length of the first number and m is the length of the second number.
# Space complexity is also O(n + m) where, again, n is the length of the first number and m is the length of the second number.

# Overall solution is iteratively, not recursive, which preserves the stackspace from recursive abuse.

class LinkedListNode():

    def __init__(self, next=None, val: int=0):
        self.next, self.val = next, val

    def __str__(self):
        return str(self.val) + ('' if not self.next else str(self.next))

class Solution():

    def addTwoLinkedLists(self, num1: LinkedListNode, num2: LinkedListNode) -> LinkedListNode:
        # Carry value
        c = 0
        # Empty header node
        outputNode = LinkedListNode()
        nodePointer = outputNode

        # While both digits are valid, we iterate through both linked lists adding the numbers together
        while num1 or num2:

            num1Val = (num1.val if num1 else 0)
            num2Val = (num2.val if num2 else 0)

            # Adding the two numbers together including the carry digit
            value = (num1Val + num2Val + c) % 10

            # Setting our new carry
            c = 1 if num1Val + num2Val + c >= 10 else 0

            # Setting our digit into the linked list
            nodePointer.next = LinkedListNode(val=value)
            nodePointer = nodePointer.next

            # Moving our pointers forward
            num1 = (num1.next if num1 else None)
            num2 = (num2.next if num2 else None)

        return outputNode.next
            

# Helper test function.
def buildLinkedListFromList(values: List[int]) -> LinkedListNode:
    header = LinkedListNode()
    pointer = header
    for value in values:
        pointer.next = LinkedListNode(val=value)
        pointer = pointer.next
    return header.next

s = Solution()

# Two normal test cases
num1 = buildLinkedListFromList([5,4,3])
num2 = buildLinkedListFromList([7,6,5,2])
print(str(s.addTwoLinkedLists(num1,num2)))
num1 = buildLinkedListFromList([7,9,8])
num2 = buildLinkedListFromList([1,2,3,4,5,6,7,8,9])
print(str(s.addTwoLinkedLists(num1,num2)))

# Some weird test cases
num1 = buildLinkedListFromList([])
num2 = buildLinkedListFromList([1,2,3,4,5,6,7,8,9])
print(str(s.addTwoLinkedLists(num1,num2)))

num1 = buildLinkedListFromList([5,1])
num2 = buildLinkedListFromList([0])
print(str(s.addTwoLinkedLists(num1,num2)))