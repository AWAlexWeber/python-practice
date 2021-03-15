'''
Given an array of integers, return the subarray that equals a target sum.
'''

import random
from typing import List

class Solution:
    def targetSubarray(self, arr: List[int], target: int) -> List[int]:
        # This is a two pointers sliding window problem
        currentSum, i, j = arr[0], 0, 1
        while j < len(arr) and currentSum != target:
            if currentSum < target:
                currentSum += arr[j]
                j += 1
            elif currentSum > target:
                currentSum -= arr[i]
                i += 1

        while currentSum > target:
            currentSum -= arr[i]
            i += 1

        if currentSum == target:
            return arr[i:j]
        else:
            return []

s = Solution()