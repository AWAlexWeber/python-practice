'''
Character mapping. Given a string (abc) and another string (def) determine if we can match one character to exactly one other string.
'''

class Solution:
    def canCharacterMap(self, s: str, t: str) -> bool:
        # Is the number of unique characters in the first string equal to the number of unique characters in the second string.
        # Can solve in O(n + k) time and O(1) space
        sMap, tMap = [0] * 26, [0] * 26
        for c in s:
            sMap[ord(c.lower()) - 97] = 1
        for c in t:
            tMap[ord(c.lower()) - 97] = 1
        return sum(sMap) == sum(tMap)

s = Solution()
print(s.canCharacterMap('abc','def'))
print(s.canCharacterMap('aaaabbabababababacccabaccc','defX'))
print(s.canCharacterMap('aac', 'def'))