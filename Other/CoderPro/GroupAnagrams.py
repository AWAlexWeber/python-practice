'''
Given anagrams, group them together
'''

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, words: List[str]) -> List[str]:
        # Grouping anagrams by the hashing the characters within the string. Note we assume capital letters don't matter.
        characterSet = [0] * 26

        # O(n) space.
        s = defaultdict(lambda: list())

        # Going through each word. This is O(n) time.
        for word in words:
            newCharacterSet = characterSet[:]
            for c in word:
                # Converting to int
                v = ord(c.lower())
                v -= 97
                newCharacterSet[v] += 1
            stringMap = str(newCharacterSet)
            s[stringMap].append(word)

        output = list()
        for k in s.keys():
            output.append(s[k])
        return output

s = Solution()
print(s.groupAnagrams(['abc', 'bcd', 'cba', 'cbd', 'efg']))
