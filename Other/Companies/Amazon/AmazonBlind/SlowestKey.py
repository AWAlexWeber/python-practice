'''
'''

from typing import List

class Solution():
    def slowestKey(self, keyTimes: List[tuple]) -> chr:
        # We will sort our keyTimes in O(nlogn) time and O(n) space, then iterate over it finding the 'biggest' gap in times.
        # There may be a way to do this in linear time but it's not obvious to me.
        s = sorted(keyTimes, key = lambda t: t[1])

        biggestGapKey, biggestGap, previousTime = None, 0, 0
        for key, time in s:
            if (time - previousTime) > biggestGap:
                biggestGap, biggestGapKey = (time - previousTime), chr(key + 97)
            
            # Taking the smallest (smallest lexicographic letter) letter for ties
            if (time - previousTime) == biggestGap and (key + 97) < ord(biggestGapKey):
                biggestGapKey = chr(97+key)

            previousTime = time
        return biggestGapKey

s = Solution()
slowestKey = s.slowestKey([[0, 2], [1,5], [0,9], [2, 15], [2,12], [3,19]])
print(slowestKey)
