'''
1063. Number of Valid Subarrays

Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following condition:

The leftmost element of the subarray is not larger than other elements in the subarray.

 

Example 1:

Input: [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
Example 2:

Input: [3,2,1]
Output: 3
Explanation: The 3 valid subarrays are: [3],[2],[1].
Example 3:

Input: [2,2,2]
Output: 6
Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].
 

Note:

1 <= A.length <= 50000
0 <= A[i] <= 100000
'''

from typing import List

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        s, n = [], [len(nums)] * len(nums)
        for i, v in enumerate(nums):
            while s and s[-1][1] > v:
                n[s.pop()[0]] = i
            s.append([i, v])
        return sum([v - i for i, v in enumerate(n)])