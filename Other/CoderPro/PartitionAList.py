'''
Partition a list such that, given a number k, all elements less than k are on the left and all elements greater are on the right.
'''

from typing import List

class Solution:
    def partition(self, arr: List[int], k: int) -> List[int]:
        # Essentially just the partitioning component of quicksort
        i, j = 0, len(arr) - 1
        while i <= j:
            if arr[j] > k:
                j -= 1
                continue

            if arr[i] <= k:
                i += 1
                continue
            
            arr[i], arr[j] = arr[j], arr[i]
        return arr

s = Solution()
print(s.partition([8,9,2,4,1,0,5,4,7,8,1,2,3,1,6,7,9,0,5,2,1,5,2,3], 4))
print(s.partition([8, 9, 9, 2, 4, 1, 1, 0], 3))