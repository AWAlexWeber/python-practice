''' Find maximum contiguous subarray '''

# Kadanes
from typing import List

class Solution:
    def maximumContiguousSubarray(self, arr: List[int]) -> int:
        # What we will do is iterate over every value, keeping track of the maximal sub and current sum.
        # If our current sum ever gets below zero, we reset the current sum
        if len(arr) <= 0:
            return 0

        maximumSum, currentSum = arr[0], 0
        for n in arr:
            currentSum += n
            maximumSum = max(currentSum, maximumSum)
            if currentSum < 0:
                currentSum = 0

        return maximumSum

s = Solution()
print(s.maximumContiguousSubarray([-1,-2,1,3,4,5,10,-1,-15,-10,20,-100,44]))
print(s.maximumContiguousSubarray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maximumContiguousSubarray([-19,-21,-3,-4,-5,-4,-3,-2,-21]))