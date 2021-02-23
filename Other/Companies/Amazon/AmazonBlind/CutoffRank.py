'''

'''

from typing import List
from collections import defaultdict

class Solution():
    def cutoffRank(self, scores: List[int], cutoffRank: int) -> int:
        # Handling silly sizes
        if cutoffRank == 0:
            return 0

        # Effectively what we are going to do is sort and then count.
        scores.sort(reverse=True)
        currentRank = 1
        adjustRank = 1

        for idx, score in enumerate(scores):
            # If our current value is equal to the next value, do NOT increment current rank but DO increment adjust rank.
            if idx < len(scores) - 1 and score == scores[idx + 1]:
                adjustRank += 1

            # If our current value is not equal to the next value, increment current rank by adjust rank and set adjust rank back to 1
            if idx < len(scores) - 1 and score > scores[idx + 1]:
                currentRank += adjustRank
                adjustRank = 1

            # If our current rank is greater than cutoff rank, return index + 1
            if currentRank > cutoffRank:
                return idx + 1

        # We made it to the end without cutting anyone off, return everyone
        return len(scores)

    def cutoffRankImproved(self, scores: List[int], cutoffRank: int) -> int:
        # Handling some base cases
        if cutoffRank == 0:
            return 0
        if cutoffRank == len(scores):
            return len(scores)

        # Building a cache, this will have at most a size of 100, so we have O(1) size complexity.
        # This is basically a cheating way to do the sort we do in the other solution, since we know our score ranges.
        cache = defaultdict(lambda: 0)

        for score in scores:
            cache[score] += 1

        result = 0
        for i in range(100, -1, -1):
            if cutoffRank <= 0:
                break
            if i not in cache:
                continue
            cutoffRank -= cache[i]
            result += cache[i]
        return result



s = Solution()
print(s.cutoffRank([100,60,60,60,60,60,50],3))
print(s.cutoffRank([100,50,50,25],3))
print(s.cutoffRank([2,2,3,4,5],4))

print(s.cutoffRankImproved([100,60,60,60,60,60,50],3))
print(s.cutoffRankImproved([100,50,50,25],3))
print(s.cutoffRankImproved([2,2,3,4,5],4))