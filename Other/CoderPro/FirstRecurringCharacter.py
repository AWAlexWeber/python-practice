'''
Find the first recurring character.
'''

class Solution:
    def firstRecurringCharacter(self, word: str) -> str:
        h = {}
        for c in word:
            if c.lower() in h:
                return c.lower()
            h[c.lower()] = 1

s = Solution()
print(s.firstRecurringCharacter("qwertty"))