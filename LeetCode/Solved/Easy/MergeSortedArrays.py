'''
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        i, j, k, output = 0, 0, 0, [0] * (n + m)
        while k < (n + m):
            if i < m and (j >= n or nums1[i] < nums2[j]):
                output[k], i, k = nums1[i], i + 1, k + 1
            else:
                output[k], j, k = nums2[j], j + 1, k + 1

        for i, v in enumerate(output):
            nums1[i] = v