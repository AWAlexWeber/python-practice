'''
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
'''

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Binary search making decisions based off of dimensions
        i, j = 0, len(nums)
        while i != j:
            (i, j) = self.selectSection(nums, i, j, (j - i) // 2 + i)
        
        return nums[i]
        
    def selectSection(self, nums: List[int], left: int, right: int, center: int) -> (int, int):
        # Given a midpoint, determine the derection to go based off of an integer tuple
        # Note that the right most value is excluse, ie [int, int)
        if center + 1 < len(nums) and nums[center] == nums[center + 1]:
            # Our i is the left-most index
            # If the size to the right of i + 1 is odd, that is our new direction
            # Else, go left
            if (len(nums) - (center + 1)) % 2 != 0:
                # Going left
                return (left, center)
            else:
                return center + 2, right
            
        elif center - 1 >=0 and nums[center] == nums[center - 1]:
            # Our i is the right most index
            if (len(nums) - center) % 2 != 0:
                # Going left
                return (left, center - 1)
            else:
                return center + 1, right
            
        else:
            # This is the invaid value!
            # Returning equal integers to represent that this is the final value
            return center, center