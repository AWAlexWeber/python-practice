'''
Given a set of intervals, return the minimum set such that overlapping intervals are combined.
'''

from typing import List

class Solution:
    def mergeIntervals(self, intervals: List[tuple]) -> List[tuple]:
        # First we sort
        intervals.sort(key=lambda t: t[0])
        
        output = list()
        idx = 0
        while idx < len(intervals):
            # Attempting to merge with the next interval
            currentInterval = intervals[idx]
            while idx < len(intervals) - 1 and self.canMerge(currentInterval, intervals[idx + 1]):
                newLeft = min(currentInterval[0], intervals[idx + 1][0])
                newRight = max(currentInterval[1], intervals[idx + 1][1])
                currentInterval = (newLeft, newRight)
                idx += 1
                continue

            output.append(currentInterval)
            idx += 1

        return output

    def canMerge(self, interval: tuple, match: tuple) -> bool:
        # We need to check if we can merge these intervals. They can be merged if:
        # [1,10], [0,4] -> Interval overlaps start
        # [1,10], [4,6] -> Interval overlaps middle
        # [1,10], [9,15] -> Interval overlaps end
        # [1,10], [0,11] -> Interval sits within.
        if match[0] < interval[0] and match[1] > interval[0]:
            return True

        elif interval[0] < match[0] and match[1] < interval[1]:
            return True

        elif match[0] < interval[1] and match[1] > interval[1]:
            return True

        else:
            return False

s = Solution()
print(s.mergeIntervals([(0,11),(7,8),(9,10)]))
print(s.mergeIntervals([[1, 3], [5, 8], [4, 10], [20, 25]]))