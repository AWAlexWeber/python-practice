'''
https://aonecode.com/interview-question/maximum-bounded-array

Basically, given a length n, a lowerBound and upperBound, construct an array that
1) is maximal
2) has a length of n
3) starts going up, then goes down. both the up section and down section must have a length of at least 1
'''

from typing import List

class Solution():
    def maximumBoundedArray(self, n: int, lowerBound: int, upperBound: int) -> List[int]:
        # Handling some base cases
        if n <= 2: # Need at least 3 values to go up and down
            return None

        if lowerBound > upperBound:
            return None

        # Determining our bounds size (adding 1 since our range is inclusive)
        boundSize = upperBound - lowerBound + 1

        # Constructing our output
        output = list()

        # First datapoint we need to know is how far down do we start going up.
        # [1,2,3,4,3,2,1], for example with bounds [1,4] and k = 7, we start at (upperBounds - (k - boundSize)) if boundSize < k
        if boundSize < n:
            value = upperBound - (n - boundSize)
        else:
            value = upperBound - 1

        if value < lowerBound:
            return None

        while value <= upperBound:
            output.append(value)
            value += 1

        value -= 1
        while len(output) != n:
            if value < lowerBound:
                return None
            value -= 1
            output.append(value)

        return output

s = Solution()
print(s.maximumBoundedArray(7,10,13))