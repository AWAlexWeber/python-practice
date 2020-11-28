'''
415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        c, o = 0, ""
        while i >= 0 or j >= 0:
            n1, n2 = (int(num1[i]) if i >= 0 else 0), (int(num2[j]) if j >= 0 else 0)
            s = n1 + n2 + c
            o = str((s % 10)) + o
            if (n1 + n2 + c) >= 10:
                c = 1
            else:
                c = 0
            i -= 1
            j -= 1
        if c == 1:
            o = '1' + o
        return o
            