'''
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        mL = 0
        mR = 1
        
        for i in range(0,len(s)):
            
            l1 = r1 = 0
            l2 = r2 = 0
            
            if i + 1 < len(s) and s[i] == s[i+1]:
                # Attempt to expand our palindrome
                l1, r1 = self.expandPalindrome(s,i,i+1)
                
            if i + 2 < len(s) and s[i] == s[i+2]:
                l2, r2 = self.expandPalindrome(s, i, i+2)
                
            l = r = 0
            if r2 - l2 > r1 - l1:
                l = l2
                r = r2
            else:
                l = l1
                r = r1
                
            if r - l > mR - mL:
                mR = r
                mL = l
                
        return s[mL:mR]
                
    # Function that helps us expand our palindrome
    def expandPalindrome(self, s: str, l: int, r: int) -> int:
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return l + 1, r