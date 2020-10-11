'''
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
Example 4:

Input: s = "1"
Output: 1
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
'''

# Not the fastest solution, but it works (still O(n))
class Solution:
    def numDecodings(self, s: str) -> int:
        return self.numDecode(s, 0, {})
        
    # Recursive function that returns an integer of all the following decode possibilities
    # n represents the start, this way we don't have to do anything crazy
    def numDecode(self, s: str, n: int, m: dict) -> int:

        if n >= len(s):
            # Final possible subsequence, must be valid
            return 1
        
        if n in m:
            return m[n]
        
        l = r = 0
        if self.isValidCharacter(s[n]):
            l = self.numDecode(s, n + 1, m)
        if n + 1 < len(s) and self.isValidCharacter(s[n] + s[n+1]):
            r = self.numDecode(s, n + 2, m)
            
        m[n] = l + r
            
        return l + r
               
        

    def isValidCharacter(self, i: str) -> bool:
        # Checks to see if an integer value is correct
        
        if len(i) > 1 and int(i) < 10:
            return False
        
        i = int(i)
        
        return i >= 1 and i <= 26