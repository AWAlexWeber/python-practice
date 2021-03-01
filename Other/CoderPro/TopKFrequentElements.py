'''
Top K Frequent Elements
'''

from heapq import heapify, heappush, heappop
from typing import List
from collections import defaultdict

class Solution:
    def topKFrequentElements(self, data: List[int], k: int):
        # We are going to do this using a heap
        # We will pop an element, increment its count, then reinsert it using tuples.
        # Pop will be O(logn) + O(nlogn) to rebalance.
        # Insert will be O(logn) + O(nlogn) to rebalance.
        # This means that we effectively have O(nklogn) to get the top k frequent elements, with O(n) space.

        # O(n) time and O(n) space.
        count = defaultdict(lambda: 0)
        for value in data:
            count[value] += 1

        # Inserting into heap
        h = list()
        heapify(h)
        # O(n) time to build a heap
        for value in count.keys():
            # Inverting for max heap
            heappush(h,(-count[value], value))

        # O(klogn) time
        output = list()
        for n in range(k):
            if len(h) <= 0:
                break
            output.append(heappop(h)[1])
        return output

s = Solution()
print(s.topKFrequentElements([1,1,2,5,4,32,6,2,1,2,3,5,6,4,4,2,1,6,7,2,3,4,5,6,7,3,2,3,5,1], 30))