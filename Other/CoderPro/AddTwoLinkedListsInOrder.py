''' 
#4a

Given two linked lists representing a number (in order!) return a linked list representing their sum.

Given 5->6->7 and 1->2->3->4, return 1->8->0->1

'''

from typing import List

# Slightly more complicated than adding two numbers as linked lists that are in reverse order.
# The main problem we're going to have to handle here is traversal. What we can do, however, is create two stacks, push each element onto each.
# Then, we can add the two top most elements, create a node, and repeat.

# This does give us an O(n + m) space complexity (where n is the first linked list, and m is the second), but given we are returning an O(n + m) object, that is okay
# Additionally, this is O(n + m) time complexity, which is the lowest we're going to get.

# Defining our linked list
class LinkedListNode():
    def __init__(self, val: int=0, nextVal=None):
        self.val, self.next = val, nextVal

    def __str__(self):
        return str(self.val) + (str(self.next) if self.next else '')

class Solution():
     def addTwoLinkedListsInOrder(self, num1: LinkedListNode, num2: LinkedListNode) -> LinkedListNode:
        # Using two lists as stacks.
        stackOne = list()
        stackTwo = list()

        headerOne = num1
        while headerOne:
            stackOne.append(headerOne.val)
            headerOne = headerOne.next

        headerTwo = num2
        while headerTwo:
            stackTwo.append(headerTwo.val)
            headerTwo = headerTwo.next

        # Is one of these empty? Note this handles if both are empty.
        if len(stackOne) <= 0:
            return num2

        if len(stackTwo) <= 0:
            return num1

        # We now have two lists (stacks) containing our values.
        # Now we go backwards

        # Tracking our current node
        node = LinkedListNode()
        c = 0

        while len(stackOne) > 0 or len(stackTwo) > 0:
            num1Val = (0 if len(stackOne) <= 0 else stackOne.pop())
            num2Val = (0 if len(stackTwo) <= 0 else stackTwo.pop())
            
            newValue = (num1Val + num2Val + c) % 10
            c = (1 if (num1Val + num2Val + c >= 10) else 0)

            node.val = newValue
            newNode = LinkedListNode()
            newNode.next = node
            node = newNode

        return node.next

# Helper test function.
def buildLinkedListFromList(values: List[int]) -> LinkedListNode:
    header = LinkedListNode()
    pointer = header
    for value in values:
        pointer.next = LinkedListNode(val=value)
        pointer = pointer.next
    return header.next

num1 = buildLinkedListFromList([5,6,7])
num2 = buildLinkedListFromList([1,2,3,4,5,6,7,8,9])

s = Solution()
print(s.addTwoLinkedListsInOrder(num1,num2))