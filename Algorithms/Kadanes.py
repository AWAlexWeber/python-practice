'''
    Maximum contiguous subarray. Very common problem.
'''

from typing import List

def kadanes(nums: List[int]) -> int:
    # Keeping track of our maximal value
    maximalValue = float("-inf")

    # Keeping track of our current maximal value
    maximalCurrent = 0

    for n in nums:
        maximalCurrent = maximalCurrent + n
        if maximalCurrent > maximalValue:
            maximalValue = maximalCurrent

        if maximalCurrent < 0:
            maximalCurrent = 0

    return maximalValue

print(kadanes([1,2,3,0,-1,2,1]))

        