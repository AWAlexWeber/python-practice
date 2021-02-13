# Given an image represented by an NxN matrix, rotate the image in place by 90 degrees to the right
from typing import List

def rotateImage(arr: List[List[int]]):
    # Handling empty cases
    if (len(arr) <= 0 or len(arr[0]) <= 0):
        return False

    n = len(arr)
    for l in range(len(arr) // 2):
        f = l
        s = n - 1 - l

        for i in range(f, s):
            o = i - f
            t = arr[f][i]

            # Performing swap
            arr[f][i] = arr[s - o][f]
            arr[s-o][f] = arr[s][s-o]
            arr[s][s-o] = arr[i][s]
            arr[i][s] = t
    
    return

testCase=[[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5]]
print(testCase)
rotateImage(testCase)
print(testCase)