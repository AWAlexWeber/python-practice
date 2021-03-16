'''
Given an array of +/- numbers that are sorted, return the array in sorted order with the values squared.
'''

from typing import List

# Obvious answer is O(nlogn), but we can do this in O(n) time using two pointers.
class Solution:
    def sortedSquareArray(self, arr: List[int]) -> List[int]:
        
        i, j = 0, 0
        while arr[j] < 0:
            j += 1
        if i == j:
            return arr

        # Now we have two pointers, one starting at 0 in the negative position, and one starting at the first positive index
        output = list()
        i = j - 1
        while len(output) < len(arr):
            if j < len(arr) and arr[j] < abs(arr[i]):
                output.append(arr[j]**2)
                j += 1
            else:
                output.append(arr[i]**2)
                i -= 1
        
        return output

s = Solution()
print(s.sortedSquareArray([-5,-3,-1,0,1,4,5]))