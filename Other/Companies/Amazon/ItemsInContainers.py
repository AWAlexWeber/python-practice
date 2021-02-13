'''

Amazon would like to know how much inventory exists in their closed inventory system.

Given a string s consisting of items as "*" and losed compartments as an open and close "|", an array of starting indices startIndices, and an array of ending indices endIndeces.

Determine the number of items in closed compartments within the substring between the two indices, inclusive.

- An Item is represented as an asterisk
- A compartment is represented as a pair of pipes that may or may not have items between them (|)

Exampe
s = '|**|*|*'
start = [1,1]
end = [5, 6]

answer = [2,3]
'''

from typing import List

class Solution():
    def itemsInContainers(self, s: str, startIndices: List[int], endIndices: List[int]):
        # Forward computing known containers once it has been solved.
        # Key is the start index, value is the end index and the number of items contained within
        knownContainers = {}
        o = []

        for i in range(len(startIndices)):
            start, end = startIndices[i] - 1, endIndices[i] - 1
            total = 0

            # Getting next pipe
            while start < end and start < len(s) and s[start] != '|':
                start += 1

            while start in knownContainers:
                container = knownContainers[start]
                if container[0] >= end:
                    break
                total += container[1]
                start = container[0]

            start += 1

            currentTotal = 0
            currentIndex = start - 1
            while start <= end:

                if s[start] == '|':
                    knownContainers[currentIndex] = (start, currentTotal)
                    currentIndex = start
                    total += currentTotal
                    currentTotal = 0
                else:
                    currentTotal += 1

                start += 1

            o.append(total)

        return o

s = Solution()
s.itemsInContainers("|**|*|*",[1,1],[5,6])
            
