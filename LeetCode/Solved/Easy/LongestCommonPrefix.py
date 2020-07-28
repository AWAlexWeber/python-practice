'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

from typing import List

# Basic approach here is going to be to just continually iterate across every string until we finish
# This gives us a complexity of O(nk) where n is the number of words, and k is the shortest word length
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        o = ""
        for n in range(0, len(strs[0])):
            c = strs[0][n]
            for s in strs:
                if n >= len(s) or s[n] != c:
                    return o
            o += c
        return o

    def betterLongestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

s = Solution()
print(s.betterLongestCommonPrefix([]))
print(s.betterLongestCommonPrefix(["aabe","aabc","aabd","aabf"]))