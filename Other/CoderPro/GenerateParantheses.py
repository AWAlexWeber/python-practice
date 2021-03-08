'''
Given a number generate all permutations of that number of paranetheses that are valid
'''
from typing import List

# DFS with pruning.
class Solution:
    def generateParantheses(self, num: int) -> List[List[str]]:
        # We are going to create an output list, then dfs for all possible values
        output = list()

        def dfs(l: int, r: int, s: str):
            # L represents number of left parantheses left, r represents right parantheses left.
            # We prune any branch where r < l.
            # Note by l I mean ( and by r I mean )
            if l == 0 and r == 0:
                output.append(s)
                return

            if l > 0:
                dfs(l - 1, r , s[:] + '(')
            if r > l:
                dfs(l, r - 1, s[:] + ')')

        dfs(num, num, '')
        return output

s = Solution()
print(s.generateParantheses(3))