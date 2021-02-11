'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''

from typing import List
from queue import Queue, deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        queue = deque([('', 0, 0)])
        while queue:
            cur_str, cur_open, cur_close = queue.popleft()
            if cur_open == n and cur_close == n:
                output.append(cur_str)
            else:
                if cur_open < n:
                    queue.append((cur_str + '(', cur_open + 1, cur_close))
                if cur_open > cur_close:
                    queue.append((cur_str + ')', cur_open, cur_close + 1))
        return output

s = Solution()
s.generateParenthesis(4)