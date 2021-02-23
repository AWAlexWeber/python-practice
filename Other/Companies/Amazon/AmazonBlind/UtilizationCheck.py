'''

'''

from typing import List
import math

class Solution():
    def autoscalePolicyCheck(self, averageUtil: List[int], instances: int) -> int:
        i = 0
        while i < len(averageUtil):
            # Check if we make an action
            if averageUtil[i] < 25 and instances > 1:
                instances /= 2
                i += 11
            elif averageUtil[i] > 60 and instances <= (10**8):
                instances *= 2
                i += 11
            else:
                i += 1
            instances = int(math.ceil(instances))
        return int(instances)

s = Solution()
print(s.autoscalePolicyCheck([1, 3, 5, 10, 80], 1))
print(s.autoscalePolicyCheck([25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80], 1))
print(s.autoscalePolicyCheck([30, 5, 4, 8, 19, 89], 5))
print(s.autoscalePolicyCheck([5, 10, 80], 1))
print(s.autoscalePolicyCheck([30,95,4,8,19,89], 100000000))