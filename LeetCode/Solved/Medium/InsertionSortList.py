'''
147. Insertion Sort List

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        while True:
            (head, run) = self.sortOnce(head)
            #print(head)
            if not run:
                break
                
        return head
        
    def sortOnce(self, head: ListNode) -> bool:
        # Performs one attempt of sort
        # Iterate until we find an out of order node
        # This is O(n)
        n = head
        while n.next and n.val <= n.next.val:
            n = n.next
        # Checking if we've completed
        if n.next == None:
            return head, False
            
        # Okay we've found the first value to sort
        target = n.next
        target_previous = n
        
        # Then we will make another iteration through, again O(n)
        # We will take the non-recrusive solution here, various trade-offs associated with this decision.
        place = head
        place_before = head
        while place.next and place.val <= target.val:
            place_before = place
            place = place.next
            
        #print(target_previous.val, target.val)
        #print(place_before.val, place.val)
        #print("")
        
        # Place's next becomes target's next if target_previous is equal to place
        if target_previous == place:
            place.next = target.next
        else:
            target_previous.next = target.next
            
        target.next = place
        
        # If place before is not place, we need it to point to target
        if place_before != place:
            place_before.next = target
            
        # If placement target is the head, then we need to make this the new head
        if place_before == place:
            return target, True
        return head, True