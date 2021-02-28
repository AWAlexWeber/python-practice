''' 
Given an array, return the values where it is the product of all other values except itself. You may not use division.

eg:
[1,2,3,4,5] =
[120,60,40,30,24]
'''

from typing import List

# O(n) time, O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nL = [1] * len(nums) # [1,1,2,6,24]
        nR = [1] * len(nums) # [120,60,20,1]

        lVal, rVal = 1, 1
        for idx in range(1, len(nums)):
            lVal *= nums[idx - 1]
            nL[idx] = lVal
        for idx in range(len(nums) - 2, -1, -1):
            rVal *= nums[idx + 1]
            nR[idx] = rVal

        o = [1] * len(nums)
        for idx in range(0, len(nums)):
            o[idx] = (nR[idx] * nL[idx])
        return o

s = Solution()
print(s.productExceptSelf([1,2,3,4,5]))
print(s.productExceptSelf([1,2,3,4]))
