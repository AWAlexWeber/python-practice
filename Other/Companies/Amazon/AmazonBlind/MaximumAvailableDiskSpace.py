'''
A user wants to store a file in a data center, but requests it to be replicated across each machine in a block. A block is defined as a continuous set of machines, starting from the first machine, with each block being next to one another and fixed in size. For example - if the block size is defined as 3, the first block is composed of machines 1 to 3, the second block is composed of machines 2 to 5, and so on.

Find the largest possible file the user can store in a data center, given a block size.

Input
freeSpace: a list of numbers representing the free space available in each machine of the data center

blockSize: a number representing the size of each block

Output
A number representing the amount of free space that the emptiest block in the data center has. The free space within a given block is the minimum free space of all the machines in it.

Constraints
The size of the block is always smaller than the number of machines in the freeSpace list. freeSpace values are never zero.

Examples
Example 1:
Input:
freeSpace = [8,2,4,5]

blockSize = 2

Output: 2
Explanation:
In this data center, the subarrays representing the free space of each block of size 2 are [8,2], [2,4], and [4,5]. The minimum available space of each blocks is 2, 2, and 4. The maximum of these values is 4. Therefore, the answer is 4.

Complexity
Both time complexity and O(n) space complexity must be around O(n).
'''

from collections import deque
from typing import List

def available_space(num_computer: int, free_space: List[int], block_length: int) -> int:
    # Sliding window maximum problem. Going to use a dequeue
    # We iterate over every value in our free_space
    output = float('-inf')
    deq = deque()

    for idx, value in enumerate(free_space):
        print(deq)
        # Removing our top value if it's outside of our window
        if len(deq) > 0 and deq[0][0] <= (idx - block_length):
            deq.popleft()
        # Removing all values that are greater than our minimal value.
        while len(deq) > 0 and deq[-1][1] >= value:
            deq.pop()
        # Appending whatever value we just got.
        deq.append((idx, value))
        if idx >= block_length:
            output = max(output, deq[0][1])

    return output        

print(available_space(4, [8,2,4,5], 2))