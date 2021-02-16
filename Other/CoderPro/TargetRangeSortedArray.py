'''
#6

Given a sorted array, return the first and last indexes of a target number

[1,3,3,5,7,8,9,9,15], target = 9, return [6,7]
'''

# TODO: Iterative binary search with O(1) space

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

class SolutionTwo():
    # Recursive search that uses O(logn) space complexity (due to search space stack with recursion) and O(logn) time complexity with our two searches.
    # Here we are going to use two binary sorts, but one that finds the index where the value to the left is less, and one where the value to the right is greater.
    def findRangeOfTargetInSortedArray(self, nums: List[int], target: int) -> tuple:
        return [self.findSearch(nums, 0, len(nums)//2, len(nums), target, True), self.findSearch(nums, 0, len(nums)//2, len(nums), target, False)]

    # Helper function; normal binary search, but we pass in a parameter called 'direciton' that tells us if we need to ensure that the value to the left/right is greater than center
    # direction = True means our value to the left needs to be less, and false means our value to the right needs to be greater.
    # Other than that, this is simple binary search
    def findSearch(self, nums: List[int], left: int, center: int, right: int, target: int, direction: bool):

        # Handling if we didn't find our value
        if left == center and right == center:
            return -1

        # Handling success state
        if direction:
            # Left-sided search
            if nums[center] == target and (center - 1 < 0 or nums[center - 1] < target):
                return center

        else:
            # Right-sided search
            if nums[center] == target and (center + 1 >= len(nums) or nums[center + 1] > target):
                return center

        # Alright, now we handle going left or going right. Note we need to force going left if we're sera
        if nums[center] > target or (nums[center] == target and direction):
            # Going left
            # Calculating our new center
            newCenter = left + ((center-left)//2)
            return self.findSearch(nums, left, newCenter, center, target, direction)

        elif nums[center] < target or (nums[center] == target and not direction):
            # Going right
            # Calculating our new center
            newCenter = center + ((right-center)//2)
            return self.findSearch(nums, center, newCenter, right, target, direction)

class SolutionThree():
    def findRangeOfTargetInSortedArray(self, nums: List[int], target: int) -> tuple:
        # Iterative binary search for the left most value
        return [self.iterativeBinarySearch(nums, target, True), self.iterativeBinarySearch(nums, target, False)]
        
    # Iterative search; goes left or right depending on dir (true=left)
    def iterativeBinarySearch(self, nums: List[int], target: int, dir: bool) -> int:
        l, c, r = 0, len(nums) // 2, len(nums)
        while l != c or r != c:
            print(l,c,r)
            if nums[c] == target:
                # Handling left-target
                if dir and (c == 0 or nums[c - 1] < target):
                    return c
                elif not dir and (c == len(nums) - 1 or nums[c + 1] > target):
                    return c

                # Hit target but we have more to go
                else:
                    if dir:
                        # Going left
                        newCenter = l + ((c-l) // 2)
                        l, c, r = l, newCenter, c

                    else:
                        # Going right
                        newCenter = c + ((r-c) // 2)
                        l, c, r = c, newCenter, r

            else:
                if nums[c] > target:
                    newCenter = l + ((c-l) // 2)
                    l, c, r = l, newCenter, c
                    continue

                else:
                    # Going right
                    newCenter = c + ((r-c) // 2)
                    l, c, r = c, newCenter, r
                    continue

        return -1




s = Solution()
s2 = SolutionTwo()
s3 = SolutionThree()
print(s.findRangeOfTargetInSortedArray([9,9,9,9,9,9,9],9))
print(s2.findRangeOfTargetInSortedArray([9,9,9,9,9,9,9],9))
print(s3.findRangeOfTargetInSortedArray([9,9,9,9,9,9,9],9))