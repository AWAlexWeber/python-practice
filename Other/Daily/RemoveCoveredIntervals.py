'''
Remove Covered Intervals

Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.
'''

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        c, intervals, = 1, sorted(intervals)
        current = intervals[0]

        for i in range(1, len(intervals)):
            # Checking if overlap can exist
            if intervals[i][0] <= current[0] and current[1] <= intervals[i][1]: 
                # Our current is covered by this guy
                current = intervals[i]
                continue

            elif current[0] <= intervals[i][0] and intervals[i][1] <= current[1]:
                # This overlaps the other
                # Continue
                continue

            else:
                current = intervals[i]
                c += 1

        return c

s = Solution()
print(s.removeCoveredIntervals( [[1,2],[1,4],[3,4]] ))