'''
Find all values such that the value at a given index is equal to the index (fixed point).
'''

from typing import List

class Solution:
    def fixedPoints(self, arr: List[int]):
        output = list()
        for idx, value in enumerate(arr):
            if idx == value:
                output.append(value)
        return output

    def fixedPointsSorted(self, arr: List[int]):
        # Given that our input is sorted, we can search more easily
        left, right = 0, len(arr)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                return mid
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1

        return None

s = Solution()
print(s.fixedPointsSorted([-5,1,3,4]))
print(s.fixedPointsSorted([-5,-4,0,4,4]))