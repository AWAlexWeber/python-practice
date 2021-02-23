from collections import deque
from typing import List

def slidingWindowMaximum(nums: List[int], windowSize: int) -> List[int]:
    deq = deque()
    output = list()
    for idx, value in enumerate(nums):
        # While the value at the last index in our deque is LESS than value, we just pop them all out
        while deq and nums[deq[-1]] <= value:
            deq.pop()

        # Inserting our new value
        deq.append(idx)

        # Removing our head if it's outside the window
        if deq[0] <= (idx - windowSize):
            deq.popleft()

        if idx >= windowSize - 1:
            output.append(nums[deq[0]])

    return output

o = slidingWindowMaximum([10,5,12,5,4,3,9,8],3)
print(o)