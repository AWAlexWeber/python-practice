'''
#6

Given a sorted array, return the first and last indexes of a target number

[1,3,3,5,7,8,9,9,15], target = 9, return [6,7]
'''

# TODO: Iterative binary search, O(logn) time, O(1) space

from typing import List

# This can be done by using binary search until we find the target, then performing binary search again.

# Time complexity: O(n) because we cheat and expand off of our target index in linear time.
# Space complexity: O(logn) because of our binary search recursive calls that build up on our stack.

class Solution():

    def findRangeOfTargetInSortedArray(self, nums: List[int], target: int) -> tuple:
        # Finding our initial index
        targetIndex = self.binarySearchForTarget(nums, target, 0, len(nums) // 2, len(nums))

        # Handling not found
        if targetIndex == -1:
            return [-1, -1]
        
        # First approach; linerally expand our target index. Note that this reduces our time complexity from the nice O(logn) of binary search to the ugly linear time of O(n).
        leftIndex, rightIndex = targetIndex, targetIndex

        while leftIndex - 1 >= 0 and nums[leftIndex - 1] == target:
            leftIndex -= 1

        while rightIndex + 1 < len(nums) and nums[rightIndex + 1] == target:
            rightIndex += 1

        return [leftIndex, rightIndex]

    # Function returns the first found index of the target.
    def binarySearchForTarget(self, nums: List[int], target: int, left: int, center: int, right: int) -> int:
        # If we've found our target, return the index.
        if nums[center] == target:
            return center

        # If we've closed our gap to zero we must've not found it.
        elif left == center or right == center:
            return -1

        # Otherwise, returning the value from the right or the left
        else:
            if nums[center] > target:
                #  We need to go left; value at center is too big
                newCenter = left + ((left + center) // 2)
                return self.binarySearchForTarget(nums, target, left, newCenter, center)

            else:
                # We need to go right; value at center is too small
                newCenter = center + ((right - center) // 2)
                return self.binarySearchForTarget(nums, target, center, newCenter, right)

s = Solution()
print(s.findRangeOfTargetInSortedArray([1,3,3,5,7,8,9,9,15],9))
print(s.findRangeOfTargetInSortedArray([1,2,3,9,9,9,9,9,9,9,15],9))