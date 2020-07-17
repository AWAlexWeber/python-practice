'''
1486. XOR Operation in an Array
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
Example 2:

Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
Example 3:

Input: n = 1, start = 7
Output: 7
Example 4:

Input: n = 10, start = 5
Output: 2
'''

from typing import List

class Solution:
    def naiveXorOperation(self, n: int, start: int) -> int:
        # Naive O(n) approach
        out = 0
        for x in range(0,n):
            out = out ^ (2*x + start)   

    # Faster O(1) solution
    # This is more of a trick than something you're going to probably find intuitively imho
    def xorOperation(self, n: int, start: int) -> int:
        
        last = start + 2 * (n-1)

        if start % 4 <= 1:
            if n % 4 == 1: 
                return last
            elif n % 4 == 2: 
                return 2
            elif n % 4 == 3: 
                return 2 ^ last
            else: 
                return 0

        else:
            if n % 4 == 1: 
                return start
            elif n % 4 == 2: 
                return start ^ last
            elif n % 4 == 3: 
                return start ^ 2
            else: 
                return start ^ 2 ^ last

s = Solution()
s.naiveXorOperation(5,0)