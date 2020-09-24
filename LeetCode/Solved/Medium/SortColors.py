'''
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
'''

from typing import List

class Solution:
    # Double pass approach
    def sortColors(self, nums: List[int]) -> None:
        # First sort, move everything that is a 2 to the back and everything else to the front
        # Tracking our positions with i, j where i is the next front position and j is the next back position
        # Before we do any swaps, we move j backwards if there is already a conflicting 2
        j = self.swapSort(0, len(nums) - 1, nums, 2)
        self.swapSort(0, j, nums, 1)
                
    def swapSort(self, i, j, nums, target) -> int:
        while i <= j:
            if nums[i] == target:
                # Move it to the back
                while nums[j] == target and j > i:
                    j -= 1
                    
                # Swap
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1
        return j

    # Single pass approach, using the dutch flag sort
    # This is much faster as it is both in-place and single pass O(n)
    def sort(self, nums: List[int]) -> None:
        i, j, k = 0, 0, len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j + 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1