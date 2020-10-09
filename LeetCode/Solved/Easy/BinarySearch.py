'''
704. Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 0:
            return -1
        
        return self.bSearch(nums, 0, len(nums) // 2, len(nums), target)
        
    def bSearch(self, nums: List[int], l: int, i: int, r: int, t: int):
        # If we find the value
        if nums[i] == t:
            return i
        
        # Handling the value not being here
        if r - l <= 1:
            return -1
        
        # Handling everything else
        centerLeft = (i - l) // 2 + l
        centerRight = (r - i) // 2 + i
        
        searchLeft = self.bSearch(nums, l, centerLeft, i, t)
        searchRight = self.bSearch(nums, i, centerRight, r, t)
        
        return (searchLeft if searchLeft != -1 else searchRight)
        