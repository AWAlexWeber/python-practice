'''
Daily August 4th 2020

Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
'''

import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # Base case
        if num == 1:
            return True
        
        c = 4
        while c <= num:
            if c == num:
                return True
            c *= 4
    def fasterIsPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        return math.log(num,4).is_integer()