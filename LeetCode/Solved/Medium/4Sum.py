'''
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # The format for the pairs is as follows:
        # Key: total sum of each pair, value is a list of pairs where the pair has the format of (pair 1 index, pair 2 index)
        pairs = {}
        
        # Building our pair set
        # This is O(n^2). Polynomial time is not fantastic but at least its limited to square time.
        for i, n in enumerate(nums):
            next = i + 1
            for j, m in enumerate(nums[next:]):
                jo = j + i + 1
                sumValue = n + m
                
                if sumValue not in pairs:
                    pairs[sumValue] = list()
                
                pairs[sumValue].append((i,jo))
                    
        # Pair set has been constructed
        # Now we want to find all possible pairs that have a matching value that equals the target

        # Knowing that for every value that exists, there exists a match for it that must be greater than or equal to half the target,
        # We will only do this for every value of sum pair up to half of the target
        o = set()
        output = list()
        
        # O(n * (n * (n - 1)/2)^2 )
        # or
        # n^3
        for sumValue in sorted(pairs):
            if sumValue > (target // 2):
                # No need to continue
                break
                
            targetSum = target - sumValue
            if targetSum in pairs:
                print(sumValue,targetSum)
                for pairOne in pairs[sumValue]:
                    for pairTwo in pairs[targetSum]:
                        if pairOne[0] == pairTwo[0] or pairOne[0] == pairTwo[1] or pairOne[1] == pairTwo[0] or pairOne[1] == pairTwo[1]:
                            continue
                        else:
                            fullPair = sorted([nums[pairOne[0]],nums[pairOne[1]],nums[pairTwo[0]],nums[pairTwo[1]]])
                            if str(fullPair) not in o:
                                output.append(fullPair)
                                o.add(str(fullPair))
                            
        return output
                    
                