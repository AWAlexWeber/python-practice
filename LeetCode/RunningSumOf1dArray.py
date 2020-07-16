from typing import List

def runningSum(nums: List[int]) -> List[int]:
    output = []
    p = 0
    for i in nums:
        output.append(p + i)
        p = p + i

    return output

runningSum(nums=[0,1,2,3,4,5,6,7,8,9])
