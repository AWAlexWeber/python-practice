'''
#9
Given a list randomly sorted of the form of a tuple where the first elemenet represents the height and the second the number of people in front with an equal or higher height,
reconstruct the array to be in order.

[(7,0),(4,4),(7,1),(5,0),(6,1),(5,2)] -> [(5,0),(7,0),(5,2),(6,1),(4,4),(7,1)]
'''

# We accomplish this by placing each element into an expanding list, iterating over elements in sorted height.
# First we sort the array in descending heights. Then we sort the array by people in front. Then we place them into the array in order such that n is the index.

from typing import List
from collections import defaultdict

class Solution():
    def queueReconstruction(self, nums: List[tuple]) -> List[tuple]:
        o = []

        # Using a dictionary here to keep the values sorted properly
        d = defaultdict(lambda: defaultdict(lambda: 0))

        # O(n) time complexity, O(n) space complexity
        for n in nums:
            (height, count) = n
            d[height][count] += 1

        # Creating our output
        output = list()

        # Now we will sort the keys of the dictionary
        # Total time complexity is O(nlogn + n^2) = O(n^2)
        # Space complexity is O(n)
        for height in sorted(d.keys(),reverse=True):
            for position in sorted(d[height]):
                output.insert(position,(height,position))

        return output

    def optimalQueueReconstruction(self, nums: List[tuple]) -> List[tuple]:
        # Sorting
        nums.sort(key=lambda x:(-x[0], x[1]))
        output = []
        for n in nums:
            output.insert(n[1], n)
        return output

    def queueReconstructionTwo(self, nums: List[tuple]) -> List[tuple]:
        nums.sort(key=lambda t:(-t[0], t[1]))
        output = []
        for n in nums:
            output.insert(n[1], n)
        return output 


s = Solution()
print(s.queueReconstruction([(7,0),(4,4),(7,1),(5,0),(6,1),(5,2)]))
print(s.queueReconstructionTwo([(7,0),(4,4),(7,1),(5,0),(6,1),(5,2)]))