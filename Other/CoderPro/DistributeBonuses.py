'''
Bonuses questions.
'''

from typing import List

class Solution:
    def bonuses(self, arr: List[int]) -> List[int]:
        def backtrackModifyBonus(start: int, amount: int, o: list) -> None:
            while start >= 0:
                # If our start valley is now a peak, we break
                if (start == 0 or arr[start] > arr[start - 1]) and (start == len(arr) - 1 or arr[start] > arr[start + 1]):
                    if amount > 0:
                        o[start] += amount
                    return
                o[start] += amount
                start -= 1

        c, o = 1, list([1])
        for idx in range(1, len(arr)):
            if arr[idx] > arr[idx - 1]:
                c += 1
            elif arr[idx] < arr[idx - 1]:
                c -= 1

            o.append(c)

            # If valley, check for readjust and then continue forward
            if arr[idx] < arr[idx - 1] and (idx == len(arr) - 1 or arr[idx] < arr[idx + 1]):
                # Check for readjust
                if c != 1:
                    backtrackModifyBonus(idx, 1 - c, o)
                    c = 1

        return o

s = Solution()
print(s.bonuses([1,2,3,5,3,1]))
print(s.bonuses([1,2,1,7,6,5,1,5,6,5,4,3,2,1,0]))
print(s.bonuses([4,3,2,1]))
print(s.bonuses([1,1,1,1]))