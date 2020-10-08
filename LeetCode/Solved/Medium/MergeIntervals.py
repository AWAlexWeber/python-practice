'''
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

Constraints:

intervals[i][0] <= intervals[i][1]
'''

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        
        # Ensuring data-format validity (correct input direction)
        intervals = sorted(intervals)
        
        (s, e) = intervals[0]
        
        o = list()
        
        for i in intervals:
            # Checking to see if we append this to our existing interval
            if i[0] > e:
                # Completing the current interval, starting a new one
                o.append([s,e])
                (s, e) = i
            else:
                # Moving our end (if its larger)
                if i[1] > e:
                    e = i[1]
               
        # Appending the final interval
        o.append([s,e])
        return o