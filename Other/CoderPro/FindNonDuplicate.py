'''
# 10
Given an array of randomly sorted integers, find the non-duplicate.
'''

# Two approaches; optimizing for space complexity and optimizing for time complexity.
# Space complexity optimization will give us O(nlogn) time and O(1) space.
# We sort the array and perform a binary search on the side that has an odd number of digits until the value we're at is unique on the left and right

# Time complexity optimization will give us O(n) time and O(n) space.
# We simply iterate on every value and track a dictionary of all values. When we reach the second value, we delete the key. We then get the only remaining key.

# TODO: XOR

from collections import defaultdict
from typing import List

class SolutionTimeComplexity():
    def findNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        d = defaultdict(lambda: 0)
        # O(n) time, O(n) space to keep all of those digits in our dictionary
        for n in nums:
            d[n] += 1
            if d[n] == 2:
                del d[n]

        # Really just O(1)
        for k in d.keys():
            return k

s1 = SolutionTimeComplexity()
print(s1.findNonDuplicate([1,2,3,4,5,6,1,2,3,4,5]))

class SolutionSpaceComplexity():
    # Tiny helper function to keep track
    def isUnique(self, nums: List[int], n: int) -> bool:
        if n == 0 and nums[n] != nums[n + 1]:
            return True
        elif n == len(nums) - 1 and nums[n] != nums[n - 1]:
            return True
        elif nums[n] != nums[n - 1] and nums[n] != nums[n + 1]:
            return True

        return False

    def findNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Sorting O(nlogn)
        nums = sorted(nums)
        print(nums)

        # Iterative binary search (which keeps our stack size small at O(1))
        # O(logn) time
        l, c, r = 0, len(nums) // 2, len(nums)
        f = 0
        while not self.isUnique(nums, c):
            f += 1
            if f > 10:
                break

            # Getting our compare index
            comp_index = c + 1
            if nums[c] == nums[c + 1]:
                comp_index = c
            
            if comp_index % 2 != 0:
                # Our target is in the left
                new_c = l + ((c - l) // 2)
                l, c, r = l, new_c, c

            else:
                # Our target is in the right
                new_c = c + ((r-c) // 2)
                l, c, r = c, new_c, r

        return nums[c]

s2 = SolutionSpaceComplexity()
print(s2.findNonDuplicate([1,2,3,4,5,52,52,9,1,2,3,4,5]))