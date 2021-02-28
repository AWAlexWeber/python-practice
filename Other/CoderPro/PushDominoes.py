'''
Given an initial state of dominoes and an initial force, determine the resulting domino state

ie (where 0 = standing, -1 = fell left, 1 = fell right)
[0,0,0,0,0,0,0,0,0,0,0]
[0,0,1,0,0,0,-1,0,0,1,0]

We would return

[0,0,1,1,0,-1,-1,0,0,1,1]
'''

from typing import List

# O(n) time complexity, O(n) space complexity.
class Solution:
    def dominoPush(self, force: List[int]) -> List[int]:
        # Creating our dominos
        numDominos = len(force)
        dominos = [0] * numDominos

        # What we are going to do is the following;
        # Iterate from 0 to numDominos and process values using the following methodology:
        # If we have not ran into any force:
        #   If we run into a -l, set everything to the left of it as -1 until we find another -1
        #   If we run into a 1, search to the right to find another -1. Everytime we find another 1, set everything between the two indexes to 1

        for idx in range(numDominos):
            print(dominos,idx)

            if force[idx] == 0:
                continue
            # Handling going left
            if force[idx] == -1:
                for j in range(idx, -1, -1):
                    if dominos[j] == -1:
                        break
                    dominos[j] = -1
            # Handoing going right
            if force[idx] == 1:
                # Finding the next value, or the end
                nextValIdx = -1
                for j in range(idx + 1, numDominos):
                    if force[j] != 0:
                        nextValIdx = j
                        break
                # If the next value is equal to a 1, and we've continued falling to the right, setting all values inbetween
                if nextValIdx == -1 or force[nextValIdx] == 1:
                    for j in range(idx, (numDominos if nextValIdx == -1 else nextValIdx)):
                        dominos[j] = 1
                    idx = j + 1
                # If the next value is equal to a -1, we are going to set the first half to 1s and the second half to -1s
                # The middle of course stays at zero
                elif force[nextValIdx] == -1:
                    for j in range(idx, nextValIdx + 1):
                        if j < (idx + nextValIdx) / 2:
                            dominos[j] = 1
                        elif j > (idx + nextValIdx) / 2:
                            dominos[j] = -1
                    idx = j + 1

        return dominos

s = Solution()
print(s.dominoPush([0,0,1,0,0,0,-1,0,0,1,0]))
print(s.dominoPush([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,-1]))