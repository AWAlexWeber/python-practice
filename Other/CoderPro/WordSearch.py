''' 
Given a 2d array filled with words, find a word if it exists, otherwise return false.

F,M,K,O
O,F,O,K
D,M,A,Z

Foam exists, Foal does not
'''

from typing import List

class Solution:
    def wordSearch(self, word: str, arr: List[List[str]]) -> bool:
        # This is effectively just dfs with backtracking.
        # Attempting to start at every possible position, skipping previously visisted positions.
        # O(n*m) time complexity where n, m is the width/height of the array. This is likely the minimal time complexity.
        def attemptWord(word: str, i: int, j: int, visit: set) -> bool:
            
            if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
                return False
            if (i,j) in visit:
                return False

            if arr[i][j] == word[0]:
                visit.add((i,j))
                if len(word) == 1:
                    return True

                # Attempting to go deeper
                return attemptWord(word[1:], i + 1, j, visit) or attemptWord(word[1:], i - 1, j, visit) or attemptWord(word[1:], i, j + 1, visit) or attemptWord(word[1:], i, j + 1, visit) or attemptWord(word[1:], i, j - 1, visit)
            return False

        for i in range(len(arr)):
            for j in range(len(arr)):
                if attemptWord(word,i,j,set()):
                    return True
        return False

s = Solution()
print(s.wordSearch('foam', [['f','m','k','o'],['o','f','o','k'],['d','m','a','z']]))