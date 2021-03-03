'''
Find the Kth Largest Element within a list.
'''

# This is easily solved using a heap and popping it O(klogn) time.
# Our heap construction is O(n) time so our final complexity os O(klogn) and O(n) time/space.

from collections import defaultdict
from typing import List
from heapq import heappush, heappop

# Quickselect would be better but its a hard algorithm to come up with on the fly

class Solution:
    def findKthLargestElement(self, k: int, data: List[int]) -> int:
        # Using heapsort
        h = list()

        for d in data:
            heappush(h, -d)

        # Popping to k
        for i in range(1, k):
            if len(h) <= 0:
                return -1
            heappop(h)

        if len(h) <= 0:
            return -1
        return -heappop(h)

s = Solution()
print(s.findKthLargestElement(5,[1,2,3,4,5,6,7,8]))