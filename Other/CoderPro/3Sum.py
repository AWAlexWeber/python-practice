'''
3 Sum. Find three values that add up to the target number.
'''

from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, data: List[int], target: int) -> List[tuple]:
        # 2-sum variant
        # O(n^2) time.
        count = defaultdict(lambda: list())
        for i, val_i in enumerate(data):
            for j, val_j in enumerate(data):
                if i == j:
                    continue
                count[val_i+val_j].append((i,j))

        print(count)
        output = list()
        visit = set()
        for i, val in enumerate(data):
            if target - val in count:
                for d in count[target - i]:

                    if i == d[0] or i == d[1]:
                        continue

                    val_i = val
                    val_j = data[d[0]]
                    val_k = data[d[1]]

                    s_data = sorted([val_i,val_j,val_k])
                    if str(s_data) not in visit:
                        output.append(s_data)
                        visit.add(str(s_data))
        
        return output

s = Solution()
print(s.threeSum([1,2,3,3,4,5,6,7,8,9,10],8))