'''
1464. Maximum Product of Two Elements in an Array

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
'''

from typing import List

# This is a very straightforward problem
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = m2 = i1 = i2 = 0
        for i, n in enumerate(nums):
            if n >= m1:
                m2, i2 = m1, i1
                m1, i1 = n, i
            elif n >= m2:
                m2, i2 = n, i

        return (nums[i1] - 1) * (nums[i2] - 1)

    # Second solution that sorts the array first
    # This has a worse complexity
    def sortedMaxProduct(self, nums: List[int]) -> int:
        return ((sorted(nums)[-1]) - 1) * ((sorted(nums)[-2] - 1))