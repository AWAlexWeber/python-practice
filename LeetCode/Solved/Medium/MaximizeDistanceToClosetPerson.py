'''
849. Maximize Distance to Closest Person

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

 

Example 1:


Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Example 3:

Input: seats = [0,1]
Output: 1
 

Constraints:

2 <= seats.length <= 2 * 104
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
'''

from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Finding maximal left and maximal right
        start_l, start_r = 0, len(seats) - 1
        
        while seats[start_l] != 1 and start_l != start_r:
            start_l += 1
        while seats[start_r] != 1 and start_r != start_l:
            start_r -= 1
            
        # Calculating distances using start_l and start_r
        d, t = float("-inf"), None
        
        # Checking which tuple to start us off with
        if (start_l > len(seats) - 1 - start_r):
            d = start_l
        else:
            d = len(seats) - 1 - start_r
            
        l = start_l
        for i in range(start_l + 1, start_r + 1):
            # Checking to see if we can find a better pair
            if seats[i] == 1:
                max_distance = (i - l) // 2
                if max_distance > d:
                    d = max_distance
                l = i
                
        return d

            