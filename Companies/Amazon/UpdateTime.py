'''
Amazon wants to update all of its radio towers. Radio towers may only be updated by being adjactent to radio towers that are already updated.

Given a 2d array where a 1 represents an updated radio tower and a 0 an out of date radio tower, how long will it take to update all radio towers?

[0,0,0,1,0]
[1,0,0,0,0]
[0,0,0,0,0]
[0,1,0,1,0]
[0,1,1,1,1]

In this example it takes two ticks

[1,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]

In this example it takes eight ticks
'''

# Using a queue for BFS since it is an effective datastructure for implementing a queue
from queue import Queue
from typing import List

class Solution():

    def maximumUpdateTime(self, nums: List[List[int]]):
        # Handling empty nums array
        if len(nums) <= 0 or len(nums[0]) <= 0:
            return -1

        # Basically BFS, aggregating all of the starting points.
        q = Queue()

        for r in range(len(nums)):
            for c in range(len(nums[0])):
                if nums[r][c] == 1:
                    # This is one of our entry points
                    q.put((r,c,0))

        # Checking to see if there were no entry points
        if q.empty():
            return -1

        # Alright, now what we're going to do is simply pop positions from q until we've processed every node
        processCount = 0

        while not q.empty():
            r, c, time = q.get()

            processCount = max(processCount, time)

            # North
            if r + 1 < len(nums) and nums[r + 1][c] == 0:
                nums[r + 1][c] = 1
                q.put((r + 1,c,time + 1))

            # South
            if r - 1 >= 0 and nums[r - 1][c] == 0:
                nums[r - 1][c] = 1
                q.put((r - 1,c,time + 1))

            # East
            if c + 1 < len(nums[0]) and nums[r][c + 1] == 0:
                nums[r][c + 1] = 1
                q.put((r, c + 1, time + 1))

            # West
            if c - 1 >= 0 and nums[r][c - 1] == 0:
                nums[r][c - 1] = 1
                q.put((r, c - 1, time + 1))

        return processCount

c = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[1,1,1,1,1],[1,1,1,1,1]]
s = Solution()
print(s.maximumUpdateTime(c))