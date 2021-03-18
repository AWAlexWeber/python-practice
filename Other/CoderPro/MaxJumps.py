'''
Given an array representing the number of jumps you can take from a position, what is the minimal number of jumps it takes to reach the end.
'''

from collections import defaultdict
from typing import List

class Solution:
    def numberOfJumps(self, arr: List[int]) -> int:
        # This is essentially DFS with memoization.
        memo = defaultdict(lambda: float('inf'))

        def dfs(idx: int, arr: List[int], memo: dict, currentJumps: int) -> int:
            if idx in memo:
                # If we've already visisted this index, check to see if our current number of jumps is better. If it isn't, we return
                if currentJumps >= memo[idx]:
                    return memo[idx]

            if idx >= len(arr):
                # Too far, we return infinity.
                return float('inf')

            if idx == len(arr) - 1:
                # We've reached the end, checking if this was the fastest and returning.
                memo[idx] = min(currentJumps, memo[idx])
                return currentJumps

            # Okay, we haven't visisted this index before (or our distance is better), we haven't reached the end and we haven't gone too far.
            # We need to explore starting with the maximal number of jumps available at this index.
            bestNumberOfJumps = float('inf')

            for jumpCount in range(arr[idx], 0, -1):
                bestNumberOfJumps = min(dfs(idx + jumpCount, arr, memo, currentJumps + 1), bestNumberOfJumps)

            # Letting everyone know what the best path for this index currently is.
            memo[idx] = bestNumberOfJumps
            return memo[idx]

        dfs(0, arr, memo, 0)
        return memo[len(arr) - 1]

s = Solution()
print(s.numberOfJumps([3,2,5,1,1,9,3,4,1,1,1,1,5,2,4,6,7,1,3,7,8,3,4,7]))