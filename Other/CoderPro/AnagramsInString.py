'''
Given a string find the starting and ending locations of all anagrams of another string within the given string.
'''

from typing import List

class Solution:
    def findAnagrams(self, s: str, target: str) -> List[tuple]:
        # Basically going to use a 26 sized integer array to keep our size complexity O(1) and space complexity O(N).
        targetMask = [0] * 26
        for c in target:
            targetMask[ord(c.lower()) - 97] += 1

        currentMask = [0] * 26
        output = list()
        for idx, c in enumerate(s):
            currentMask[ord(c.lower()) - 97] += 1
            if idx >= len(target) - 1:
                if self.compareMask(currentMask, targetMask):
                    output.append((idx - len(target) + 1, idx))

                exitCharacter = s[idx - len(target) + 1]
                currentMask[ord(exitCharacter.lower()) - 97] -= 1

        return output

    def compareMask(self, current: List[int], target: List[int]) -> bool:
        for idx in range(26):
            if current[idx] != target[idx]:
                return False
        return True

# abcabcabc, abc
s = Solution()
print(s.findAnagrams('acdbacdacb','abc'))