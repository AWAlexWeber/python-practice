'''
713. Subarray Product Less Than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
'''

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        s, i, j, o = 1, 0, 0, 0


        while j <= len(nums):

            # Multiplying the current sum
            if s >= k:
                o += j - i - 2 + 1
                if i >= len(nums):
                    break
                s /= nums[i]
                i += 1

            else:
                if j >= len(nums):
                    break
                s *= nums[j]
                j += 1
        
        while i != j and j > i:
            o += j - i - 1 + 1
            i += 1

        if o < 0:
            return 0
        return o
