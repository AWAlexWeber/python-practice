
from typing import List
from collections import defaultdict

class Solution:
    def multitasking(self, arr: List[int], cooldown: int) -> int:
        h, c = defaultdict(lambda: 0), 0
        for v in arr:
            h[v] += 1
            if h[v] > c:
                c = h[v]
    
        return ( (c - 1) * cooldown + c )

s = Solution()
print(s.multitasking([1,1,2,1,2,2,3,3,3,4],2))