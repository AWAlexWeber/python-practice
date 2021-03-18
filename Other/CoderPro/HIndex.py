'''
Calculate the h-index given an array.
'''

from typing import List
from collections import defaultdict

class Solution:
    def hIndex(self, arr: List[int]) -> int:
        # O(n) time O(n) space.
        s, m = defaultdict(lambda: 0), max(arr)
        for p in arr:
            s[p] += 1

        # O(k) where k is the largest value.
        i, c = m + 1, 0
        while i > 0: 
            if i in s:
                c += s[i]
            if i == c:
                return c
            i -= 1
        return c

s = Solution()
print(s.hIndex([3,5,0,1,3,5,9,7,7]))