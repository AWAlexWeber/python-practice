'''
Amazon OA - Storage Optimization

Amazon is experimenting with a flexible storage system for their warehouses. The storage unit consists of a shelving system which is one meter deep with removable vertical and horizontal separators. When all separators are installed, each storage space is one cubic meter (1' x 1' x 1'). Determine the volume of the largest space when a series of horizontal and vertical separators are removed.

Example
n = 6
m = 6
h = [4]
v = [2]
Consider the diagram below. The left image depicts the initial storage unit with n = 6 horizontal and m = 6 vertical separators, where the volume of the largest storage space is 1 x 1 x 1. The right image depicts that unit after the fourth horizontal and second vertical separators are removed. The maximum storage volume for that unit is then 2 x 2 x 1 = 4 cubic meters: 


 
Sample Case 0
Sample Input 0
STDIN Function
3 -> n = 3
3 -> m = 3
1 -> h[] size x = 1
2 -> h = [2]
1 -> v[] size y = 1
2 -> v = [2]
Sample Output 0
4
Explanation 0
There are n = m = 3 separators in the vertical and horizontal directions. Separators to remove are h = [2] and v = [2] so the unit looks like this:




Return the volume of the biggest space, 4, as the answer.

Sample Case 1
Sample Input 1
STDIN Function
2 -> n = 2
2 -> m = 2
1 -> h[] size x = 1
1 -> h = [1]
1 -> v[] size y = 1
2 -> v = [2]
Sample Output 1
4
Explanation 1
There are 2 vertical and two horizontal separators initially. After removing the two separators, h = [1] and v = [2], the top-right cell will be the largest storage space at 4 cubic meters.

Sample Case 2
Sample Input 2
STDIN Function
3 -> n = 3
2 -> m = 2
3 -> h[] size x = 3
1 -> h = [1, 2, 3]
2
3
2 -> v[] size y = 3
1 -> v = [1, 2]
2
Sample Output 2
12
Explanation 2
Initially there are n = 3 horizontal and m = 2 vertical separators. Remove separators h = [1, 2, 3] and v = [1, 2] so the unit looks like this:




The volume of the biggest storage space is 12
'''

from typing import List

# Essence of this problem is to find the two largest contiguous sets in both the horizontal and vertical axis, and then combine them to calculate the arrea
class Solution():
    def storageOptimization(self, h: List[int], v: List[int]) -> int:
        # First we will sort these guys. This is required and will take O(nlogn).
        h = sorted(h)
        v = sorted(v)

        # Finding the biggest sequence
        biggest_height = (0 if len(h) <= 0 else 1)
        biggest_vertical = (0 if len(v) <= 0 else 1)

        current_biggest_height = 1
        for idx, value in enumerate(h):
            # Does the next value minus one equal our current value? (aka is this still a consequetive sequence)
            if idx < len(h) - 1 and value == h[idx + 1] - 1:
                current_biggest_height += 1
                biggest_height = max(biggest_height, current_biggest_height)
            else:
                current_biggest_height = 1

        current_biggest_vertical = 1
        for idx, value in enumerate(v):
            # Does the next value minus one equal our current value? (aka is this still a consequetive sequence)
            if idx < len(v) - 1 and value == v[idx + 1] - 1:
                current_biggest_vertical += 1
                biggest_vertical = max(biggest_vertical, current_biggest_vertical)
            else:
                current_biggest_vertical = 1

        return (biggest_height + 1) * (biggest_vertical + 1)

s = Solution()
print(s.storageOptimization([1,2,3], [1,2]))
print(s.storageOptimization([2], [2]))
            