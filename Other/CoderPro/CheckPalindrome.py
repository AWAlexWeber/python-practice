'''
Given a string, check if it can be rearranged to form a palindrome.
'''

from collections import defaultdict

class Solution:
    def checkForPalindrome(self, s: str) -> bool:
        # Basically counnting all of the characters. We must have an all even count, or an all even count with one odd
        h = defaultdict(lambda: 0)
        for c in s:
            h[c.lower()] += 1
        isOddUsed = False
        for c in s:
            if h[c] % 2 == 1:
                if not isOddUsed:
                    isOddUsed = True
                else:
                    return False
        return True

s = Solution()
print(s.checkForPalindrome('foxyfoxfoxfox'))