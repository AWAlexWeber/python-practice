'''
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
'''

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        
        for n in range(len(nums)):
            
            if nums[n] < 0 or nums[n] >= len(nums):
                nums[n]=0
                
        for n in range(len(nums)):
            nums[nums[n]%len(nums)]+=len(nums)

        for n in range(1,len(nums)):
            if nums[n] // len(nums)==0:
                return n
            
        # Array is perfectly organized, returning the length
        return len(nums)