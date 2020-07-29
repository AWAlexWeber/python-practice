'''
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List

class Solution:
    
    # Classic brute force solution,
    # O(n) where we compute the length then add each value
    def getDecimalValue(self, head: ListNode) -> int:
        # Initializing values
        o, n, l = 0, head, 0
        
        # O(n)
        while n != None:
            l, n = l + 1, n.next
            
        # O(n)
        while head != None:
            l, head, o = l - 1, head.next, (o + pow(2, l - 1) if head.val == 1 else o)

        return o
        
    # This solution has a smaller constant, though the complexity remains O(n)
    def getDecimalValueFaster(self, head: ListNode) -> int:
        # Recursing down
        self.sum = 0
        self.recurseDown(head)
        return self.sum

    def recurseDown(self, node: ListNode) -> int:
        if (node.next == None):
            self.sum += (1 if node.val == 1 else 0)
            return 0

        p = 1 + self.recurseDown(node.next)

        if node.val != 0:
            self.sum += pow(2, p)

        return p

    # Even faster solution, using a method called doubling. It works from moving from MSB to LSB
    # It accomplishes this by basically doubling the previous value as long as there is value remaining. This makes sense since the value at an index is
    # going to be 2 ^ n where n is the distance, and we are repeatedly multiplying it as we go
    # Thinkg of it like

    # If we have 
    # 101110
    # We double the following bits this number of times
    # 1 - gets doubled 5 times if its set to 1 (2^5 = 32)
    # 0 - gets doubled 4 times if its set to 1 (2^4 = 16)
    # 1 - gets doubled 3 times if its set to 1 (2^3 = 8)
    # 1 - gets doubled 2 times if its set to 1 (2^2 = 4)
    # 1 - gets doubled 1 times if its set to 1 (2^1 = 2)
    # 0 - gets doubled 0 times if its set to 1 (2^0 = 1)
    # Which is how it works

    def getDecimalValueFast(self, head: ListNode) -> int:
        answer = 0
        while head: 
            answer = 2*answer + head.val 
            head = head.next 
        return answer 