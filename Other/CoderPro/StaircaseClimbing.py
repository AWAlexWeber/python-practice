''' Given a number of steps in a staircase, how many different ways are there to climb the stairs if you can take one or two step from each step.
Note that you must take one step on the final step '''

import time

class Solution:
    def numSteps(self, numSteps: int) -> int:
        # This is basically classic fibonacci problem.
        # Memoization / DFS approach
        memo = {}

        def dfs(step: int) -> int:
            if step in memo:
                return memo[step]
            
            if step >= numSteps - 1:
                return 1

            else:
                stepOne = dfs(step + 1)
                stepTwo = dfs(step + 2)
                memo[step] = stepOne + stepTwo
                return stepOne + stepTwo

        dfs(0)
        return memo[0]

def staircase(n):
    if n <= 1:
        return 1
    return staircase(n-1) + staircase(n-2)


def staircase2(n):
    prev = 1
    prevprev = 1
    curr = 0

    for i in range(2, n + 1):
        curr = prev + prevprev

    prevprev = prev
    prev = curr
    return curr

s = Solution()

# starting time
start = time.time()
print(s.numSteps(900))
end = time.time()
print(f"Runtime of the program is {end - start}")
start = time.time()
print(staircase(25))
end = time.time()
print(f"Runtime of the program is {end - start}")