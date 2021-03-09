''' Given a string, find the longest substring that does not have any of the same characters '''

from collections import defaultdict

class Solution:
    def longestSubstring(self, data: str) -> int:
        # This is a sliding window problem.
        # We will keep a set to track the number of duplicate values
        # We will also use a hash to count the number of times they occur.
        # We only increment our sliding window when our set size is zero

        i, j = 0, 0
        maxSize = 0
        visit = set()
        count = defaultdict(lambda: 0)
        while j < len(data):
            # Counting our characters
            c = data[j]
            count[c] += 1
            if count[c] == 2:
                visit.add(c)

            if len(visit) > 0:
                # We must continue forward
                removeC = data[i]
                count[removeC] -= 1
                if count[removeC] == 1 and removeC in visit:
                    visit.remove(removeC)
                i += 1

            j += 1

            if (j - i) > maxSize:
                maxSize = max(maxSize, (j-i))
                print(maxSize,i,j)

        return (j - i)

s = Solution()
print(s.longestSubstring('abcdcbadfedfakzlxvoeaizdfcv'))
print(s.longestSubstring('aabcbbeacc'))