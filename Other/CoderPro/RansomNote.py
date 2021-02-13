'''
#3
Trying to spell words using cutouts from a magazine

Given a list of words and a word to spell, can we spell it? 
'''

# Can through each word in the list into a dictionary, tracking the total occurrence.

from typing import List
from collections import defaultdict

# O(n + m) time complexity where n is the length of the magazine, and m is the length of the word.
# O(n) to load everything into the dictionary, O(m) to iterate over each word. We use amortized time complexity for hash table.

# O(n) space complexity, as we load all of the characters in the magazine into a dictionary (n is the length of the magazine).

# Technically, space complexity is O(1) since we have at most 26 characters (or some finite amount for any language, given an alphabet with a finite number of characters)

class Solution():
    def canRansomeNote(self, magazine: List[chr], word: str):
        # Creating our dictionary
        d = defaultdict(lambda: 0)
        for c in magazine:
            d[c.lower()] += 1

        for c in list(word):
            d[c.lower()] -= 1
            if d[c.lower()] < 0:
                return False

        return True

s = Solution()
print(s.canRansomeNote(['A','B','e','D'], 'bed'))