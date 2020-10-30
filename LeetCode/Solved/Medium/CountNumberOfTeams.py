'''
1395. Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5
'''

from typing import List
from collections import defaultdict
import collections

class Solution:
    # Nice and fast brute force solution
    # Do not use this as its O(n^3)
    def bruteForceNumTeams(self, rating: List[int]) -> int:
        out = 0
        for i in range(0, len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):
                    if rating[i] < rating[j] < rating[k]:
                        out += 1
                    elif rating[i] > rating[j] > rating[k]:
                        out += 1

        return out
        

    # Slightly faster solution
    # Uses dynamic programming to precompute how many pairs each value has
    def numTeamsDP(self, rating: List[int]) -> int:
        up = collections.defaultdict(list)
        down = collections.defaultdict(list)
        index = {val : idx + 1 for idx, val in enumerate(rating)} 
        
        # O(n^2) for collection pairs in ascending or descending order
        for i in range(1, len(rating)):
            r = rating[i]
            for c in range(i + 1, len(rating)):
                n = rating[c]
                if n > r:
                    up[r].append((r,n))
                elif n < r:
                    down[r].append((r,n))
            
        upKeys = sorted(up.keys())
        downKeys = sorted(down.keys())
        
        o = 0
        
        for i, r in enumerate(rating):
            for u in upKeys:
                if u <= r:
                    continue
                else:
                    if index[u] > i:
                        print(r,up[u])
                        o += len(up[u])
            for u in downKeys:
                if u >= r:
                    break
                else:
                    if index[u] > i:
                        print(r,down[u])
                        o += len(down[u])
                    
        return o

    # O(NLogN) Solution
    def numTeams(self, rating: List[int]) -> int:
        if not rating or len(rating) < 3:
            return 0
        cnt = 0
        dic = {}
        for i, num in enumerate(sorted(rating)):
            dic[num] = i
        cur = rating[:1]
        for i in range(1, len(rating)):
            total_small = dic[rating[i]]
            total_big = len(rating) - 1 - total_small
            cur_small = self.findIdx(cur, rating[i])
            cur_big = len(cur) - cur_small
            cur = cur[:cur_small] + [rating[i]] + cur[cur_small:]
            cnt += (cur_small * (total_big - cur_big)) + (cur_big * (total_small - cur_small))

        return cnt
            
    def findIdx(self, nums, target):
        # nums is sorted
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        k = 1
        while 2 * k < len(nums) and nums[2*k] < target:
            k *=2
        for i in range(k, min(2*k+1, len(nums))):
            if nums[i] > target:
                return i
                
s = Solution()
s.bruteForceNumTeams([2,5,3,4,1])