'''
Given three colors, sort them.
'''

from typing import List

# This is just a variant on the dutch flag problem

class Solution:
    def sort(self, arr: List[int]) -> List[int]:
        # First we are going to swap all of the first value to the start of the array.
        # Then we are going to swap all of the second value to the second spot of the array
        # We'll need to find our three values first
        s = set()
        for v in arr:
            s.add(v)

        l = list(s)
        s1 = l[0]

        i = 0
        for idx in range(0, len(arr)):
            if arr[idx] == s1:
                # Swap to i
                arr[i], arr[idx] = arr[idx], arr[i]
                i += 1

        s1 = l[1]
        for idx in range(0, len(arr)):
            if arr[idx] == s1:
                # Swap to i
                arr[i], arr[idx] = arr[idx], arr[i]
                i += 1

        return arr

s = Solution()
print(s.sort([1,1,1,1,2,2,2,3,3,3,2,2,1,1]))