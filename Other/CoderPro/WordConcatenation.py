'''
Given a list of words, check if any words within the list can be combined to form another word within the list
[cat, cats, dog, catsdog] can combine cats and dog to form catsdog which is in the list
'''

from typing import List
from functools import lru_cache

class Solution:
    def wordConcat(self, arr: List[str]) -> List[str]:

        @lru_cache(None)
        def search(word: str, depth: int=0):
            if len(word) == 0:
                return True
        
            for targetWord in arr:
                if targetWord == word and depth == 0:
                    continue

                if len(targetWord) > len(word):
                    continue

                if targetWord == word[0:len(targetWord)] and search(word[len(targetWord):], depth+1):
                    return True

            return False
        
        output = list()
        for word in arr:
            if len(word) == 0:
                continue
            if (search(word)):
                output.append(word)

        return output

s = Solution()
print(s.wordConcat(['cat','cats','dog','catcats', 'catdog', 'catdogs']))
print(s.wordConcat(['']))