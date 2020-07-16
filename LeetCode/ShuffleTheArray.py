from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = [0] * 2 * n
        index = 0
        while index < 2 * n:
            newIndex = (int)(index / 2 if index % 2 == 0 else n + (index / 2))
            out[index] = nums[newIndex]
            index += 1

        return out