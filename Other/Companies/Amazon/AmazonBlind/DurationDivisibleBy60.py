'''
Given a list of numbers and a target number. Find the number of pairs of numbers from the list whose sum is diviside by 60.

Example 1:
Input: [30,20,150,100,40]
Output: 3
Explanation:
(30, 150), (20, 100) and (20, 40) are pairs of numbers whose sum are divisible by 60.
'''

from typing import List
from collections import defaultdict
import math

class Solution():
    def durationBySixty(self, nums: List[int]) -> int:
        # This is effectively a two-sum problem.
        # We are going to build a dictionary and count the number % 60 in it. Then we will count the total number of available pairs.
        # We will use the binomial coefficient to calculate total number of pairs.
        pairs = defaultdict(lambda: 0)

        for n in nums:
            pairs[(n % 60)] += 1

        # Now for each key in our pairs, we check to see if the opposite (60 - value) exists. If so, we can count the number of pairs.
        output = 0
        for key in pairs.keys():
            # We will handle 30/60 seperately since they are unique cases
            if key == 30 or key == 60:
                continue
            # Not counting values >= 30 since we'd be counting matches twice
            elif key >= 30:
                continue

            elif (60-key) in pairs:
                # We found a match!
                keyCount = pairs[key]
                targetCount = pairs[60-key]
                output += (keyCount * targetCount)

        # Handling value of 30
        output += math.comb(pairs[30], 2)

        # Handling value of 60
        output += math.comb(pairs[0], 2)

        return output

s = Solution()
f = s.durationBySixty([30,60,60,60,60,90,120,150,70,70,70,50,50,50,50])
print(f)