'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Handling a simple base case
        if len(nums) <= 0:
            return [-1, -1]
        
        # Binary search to find a SINGLE instance of our target value
        firstInstance = self.binarySearch(nums, target, 0, len(nums)//2, len(nums))
        
        if firstInstance == -1:
            return [-1, -1]
        
        # This is the cheating way that is O(n) time complexity; we will fix this
        left, right = firstInstance, firstInstance
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
            
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
            
        return [left, right]
        
    # This is the binary search algorithm to find our target
    def binarySearch(self, nums: List[int], target: int, left: int, center: int, right: int) -> int:
        # Binary search works by checking to see if our center is above, below, or equal to the target.
        
        # Handling base case
        if nums[center] == target:
            return center
        
        # Before we go any deeper, is our size metric too small?
        if left == center or right == center:
            return -1
        
        # If our number is greater than the target, we need to go left.
        # The position that we go to is left + (center - left) // 2
        # Then our center becomes the left + center move, left stays left, and right becomes center
        if nums[center] > target:
            newCenter = left + ((center-left)//2)
            return self.binarySearch(nums, target, left, newCenter, center)
            
        if nums[center] < target:
            newCenter = center + ((right-center)//2)
            return self.binarySearch(nums, target, center, newCenter, right)
        