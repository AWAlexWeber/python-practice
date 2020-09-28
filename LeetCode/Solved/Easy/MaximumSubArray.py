'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Kadane's maximum sub-array algorithm
        m, local_max = nums[0], nums[0]
        
        for n in nums[1:]:
            local_max = max(n, local_max + n)
            m = max(local_max, m)
        
        return m