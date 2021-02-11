'''
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Time complexity of O(s + t), space complexity of O(26)
        i = [0] * 26
        
        for c in s:
            i[97 - ord(c.lower())] += 1
        for c in t:
            i[97 - ord(c.lower())] -= 1
            
        # Validating our i array is zero
        for c in i:
            if c != 0:
                return False
        return True