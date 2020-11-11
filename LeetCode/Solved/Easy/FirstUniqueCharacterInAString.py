'''
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        v, o = set(), set()

        # O(n) but with two loops. Could be improved to use a linked list but would not change complexity.
        for c in s:
            if c in v:
                o.add(c)
            else:
                v.add(c)
        for i in range(len(s)):
            if s[i] not in o:
                return i
        return -1