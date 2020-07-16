from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
    match = {}
    out = 0

    # O(n)
    for i in nums:
        match[i] = match.setdefault(i, 0) + 1

        if match[i] > 1:
            out += match[i] - 1

    return out

print(numIdenticalPairs([1,2,3,1,1,3]))