'''
Given an error rate array, eg [10,4,5,15,20,3,5,7], return if any error rate within range is (x,y) is larger than threshold.
Eg. threshold is 10, x= 1,y = 3, return True because 15 is larger than 10.
'''

from typing import List

# Unless I'm missing something this seems extremely easy. There is likely more to it than just this.
class Solution():
    def checkError(self, errorRange: List[int], nums: List[int], threshold: int) -> bool:
        for i in range(errorRange[0], errorRange[1] + 1):
            if nums[i] >= threshold:
                return True
        return False

s = Solution()
print(s.checkError([1,3], [10,4,5,15,20,3,5,7], 10))