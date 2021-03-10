'''
Given a set of words, determine if a chain can be formed from the last letter to the first letter, such that you arrive back at the first word skipping no elements
'''

from typing import List
from collections import defaultdict

class Solution:
    def canCircle(self, words: List[str]) -> bool:
        # We are going to form our edges first
        edges = defaultdict(lambda: list())

        for word in words:
            firstLetter = word[0]
            edges[firstLetter].append(word)

        # Now we will attempt to find a chain. Note that since a chain must include every element, we can pick arbitrarily a startpoing point.
        # This is basically DFS with backtracking.
        def dfs(word: str, visit: list=list(), visitSet: set=set()) -> bool:

            if word in visitSet:
                if word == visit[0] and len(visitSet) == len(words):
                    return True
                else:
                    return False

            visit.append(word)
            visitSet.add(word)

            lastLetter = word[-1]
            for nextWord in edges[lastLetter]:
                if dfs(nextWord, visit, visitSet):
                    return True

            # Is our set size equal to 
            visit.pop(len(visit)-1)
            visitSet.remove(word)

            return False

        return dfs(words[0])

s = Solution()
print(s.canCircle(['apple','eggs','snack','karat','tuna']))
print(s.canCircle(['apple', 'eggs', 'snack', 'karat', 'tunax']))