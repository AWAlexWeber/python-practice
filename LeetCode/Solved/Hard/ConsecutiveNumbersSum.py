'''
829. Consecutive Numbers Sum

Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
'''

import math

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # O(N//2)
        count = 0
        upper_limit = ceil((2 * N + 0.25)**0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            # x should be integer
            if (N - k * (k + 1) // 2) % k == 0:
                count += 1
        return count

    def consecutiveNumbersSumSlow(self, N: int) -> int:
        # O(N//2). Exceeds run time, but does provide valid answer
        
        # Base case
        if N == 1:
            return 1
        
        o = 1 # Adding one for (N)
        if N % 2 == 1:
            o += 1 # Adding (N//2, N//2+1)
        l, r, s = 1, 1, 1
        while r <= N // 2:
            while s > N:
                s -= l
                l += 1
            if s == N:
                o += 1
                s -= l
                l += 1
            r += 1
            s += r
        return o