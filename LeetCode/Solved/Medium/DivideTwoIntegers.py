'''
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

from typing import List

# Slow solution that effectively implements long-division
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        absDividend, absDivisor, r, o, i = abs(dividend), abs(divisor), 0, [0] * len(str(abs(dividend))), 0
        for n in str(absDividend):
            # Appending our remainder to the front of the digit
            n = int(str(r) + n)
            c, r = self.divideDigits(n, absDivisor)
            o[i], i = str(c), i + 1

        o = int(''.join(o))

        # Checking mathematical limits

        if (dividend < 0 and divisor >= 0) or (dividend > 0 and divisor < 0):
            o = -o

        # Checking for mathematical limits
        if o <= -2147483649:
            return -2147483648
        elif o >= 2147483648:
            return 2147483647

        return o
        
    # This is our additive divide
    # This is where all of the real processing will happen
    # The above is really just work to help minimize the amount of work that goes on here
    def divideDigits(self, dividend: int, divisor: int) -> (int, int):
        c, d = 0, divisor
        while d <= dividend:
            c, d = c + 1, d + divisor
        r = dividend - d + divisor
        return c, r

    # Faster solution that uses bitwise manipulation
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1            
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))
        

s = Solution()
print(s.divide(7,-3))