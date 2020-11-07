'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''

from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) <= 0 or sum(nums) < s:
            return 0
        
        l, u, o = 0, 0, float("inf")
        for i in range(len(nums)):
            u += nums[i]
            while u >= s:
                o = min(o, i + 1 - l)
                u -= nums[l]
                l += 1
        return o
                