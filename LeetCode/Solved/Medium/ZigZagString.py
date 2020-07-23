'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

import math

# This answer is trash, look into reducing the if/elif/else by finding a way to arbitrarily know how much to move J at all times by

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case handling
        if numRows == 1 or numRows >= len(s):
            return s

        out = ""
        cycleCount = 2 * numRows - 2
        for i in range(0, numRows):

            # If we are the top, center, or middle we have an even movement
            if i == 0 or i == numRows - 1:
                j = i
                while j < len(s):
                    out += s[j]
                    j += cycleCount

            # Performing the central movement
            elif i == (numRows - 1) / 2:
                j = i
                while j < len(s):
                    out += s[j]
                    j += (int)(cycleCount / 2)

            # Performing all other movements
            # In this case our movement 
            else:
                j = i
                moveTuple = [cycleCount - (2*i), 2*i]
                tupleIndex = 0
                while j < len(s):
                    out += s[j]
                    j += (int)(moveTuple[tupleIndex])
                    tupleIndex = tupleIndex + 1
                    tupleIndex = tupleIndex % 2

        return out

    # Weirder solution, but I like it quite a lot
    def weirdConvert(self, s: str, numRows: int) -> str:

        # Edge cases
        if numRows <= 1 or len(s) <= numRows:
            return s

        # Generating our output
        out = [''] * numRows

        i = 0
        step = 0
        for c in s:

            out[i] += c

            if i == 0:
                step = 1

            elif i == numRows - 1:
                step = -1

            i += step

        return ''.join(out)
        


s = Solution()
print(s.weirdConvert("HELLOTHEREHELLOTHERE", 5))

# Input: HELLOTHEREHELLOTHERE
# Expected output: HRHEEETELHHORLTELEOL