'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        h, c, s = {0: 1}, 0, 0
        for i in range(len(nums)):
            s += nums[i]
            if (s - k) in h:
                c += h[s - k]
            h[s] = (h[s] if s in h else 0) + 1
        return c
        