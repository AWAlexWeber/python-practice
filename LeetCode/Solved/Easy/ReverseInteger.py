'''
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution:
    # Naive, straightforward solution
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        o = ''
        for i in range(len(s) -1, -1, -1):
            o += s[i]

        i = int(o)
        if i > 2147483648 or i < -2147483647:
            return 0

        else:
            return (-i if x < 0 else i)

    # Very small a compact solution
    def reverseTiny(self, x):
        s=cmp(x,0);r=int(repr(s*x)[::-1]);return(r<2**31)*s*r

def cmp(a, b):
    return (a > b) - (a < b) 

s = Solution()
print(s.reverseTiny(-12345))