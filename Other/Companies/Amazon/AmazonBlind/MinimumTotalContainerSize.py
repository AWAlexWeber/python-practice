''' Same problem as minimum difficulty of job schedule.
You want to move N items in k days (N >= k). You have to move at least one item per day. The items are listed in array P, where P[i] is size of item i. You can move item i only if all items from 0 to [i - 1] are already moved. Every day you need a container to pack the item and move it. The container size needed for day i is the maximum item size moved on that day.

Given k days and array P as the item sizes, find out the minimum total container size required to move all the items.

Examples
Example 1:
Input: P = [10, 2, 20, 5, 15, 10, 1], d = 3
Output: 31
Explanation:
day 1 - [10, 2, 20, 5, 15]. ContainerSize = 20
day 2 - [10]. ContainerSize = 10
day 3 - [1]. ContainerSize = 1
Total = 20 + 10 + 1 = 31

Example 2:
Input: P = [10, 2, 20, 5, 15, 10, 1], d = 5
Output: 43
Explanation:
day 1 - move [10]. ContainerSize = 10
day 2 - move [2]. ContainerSize = 2
day 3 - move [20, 5, 15]. ContainerSize = 20
day 4 - move [10]. ContainerSize = 10
day 5 - move [1]. ContainerSize = 1
Total = 10 + 2 + 20 + 10 + 1 = 43

Example 3:
Input: P = [5, 4, 2, 4, 3, 4, 5, 4], d = 4
Output: 16
Explanation:
day 1 - [5, 4], containerSize = 5
day 2 - [2], containerSize = 2
day 3 - [4, 3], containerSize = 4
day 4 - [4, 5, 4], containerSize = 5
day 5 - move [1]. ContainerSize = 1
Total = 5 + 2 + 4 + 5 = 16

Example 4:
Input: P = [22, 12, 1, 14, 17], d = 2
Output: 39
Explanation:
day 1 - [22, 12], containerSize = 22
day 2 - [1, 14, 17], containerSize = 17
Total = 22 + 17 = 39
'''

from functools import lru_cache
from typing import List

class Solution():
    def minimumTotalContainerSize(self, containers: List[int], days: int) -> int:
        # If we have more days that containers to remove, invalid
        if len(containers) < days:
            return -1

        @lru_cache
        # Using lru_cache to implement DP, i is the index in our containers, d is the days remaining
        def minimumContaiers(i: int, d: int):
            if d == 1:
                return max(containers[i:])
            
            # Okay we are going to increment our i until we have reached it's maximal value
            maximalDay = len(containers) - d + 1
            maximalValue, output = 0, float('inf')
            for j in range(i, maximalDay):
                maximalValue = max(maximalValue, containers[j])
                output = min(output, maximalValue + minimumContaiers(j + 1, d - 1))
            return output
        return minimumContaiers(0, days)

s = Solution()
f = s.minimumTotalContainerSize([10, 2, 20, 5, 15, 10, 1], 3)
print(f)