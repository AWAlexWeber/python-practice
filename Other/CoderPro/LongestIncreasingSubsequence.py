'''
Given an array reutnring the longest increasing subsequence.
'''

from typing import List
from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int]) -> int:
        memo = defaultdict(lambda: 0)
        for v in range(len(arr) -1, -1, -1):
            maxIncreasing = 0
            for i in range(v, len(arr)):
                if arr[i] < arr[v]:
                    continue
                else:
                    maxIncreasing = max(maxIncreasing, memo[i])
            memo[v] = maxIncreasing + 1
        print(memo)
        return memo[0]

s = Solution()
print(s.longestSubsequence([0,8,4,12,2,10,6,14,1,9,5,13,3]))