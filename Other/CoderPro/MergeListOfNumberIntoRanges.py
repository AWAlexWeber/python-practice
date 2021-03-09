''' Given an integer array, return the ranges of all consecutive numbers '''

from typing import List

class Solution:
    def consecutiveRanges(self, nums: List[int]) -> List[tuple]:

        idx, currentMinimum, output = 1, (None if len(nums) <= 0 else nums[0]), list()
        while idx < len(nums):
            if nums[idx] > nums[idx - 1] + 1:
                # We found a break
                output.append((currentMinimum, nums[idx - 1]))
                currentMinimum = nums[idx]
            idx += 1

        # Outputting the final range
        output.append((currentMinimum,nums[idx-1]))

        return output

s = Solution()

a = [0,2,3,4,5,6,8,9,10,11,15,16,17,20]                
print(s.consecutiveRanges(a))

a = [0,1,2,5,7,8,9,9,10,11,15]                
print(s.consecutiveRanges(a))