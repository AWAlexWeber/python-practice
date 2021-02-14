'''
1010. Pairs of Songs With Total Durations Divisible by 60

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
'''

from typing import List
from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Handling some base cases
        if len(time) <= 1:
            return 0
        
        # Interesting variant on two sums
        # Since we are only interested in evenly being divided by 60, we can toss asside > 60
        # After that, it becomes a two sum problem
        
        # D represents our dictionary used to solve two sum; it tracks the number of occurences for a value
        # We need to use a dictionary and not a set because 60 and 120 represent the same thing, so we can't just use 0.
        d = defaultdict(lambda: 0)
        for value in time:
            d[value % 60] += 1
            
        # Tracking the total count
        count = 0
        
        dKeys = list(d.keys())
        for key in dKeys:
            # Ensuring we don't double count by skipping greater than 30
            if key > 30:
                continue
                
            elif key == 30 or key == 0:
                for c in range(1, d[key]):
                    count += (c)
                
            else:
                count += (d[60 - key] * d[key])
        
        return count
    