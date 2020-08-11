'''
8. String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
Thefore INT_MIN (−231) is returned.
'''

# Converting a string to an integer
class Solution:
    def myAtoi(self, str: str) -> int:
        # This is mostly handling edge cases to be honest
        # Moving ourselves to the first index of the number
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1

        # Checking if its negative
        negative = 1
        if i < len(str) and str[i] == '-':
            negative = -1
            i += 1
        elif i < len(str) and str[i] == '+':
            i += 1

        # This should've moved us to the first word
        j = i
        while j < len(str) and str[j].isnumeric():
            j += 1

        if i == j:
            return 0

        # Creating our number
        num = [''] * (j - i)
        c = 0

        while i != j:
            num[c] = str[i]
            i += 1
            c += 1

        v = negative * int(''.join(num))
        if v <= -2147483648:
            return -2147483648
        elif v >= 2147483648:
            return 2147483647

        else:
            return v

s = Solution()
print(s.myAtoi("   42"))
print(s.myAtoi("   my favorite number is 1"))
print(s.myAtoi("                      1"))
print(s.myAtoi("   "))
print(s.myAtoi(" 2464262477253875385853   "))
print(s.myAtoi(" -452   "))
print(s.myAtoi(" -450 is a great number   "))
print(s.myAtoi("42"))
print(s.myAtoi("   -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi("   +42"))