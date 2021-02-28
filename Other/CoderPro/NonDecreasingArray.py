'''
Given a 1d array of integers, determine if it can be made non-decreasing with a single modification
'''

from typing import List

# O(n) solution
class Solution:
    def nonDecreasing(self, nums: List[int]) -> bool:
        didMove = False
        for idx, num in enumerate(nums):
            if idx > 0 and num < nums[idx - 1]:
                # We must move
                if not didMove:
                    didMove = True
                    if nums[idx + 1] > nums[idx]:
                        nums[idx - 1] = nums[idx]
                    else:
                        nums[idx] = nums[idx - 1]
                else:
                    return False

        return True

print(Solution().nonDecreasing([4, 1, 2]))
print(Solution().nonDecreasing([3, 2, 4, 1]))
print(Solution().nonDecreasing([-1,4,2,3]))
print(Solution().nonDecreasing([-1,4,2,1]))
print(Solution().nonDecreasing([4,4,2,3,5]))