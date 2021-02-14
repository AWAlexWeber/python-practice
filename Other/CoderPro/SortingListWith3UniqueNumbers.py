''' 
#8
Given a list containing at most 3 unique values, sort the array. [0,1,2,0,1,2] -> [0,0,1,1,2,2]. 
'''

# Famous dutch-flag problem that Djikstra came up with
# Fairly simple, keep track of two headers, i and j.
# i and j both advance through the array, but i represents our swap index and j finds values to swap.
# ie: i moves forward when we swap, j finds values to swap.

from typing import List

class Solution():
    # O(n) time complexity, O(1) space complexity.
    # Note how this beats sorting algorithm time complexity (quicksort worse case O(n^2) and mergesort O(nlogn))
    # Also beats dictionary construction that uses O(n) space complexity.
    def dutchFlag(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        while j < len(nums):
            if nums[j] == 0 and nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
            if nums[i] == 0:
                i += 1
            j += 1

        i, j = 0, 1
        while j < len(nums):
            if nums[j] == 1 and nums[i] == 2:
                nums[j], nums[i] = nums[i], nums[j]
            if nums[i] <= 1:
                i += 1
            j += 1

        return nums

s = Solution()
print(s.dutchFlag([2,1,2]))